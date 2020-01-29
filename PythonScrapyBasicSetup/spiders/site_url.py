# -*- coding: utf-8 -*-
import logging
import scrapy
from bs4 import BeautifulSoup
# scrapy_splash import throws an error, but nothing to worry about still runs.
from scrapy_splash import SplashRequest
import scrapy_splash


class site_name(scrapy.Spider):
    name = 'site_name'
    allowed_domains = ['site_name.com']
    start_urls = (
        '#urls')
    
    # The current script runs the desired javascript on the page. Remember to keep it simple, you don't want too much heavy lifting
    # for the Splash so if neccesary slip up the scripts per single page. Luascript circumferences the javascript through jsfunc.
    #***ATTENTION*** Make sure the user-agent's are compatible with the javascript, it is not dynamic yet.
    javascript_to_be_ran = """
        function main(splash)
            splash.plugins_enabled = true
            assert(splash:go(splash.args.url))
            local get_dimensions = splash:jsfunc([[
                function () {
                var result = document.getElementsByClassName('sectionBottomLink')[1].getClientRects()[0];
                return {"x": result.left, "y": result.top}}
                ]]) 
            splash:wait(5.0)
            splash:set_viewport_full()
            local dimensions = get_dimensions()
            splash:mouse_click(dimensions.x, dimensions.y)
            -- Wait split second to allow event to propagate.
            splash:wait(2.0)
            return splash:html()
        end"""

# The way I scrape is basically find the query I want on a page to get results, then follow each of those result pages, so start_requests
#  follows the intial page can be built out if necessary, but yet had to.
    def start_requests(self):
        for urls in self.start_urls:
            yield scrapy.Request(urls, callback=self.following_listings)

#pages that are going to be scraped set up with the splash requests
    def following_listings(self, response):
        #this link will be to follow the links on each page 
        url_endline =  # ex: response.css('a.slider-item').xpath('@href').extract()
        for follow_url in url_endline:
            #baseurl e.g. : https://www.redfin.com'
            mod_url = '#baseurl'+follow_url
            # overriding controls for splash
            yield SplashRequest(mod_url, self.parse, args={
                'wait': 0.5, 
                'html': 1, 
                'endpoint': 'render.html',
                'lua_source': self.javascript_to_be_ran,
                # If running a larger javascript keep to single slot
                'slot_policy': scrapy_splash.SlotPolicy.SINGLE_SLOT})

# items to get on each page 
    def parse(self, response):
        yield {
            'address': response.css('span.street-address::text').extract(),
            'listing_dates': response.css('tr.PropertyHistoryEventRow').css('td.date-col::text').extract(),
            'CRMLS_ID': response.css('tr.PropertyHistoryEventRow').css('td.event-col').css('span.source::text').extract(),
            'Event': response.css('tr.PropertyHistoryEventRow').css('td.event-col').css('div.event::text').extract(),
            'price': response.css('tr.PropertyHistoryEventRow').css('td.price-col::text').extract()
        }
