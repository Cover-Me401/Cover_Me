BOT_NAME = 'basic_scrapy_spider'

SPIDER_MODULES = ['basic_scrapy_spider.spiders']
NEWSPIDER_MODULE = 'basic_scrapy_spider.spiders'

ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = '4dd59122-36b6-4103-9488-6cfb589aa285'

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}