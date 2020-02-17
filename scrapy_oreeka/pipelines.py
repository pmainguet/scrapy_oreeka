# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyOreekaPipeline(object):
    def process_item(self, item, spider):
        #toupdate
        item['zipcode'] = item['city'][2]
        item['city'] = item['city'][0]
        if not re.match("^38", item['zipcode']):
            raise DropItem("Item not in correct area: %s" % item)
        item['last_updated']=datetime.now().timestamp()
        item['posted_on'] = datetime.strptime(item['posted_on'][0].replace(' à ',' '), '%d/%m/%Y %Hh%M').timestamp()
        item['price']=item['price'][0].replace(' ','')
        item['time_online']=(float(item['last_updated'])-float(item['posted_on']))/(24*60*60)
        if item.get('surface'):
            item['surface']=item['surface'][0].replace(' m²','')
            item['price_surface']= int(item['price'])/int(item['surface'])
        for q in self.quartiers):
            if item['description'].find(q) >= 0:
                item['quartier'] = q
                break
        return item
