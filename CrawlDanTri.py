import scrapy

class DanTriSpider(scrapy.Spider):
    name = 'DanTriSpider'
    start_urls = ['https://dantri.com.vn/xa-hoi/thu-tuong-xu-ly-sao-voi-o-dich-covid-19-o-do-thi-lon-nhu-ha-noi-tphcm-20200807115954397.htm']

    def parse(self, response):
         f = open('C:/Users/Admin/DSKT/tutorial/tutorial/Output/abc.txt','a+', encoding="utf8")

         title = response.css('h1.dt-news__title::text').get().strip()
         f.write(title + '           ')
         time = response.css("div.dt-news__header div.dt-news__meta span::text").extract_first()
         f.write(time + '           ')
         author = response.css("div.dt-news__content p strong::text").extract_first()
         f.write(author + '           ')
         tags = response.css("div.dt-news__tags ul li h4 a::text").extract()
         for i in tags:
             f.write(i + '  ')
         f.write('           ')
         url_str = response.url
         f.write(url_str)
         f.write('\n')


         next_links = self.get_next_links(response)
         if next_links is not None:
             for link in next_links:
                 link = 'https://dantri.com.vn' + link
                 yield scrapy.Request(link, callback=self.parse)

    def get_next_links(self, response):
        next_links = response.css('a[href^="/"]::attr(href)').extract()
        if len(next_links):
            return next_links
        else:
            return None



