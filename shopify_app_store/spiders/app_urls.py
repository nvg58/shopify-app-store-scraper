import scrapy

class AppUrlsSpider(scrapy.Spider):
    name = 'app_urls'
    start_urls = ['https://apps.shopify.com/categories/finding-products-sourcing-options-print-on-demand-pod/all']
    
    custom_settings = {
        'OUTPUT_FILE': 'app_urls.txt',  # Replace with your desired default filename
        'ITEM_PIPELINES': {
            'shopify_app_store.pipelines.TextFilePipeline': 300,
        }
    }
    

    def parse(self, response):
        for url in response.xpath('//*[@data-controller="app-card"]/@data-app-card-app-link-value'):
            app_url = url.get().split('?')[0]
            yield {'app_url': app_url}

        for next_page in response.xpath('//a[@rel="next"]'):
            yield response.follow(next_page, self.parse)