# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class MelodysoftItem(scrapy.Item):
	name = Field()
	email          = Field()
	post           = Field()
	host           = Field()
	place_from     = Field()
	place_to       = Field()
	academic_level = Field()
	post_date      = Field()

	pass