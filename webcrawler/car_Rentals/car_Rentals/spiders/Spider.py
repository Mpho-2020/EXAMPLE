import scrapy

class Rentals(scrapy.Spider):
    name = 'cars'
    start_urls =['https://www.gumtree.co.za']
    def parse(self,response):
        wrapper =response.css('li').css('a')
        href =self.start_urls[0] + wrapper[1].attrib['href']
        
        print(href)

        yield scrapy.Request(href,callback= self.getLinkTo)


    def getLinkTo(self,response):
        wrapper_gau=response.css('div.container-srp-showcase')
        gau_Item=wrapper_gau.css('div:nth-child(1)')
        url =self.start_urls[0] + gau_Item.css('a').attrib['href']
        print(url)
        yield scrapy.Request(url,callback=self.getCars)
    
    def getCars(self,response):
        print(response.url)
        carName =response.css('::Text')


