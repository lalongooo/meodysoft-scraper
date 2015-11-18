from scrapy.spiders 		import Spider
from scrapy.selector 		import Selector
from nettuts.items		import NettutsItem
from scrapy.http		import Request

class MelodysoftSpider(Spider):
    name = 'melodysoft'
    start_urls = ['http://gbooks1.melodysoft.com/app?ID=pizarra1']
    rules = (
        # Extract links for next pages
        Rule(LinkExtractor(allow=(), restrict_xpaths=("/html/body/center[4]/table/tr/td/font/b/a[8]/@href")), callback='parse_page', follow=True),
    )

    def parse(self, response):
        print '##########################################################################################'
        print response.xpath("/html/body/center[4]/table/tr/td/font/b/a[8]/@href").extract()[0]
        print '##########################################################################################'
        return self.parse_page(response)

    def parse_page(self, response):

        for tbl in response.xpath("/html/body/center[3]/table[@bgcolor='#002D2D']"):
            name            =   tbl.xpath("tr[1]/td[1]/font[@color='#FFB442']/b/text()").extract()[0]
            email           =   tbl.xpath("tr[1]/td[1]/font[3]/a/img/@alt").extract()[0] if tbl.xpath("tr/td[@align='left']/font[3]/a/img/@alt").extract() else ""
            post            =   tbl.xpath("tr[2]/td/table/tr/td[1]/font/font[1]/text()").extract()[0] if tbl.xpath("tr[2]/td/table/tr/td[1]/font/font[1]/text()").extract() else ""
            host            =   tbl.xpath("tr[2]/td/table/tr/td[1]/font/font[2]/b/text()").extract()[0] if tbl.xpath("tr[2]/td/table/tr/td[1]/font/font[2]/b/text()").extract() else ""
            place_from      =   tbl.xpath("tr[2]/td/table/tr/td[2]/font[3]/p/font/text()").extract()[0] if tbl.xpath("tr[2]/td/table/tr/td[2]/font[3]/p/font/text()").extract() else ""
            place_to        =   tbl.xpath("tr[2]/td/table/tr/td[2]/font[5]/font[1]/text()").extract()[0] if tbl.xpath("tr[2]/td/table/tr/td[2]/font[5]/font[1]/text()").extract() else ""
            academic_level  =   tbl.xpath("tr[2]/td/table/tr/td[2]/font[5]/font[2]/b/text()").extract()[0] if tbl.xpath("tr[2]/td/table/tr/td[2]/font[5]/font[2]/b/text()").extract() else ""
            post_date       =   tbl.xpath("tr[1]/td[2]/font[2]/text()").extract()[0] if tbl.xpath("tr[1]/td[2]/font[2]/text()").extract() else ""

            yield{
                'name':             name.encode('ascii', 'ignore'),
                'email':            email.encode('ascii', 'ignore'),
                'post':             post.encode('ascii', 'ignore'),
                'host':             host.encode('ascii', 'ignore'),
                'place_from':       place_from.encode('ascii', 'ignore'),
                'place_to':         place_to.encode('ascii', 'ignore'),
                'academic_level':   academic_level.encode('ascii', 'ignore'),
                'post_date':        post_date.encode('ascii', 'ignore'),

            }