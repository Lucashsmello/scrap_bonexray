from pathlib import Path
import scrapy
import re
from ..items import ImageItem


class BoneXraySpider(scrapy.Spider):
    name = "bonexray"

    def start_requests(self):
        urls = [
            "https://bonexray.com",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath('//table[@class="bone-table"]//tr')

        # Extract body region
        body_regions = table[1].xpath('./td/text()').getall()[1:]

        # Extract age
        ages_month = [int(a*12) for a in [0, 0.5]+list(range(1, 16))]
        for i, row in enumerate(table[2:]):
            agem = ages_month[i]
            cells = row.xpath('.//td')[1:]
            for j, c in enumerate(cells):
                images_url = c.xpath('.//a/@href').getall()
                body_reg = body_regions[j]
                for img_url in images_url:
                    img_url = img_url.replace('content/uploads/cervical-spine-xray-newborn.jpg',
                                              'https://bonexray.com/wp-content/uploads/cervical-spine-xray-newborn.jpg')
                    yield ImageItem(age_month=agem,
                                    body_region=body_reg,
                                    image_urls=[img_url],
                                    filename=img_url.split('/')[-1].strip()
                                    )
