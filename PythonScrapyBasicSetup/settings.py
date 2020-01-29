# -*- coding: utf-8 -*-

BOT_NAME = 'PythonScrapyBasicSetup'

SPIDER_MODULES = ['PythonScrapyBasicSetup.spiders']
NEWSPIDER_MODULE = 'PythonScrapyBasicSetup.spiders'

# maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
# timeout for processing DNS queries in seconds(float) (default: 60)
DNS_TIMEOUT = 60
# time(sec) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 60

# use telnet console
TELNETCONSOLE_ENABLED = False

# delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 5
# download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# maximum number of times to retry
RETRY_TIMES = 2
# HTTP response codes to retry
RETRY_HTTP_CODES = [500, 502, 503, 504]

# disable cookies
COOKIES_ENABLED = False

#SPLASH SETTINGS
SPLASH_URL = 'http://0.0.0.0:8050'
SPLASH_COOKIES_DEBUG = True
SPLASH_LOG_400 = True
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# TOR SETTINGS
#Some websites block tor exit nodes
HTTP_PROXY = 'http://127.0.0.1:9052'
AUTH_PASSWORD = 'secretPassword'
CONTROL_PORT = 9051

# if defined, it will force exit nodes to be from given country/countries
# http://www.b3rn3d.com/blog/2014/03/05/tor-country-codes/
# EXIT_NODES = '{br}'

# number of HTTTP request before the IP change
# delete or set to None if you don't want to use it
MAX_REQ_PER_IP = 1000

# downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'PythonScrapyBasicSetup.middlewares.user_agent.RandomUserAgentMiddleware': 400,
    # 'PythonScrapyBasicSetup.middlewares.proxy.HttpProxyMiddleware': 410,
    #'PythonScrapyBasicSetup.middlewares.proxy.TorProxyMiddleware': 410
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}

ITEM_PIPELINES = {
    'PythonScrapyBasicSetup.pipelines.PythonscrapybasicsetupPipeline': 300,
  
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}


