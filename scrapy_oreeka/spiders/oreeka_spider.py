import scrapy

from scrapy.loader import ItemLoader

from scrapy_oreeka.items import Plante

class OreekaSpider(scrapy.Spider):
    name = "oreeka_spider"
    allowed_domains=['ooreka.fr']

    def __init__(self,*args, **kwargs):
        self.start_urls = self.load_url()

    def parse(self, response):
        l = ItemLoader(item=Plante(),response=response)
        l.add_value('url', response.request.url)
        l.add_xpath('title', '//div[@id="resume_plante"]/p/text()')
        l.add_xpath('nom_latin','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"]/ul/li[3]/p[2]/text()')
        l.add_xpath('famille','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"]/ul/li[2]/p[2]/text()')
        l.add_xpath('vegetation','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][2]/ul/li[3]/div/span/text()')
        l.add_xpath('entretien','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[1]/div/span/span[2]/strong/text()')
        l.add_xpath('besoin_eau','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[1]/div/span/span[2]/strong/text()')
        l.add_xpath('multiplication','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[4]/div/span/span/strong/text()')
        l.add_xpath('rusticite','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[5]/div/span/span[1]/following::text()')
        l.add_xpath('type_sol','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[6]/div/span/span/strong/text()')
        l.add_xpath('humidite_sol','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][3]/ul/li[8]/div/span/span/strong/text()')
        l.add_xpath('ensoleillement','//div[@id="resume_plante"]/div["w_1_2 parties_plantes"][4]/ul/li[1]/div/div/span[1]/following-sibling::text()')
        l.add_xpath('plantation','//div["tableau_periodicite"]/div/p[normalize-space(text())="Plantation"]/following::table/tr/td[@class = "_selected3 selectionne"]/text()')
        l.add_xpath('floraison','//div["tableau_periodicite"]/div/p[normalize-space(text())="Floraison"]/following::table/tr/td[@class = "_selected3 selectionne"]/text()')
        l.add_xpath('recolte','//div["tableau_periodicite"]/div/p[normalize-space(text())="Récolte"]/following::table/tr/td[@class = "_selected3 selectionne"]/text()')
        l.add_xpath('intro_plante','//div["intro_longue_plantes"]/div[@class="article"]')
        l.add_xpath('semis_info','//div["texte_plantes article"]/h2[@id = "semis-et-plantation"]/following::div[1]/div')
        l.add_xpath('culture','//div["texte_plantes article"]/h2[@id = "culture-et-entretien"]/following::div[1]/div')
        l.add_xpath('maladie','//div["texte_plantes article"]/h2[@id = "maladies-nuisibles-et-parasites"]/following::div[1]/div')
        l.add_xpath('conseil_recolte','//div["texte_plantes article"]/h2[@id = "recolte"]/following::div[1]/div')
        l.add_xpath('conseil_multiplication','//div["texte_plantes article"]/h2[@id = "multiplication"]/following::div[1]/div')
        l.add_xpath('conseil','//div["texte_plantes article"]/h2[@id = "conseils-ecologiques"]/following::div[1]/div')
        l.add_xpath('histoire','//div["texte_plantes article"]/h2[@id = "un-peu-d-histoire"]/following::div[1]/div')
        yield l.load_item()

    def load_url(self):
        return [
            "https://jardinage.ooreka.fr/plante/voir/104/navet",
            "https://jardinage.ooreka.fr/plante/voir/110/petit-pois",
            "https://jardinage.ooreka.fr/plante/voir/112/topinambour",
            "https://jardinage.ooreka.fr/plante/voir/116/radis-d-hiver",
            "https://jardinage.ooreka.fr/plante/voir/117/rhubarbe",
            "https://jardinage.ooreka.fr/plante/voir/121/ail",
            "https://jardinage.ooreka.fr/plante/voir/139/grenadier",
            "https://jardinage.ooreka.fr/plante/voir/14/rutabaga",
            "https://jardinage.ooreka.fr/plante/voir/1531/poivron",
            "https://jardinage.ooreka.fr/plante/voir/16/basilic",
            "https://jardinage.ooreka.fr/plante/voir/1749/poivrier-du-sichuan",
            "https://jardinage.ooreka.fr/plante/voir/179/chenopode",
            "https://jardinage.ooreka.fr/plante/voir/18/courgette",
            "https://jardinage.ooreka.fr/plante/voir/190/fenouil-officinal",
            "https://jardinage.ooreka.fr/plante/voir/2/framboisier",
            "https://jardinage.ooreka.fr/plante/voir/20/melon",
            "https://jardinage.ooreka.fr/plante/voir/2013/trefle",
            "https://jardinage.ooreka.fr/plante/voir/212/blette",
            "https://jardinage.ooreka.fr/plante/voir/221/soleil",
            "https://jardinage.ooreka.fr/plante/voir/223/angelique",
            "https://jardinage.ooreka.fr/plante/voir/232/brocoli",
            "https://jardinage.ooreka.fr/plante/voir/234/chou-chinois",
            "https://jardinage.ooreka.fr/plante/voir/235/choux-de-bruxelles",
            "https://jardinage.ooreka.fr/plante/voir/236/chou-fleur",
            "https://jardinage.ooreka.fr/plante/voir/253/choux-non-pommes",
            "https://jardinage.ooreka.fr/plante/voir/254/chou-rave",
            "https://jardinage.ooreka.fr/plante/voir/255/concombre",
            "https://jardinage.ooreka.fr/plante/voir/256/cornichon",
            "https://jardinage.ooreka.fr/plante/voir/261/oignon",
            "https://jardinage.ooreka.fr/plante/voir/265/tomate",
            "https://jardinage.ooreka.fr/plante/voir/274/fraisier",
            "https://jardinage.ooreka.fr/plante/voir/295/laurier-sauce",
            "https://jardinage.ooreka.fr/plante/voir/30/thym",
            "https://jardinage.ooreka.fr/plante/voir/316/anis-vert",
            "https://jardinage.ooreka.fr/plante/voir/336/hysope",
            "https://jardinage.ooreka.fr/plante/voir/34/radis",
            "https://jardinage.ooreka.fr/plante/voir/369/fenouil-bulbeux",
            "https://jardinage.ooreka.fr/plante/voir/37/aubergine",
            "https://jardinage.ooreka.fr/plante/voir/422/potiron",
            "https://jardinage.ooreka.fr/plante/voir/464/melisse",
            "https://jardinage.ooreka.fr/plante/voir/480/liveche",
            "https://jardinage.ooreka.fr/plante/voir/484/panais",
            "https://jardinage.ooreka.fr/plante/voir/492/equisetum-hyemale",
            "https://jardinage.ooreka.fr/plante/voir/495/vigne",
            "https://jardinage.ooreka.fr/plante/voir/515/myrte",
            "https://jardinage.ooreka.fr/plante/voir/517/pourpier",
            "https://jardinage.ooreka.fr/plante/voir/518/raifort",
            "https://jardinage.ooreka.fr/plante/voir/54/aneth",
            "https://jardinage.ooreka.fr/plante/voir/541/cumin",
            "https://jardinage.ooreka.fr/plante/voir/56/ciboulette",
            "https://jardinage.ooreka.fr/plante/voir/57/coriandre",
            "https://jardinage.ooreka.fr/plante/voir/574/verveine-citronnelle",
            "https://jardinage.ooreka.fr/plante/voir/58/estragon",
            "https://jardinage.ooreka.fr/plante/voir/60/menthe",
            "https://jardinage.ooreka.fr/plante/voir/61/origan",
            "https://jardinage.ooreka.fr/plante/voir/62/oseille",
            "https://jardinage.ooreka.fr/plante/voir/63/persil",
            "https://jardinage.ooreka.fr/plante/voir/64/romarin",
            "https://jardinage.ooreka.fr/plante/voir/66/sauge-officinale",
            "https://jardinage.ooreka.fr/plante/voir/69/asperge",
            "https://jardinage.ooreka.fr/plante/voir/699/citronnelle",
            "https://jardinage.ooreka.fr/plante/voir/70/carotte",
            "https://jardinage.ooreka.fr/plante/voir/706/perilla",
            "https://jardinage.ooreka.fr/plante/voir/74/poireau",
            "https://jardinage.ooreka.fr/plante/voir/84/betterave",
            "https://jardinage.ooreka.fr/plante/voir/85/haricot",
            "https://jardinage.ooreka.fr/plante/voir/915/celeri",
            "https://jardinage.ooreka.fr/plante/voir/98/epinard",
            "https://jardinage.ooreka.fr/plante/voir/99/feve",
        ]