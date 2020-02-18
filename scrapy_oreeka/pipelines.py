# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy import signals
from scrapy.exporters import CsvItemExporter

class ScrapyOreekaPipeline(object):
    
    def clean_paragraph(self, input):
        regex = re.compile(r'[\xa0\n\r\t]')
        return regex.sub(" ", input).replace ("  ", "")

    def process_table (self, input):
        mois = {
            'JANVIER': 1,
            'FÉVRIER': 2,
            'MARS':3,
            'AVRIL':4,
            'MAI':5,
            'JUIN':6,
            'JUILLET':7,
            'AOÛT':8,
            'SEPT.':9,
            'OCT.':"O",
            'NOV.':"N",
            'DÉC.':"D"
        }

        return ("").join(list(map(lambda x: str(mois[x]), input)))
    
    def process_item(self, item, spider):
        
        item['vegetation'] = self.clean_paragraph(item['vegetation'][0])
        item['rusticite'] = self.clean_paragraph(item['rusticite'][0])
        item['ensoleillement'] = self.clean_paragraph(item['ensoleillement'][0])
        if('plantation' in item):
            item['plantation'] = self.process_table(item['plantation'])
        if('floraison' in item):
            item['floraison'] = self.process_table(item['floraison'])
        if('recolte' in item):
            item['recolte'] = self.process_table(item['recolte'])
        if('intro_plante' in item):
            item['intro_plante'] = self.clean_paragraph(item['intro_plante'])
        if('semis_info' in item):
            item['semis_info'] = self.clean_paragraph(item['semis_info'])
        if('culture' in item):
            item['culture'] = self.clean_paragraph(item['culture'])
        if('maladie' in item):
            item['maladie'] = self.clean_paragraph(item['maladie'])
        if('conseil_recolte' in item):
            item['conseil_recolte'] = self.clean_paragraph(item['conseil_recolte'])
        if('conseil_multiplication' in item):
            item['conseil_multiplication'] = self.clean_paragraph(item['conseil_multiplication'])
        if('conseil' in item):
            item['conseil'] = self.clean_paragraph(item['conseil'])
        if('histoire' in item):
            item['histoire'] = self.clean_paragraph(item['histoire'])
        return item

class CsvPipeline(object):

  fields = [
        'title',
        'url',
        'famille',
        'nom_latin',
        'vegetation',
        'entretien',
        'besoin_eau',
        'rusticite',
        'humidite_sol',
        'type_sol',
        'ensoleillement',
        'multiplication',
        'plantation',
        'floraison',
        'recolte',
        'intro_plante',
        'semis_info',
        'culture',
        'maladie',
        'conseil_recolte',
        'conseil_multiplication',
        'conseil',
        'histoire',
  ]

  def __init__(self):
    self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    self.exporter.fields_to_export = self.fields
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
