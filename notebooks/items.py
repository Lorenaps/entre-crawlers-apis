import scrapy

class Vereador(scrapy.Item):
    
    nome = scrapy.Field()
    contatos = scrapy.Field()