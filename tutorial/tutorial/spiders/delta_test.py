import scrapy
from scrapy.item import Item, Field
import string
import re
import csv
import codecs
import json
import requests








class QuotesSpider(scrapy.Spider):
	name = "quotes1"
	
	


	def start_requests(self):
		"urls = ['file:///home/yago/tranz-scrapy/tutorial/tutorial/spiders/body.html']"
		urls = ['http://127.0.0.1/body.html']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		
		table1 = []
		row1 = []
		rows = response.xpath('//table[@id="tablaMovimientos"]/tbody/tr')
		for row in rows:
			
			
			td1 = row.xpath('td[1]/text()').extract()
			
			td1 = ''.join(c for c in td1 if c not in '\r\t\n')
			
			td1 = re.sub('[\t\r\n]','',td1)
			
			row1.append({'fecOp':td1})
			td2 = row.xpath('td[2]/text()').extract()
			td2 = ''.join(c for c in td2 if c not in '\r\t\n')
			td2 = re.sub('\W+','', td2 )


			row1.append({'fecVal':td2})
			td3 = row.xpath('td[3]/text()').extract()
			td3 = ''.join(c for c in td3 if c not in '\r\t\n')
			"td3 = re.sub('\W+','', td3 )"
			td3 = re.sub('[\t\r\n]','',td3)
			
			
			row1.append({'oficina':td3})
			td4 = row.xpath('td[4]/text()').extract()
			td4 = ''.join(c for c in td4 if c not in '\r\t\n')
			td4 = re.sub('[\t\r\n]','',td4)
			row1.append({'Concepto':td4})
			td5 = row.xpath('td[5]/text()').extract()
			td5 = ''.join(c for c in td5 if c not in '\r\t\n')
			td5 = re.sub('[\t\r\n]','',td5)
			
			td5 = td5.replace(u'\u20ac','EUR')
			row1.append({'Importe':td5})
			td6 = row.xpath('td[6]/text()').extract()
			td6 = ''.join(c for c in td6 if c not in '\r\t\n')
			td6 = re.sub('[\t\r\n]','',td6)
			
			td6 = td6.replace(u'\u20ac','EUR')
			row1.append({'Saldo':td6})

			
			
			
			table1.append(row1)
			row1 = []
		
		post_json(table1)



def post_json(tbl):
	
	tabla = json.dumps(tbl)
	r = requests.post('http://127.0.0.1:3000/bancamarch', data={'json': tabla})
	
	
	
	
        
