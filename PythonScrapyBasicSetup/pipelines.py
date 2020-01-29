# -*- coding: utf-8 -*-

#CsvItemExporter(file, include_headers_line=True, join_multivalued=', ', **kwargs)
from scrapy.exporters import CsvItemExporter

class PythonscrapybasicsetupPipeline(object):

    def process_item(self, item, spider):
        #Returns Multiple Addresses, just use one
        item['address'] = item['address'][0]
        #export to csv 
        return self.exporter.export_item(item)
        
    def open_spider(self, spider):
        self.file = open('redfin.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

 