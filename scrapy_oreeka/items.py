# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class Plante(scrapy.Item):
    url = scrapy.Field()
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
    floraison = scrapy.Field()
    recolte = scrapy.Field()
    intro_plante = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    semis_info = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    culture = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    maladie = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    conseil_recolte = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    conseil_multiplication = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    conseil = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    histoire = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    pass
