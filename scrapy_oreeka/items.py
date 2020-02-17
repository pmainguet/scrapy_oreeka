# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Plante(scrapy.Item):
    city = scrapy.Field()
    title = scrapy.Field()
    nom_latin = scrapy.Field()
    famille = scrapy.Field()
    vegetation = scrapy.Field()
    entretien = scrapy.Field()
    besoin_eau = scrapy.Field()
    multiplication = scrapy.Field()
    rusticite = scrapy.Field()
    type_sol = scrapy.Field()
    humidite_sol = scrapy.Field()
    ensoleillement = scrapy.Field()
    plantation = scrapy.Field()
    recolte = scrapy.Field()
    intro_plante = scrapy.Field()
    semis_info = scrapy.Field()
    culture = scrapy.Field()
    pass
