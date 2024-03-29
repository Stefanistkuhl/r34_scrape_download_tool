from scrapy.spiders import  CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "r34scraper"
    allow_domains = ["rule34.xxx"]
    start_urls = ["https://rule34.xxx/index.php?page=post&s=list&tags=dark_souls+"] # you can replace this with any link if the site
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination"]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="image-list"]/span'), callback='parse_item'),
    ]
    # collecting data from the tags about the image
    def parse_item(self, response):
        yield{
            "charakter": response.xpath('//li[@class="tag-type-character tag"]/a/text()').getall(),
            "artist": response.xpath('//li[@class="tag-type-artist tag"]/a/text()').getall(),
            "rating": response.xpath('//div[@id="stats"]/ul//li/text()')[6].get(),
            "score": response.xpath('//div[@id="stats"]/ul//li/span/text()')[0].get(),
            "bild": response.xpath('//div[@class="link-list"]/ul//li/a[@style]/@href')[0].get(),
        }

#