import scrapy

from scrapy.loader import ItemLoader

from oreeka_spider.items import Plante

class OreekaSpider(scrapy.Spider):
    name = "oreeka"
    allowed_domains=['ooreka.fr']

    def __init__(self,*args, **kwargs):
        self.start_urls = self.load_url()

    def parse(self, response):
        l = ItemLoader(item=Plante(),response=response)
        l.add_value('url', response.request.url)
        l.add_value('title', response.xpath('//div[@id="resume_plante"]/p/text()'))
        l.add_value('nom_latin',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"]/ul/li[2]/p[2]'))
        l.add_value('famille',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"]/ul/li[2]/p[2]')
        l.add_value('vegetation',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][2]/ul/li[3]/div/span/text()'))
        l.add_value('entretien',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[1]/div/span/span[2]/strong/text()'))
        l.add_value('besoin_eau',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[1]/div/span/span[2]/strong/text()').get()
        l.add_value('multiplication',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[4]/div/span/span/strong/text()').get()
        l.add_value('rusticite',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[5]/div/span/span[1]/following::text()'))
        l.add_value('type_sol',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[6]/div/span/span/strong/text()'))
        l.add_value('humidite_sol',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[8]/div/span/span/strong/text()'))
        l.add_value('ensoleillement',response.xpath('//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][4]/ul/li[1]/div/div/span[1]/following-sibling::text()'))
        l.add_value('plantation',response.xpath('//div["tableau_periodicite"]/div[1]/table/tr/td[@class="_selected1 selectionne"]/text()'))
        l.add_value('recolte',response.xpath('//div["tableau_periodicite"]/div[2]/table/tr/td[@class = "_selected3 selectionne"]/text()'))
        l.add_value('intro_plante',(" ").join(response.xpath('//div["intro_longue_plantes"]/div[@class="article"]/p/text()').getall())
        l.add_value('semis_info',(" ").join(response.xpath('//div["texte_plantes article"]/h2[@id = "semis-et-plantation"]/following::div[1]/div/p/text()').getall())
        l.add_value('culture',(" ").join(response.xpath('//div["texte_plantes article"]/h2[@id = "culture-et-entretien"]/following::div[1]/div').getall())
        yield l.load_item()

     def load_url(self):
        
        return [
            "https://jardinage.ooreka.fr/plante/voir/110/petit-pois"
        ]