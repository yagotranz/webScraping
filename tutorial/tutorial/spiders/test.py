import scrapy
from scrapy.item import Item, Field
import csv


class movementItem(scrapy.Item):
	fecOp = scrapy.Field()
	fecVal = scrapy.Field()
	oficina = scrapy.Field()
	concepto = scrapy.Field()
	importe = scrapy.Field()
	saldo = scrapy.Field()



with open('body.txt', 'rb') as f:
	body = f.read()
	
print body

			
			
			