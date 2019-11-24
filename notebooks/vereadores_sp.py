import scrapy
from scrapy.loader import ItemLoader
from items import Vereador

class VereadoresSpider(scrapy.Spider):
    name = 'veradores_sp'
    start_urls = ['http://www.saopaulo.sp.leg.br/vereadores/']

    def parse(self, response):      
        lista_veradores = response.css('p.vereador-name a::attr(href)').getall()
        
        for item in lista_veradores:
            yield response.follow(item, self.parse_vereador)
    
    
    def parse_vereador(self, response):
        
        item_loader = ItemLoader(Vereador(), response)
        
        item_loader.add_css('nome', 'p.vereador-name a::text')
        item_loader.add_css('contatos', 'div.vereador-data ul li a::text')
    
        return item_loader.load_item()