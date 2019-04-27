# -*- coding: utf-8 -*-
import scrapy
import re
from soufang.items import NewHouseItem, EsfHouseItem, ZuHouseItem


class SoufangspiderSpider(scrapy.Spider):
    name = 'soufangSpider'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']


    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield scrapy.Request(i, meta={
    #             'dont_redirect': True,
    #             'handle_httpstatus_list': [302]
    #         }, callback=self.parse)


    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            # 获取省份信息
            tds = tr.xpath(".//td[not(@class)]")
            provinceTd = tds[0]
            provinceText = provinceTd.xpath(".//text()").get()
            provinceText = re.sub(r"\s", "", provinceText)
            if provinceText:
                province = provinceText
            if province == "其它":
                # 不爬取海外的房源
                continue

            # 获取城市信息
            cityTd = tds[1]
            cityLinks = cityTd.xpath(".//a")
            for cityLink in cityLinks:
                city = cityLink.xpath(".//text()").get()
                cityUrl = cityLink.xpath(".//@href").get()
                # 构建城市房子信息url
                urlModule = cityUrl.split(".", 1)
                scheme = urlModule[0]
                domain = urlModule[1]
                if "/bj" not in scheme:
                    # 构建新房的url
                    newHouseUrl = scheme + ".newhouse." + domain + "house/s/"
                    # 构建二手房的url
                    esfHouseUrl = scheme + ".esf." + domain
                    # 构建租房的url
                    zuHouseUrl = scheme + ".zu." + domain
                else:
                    # 北京需要单独处理
                    # 默认二手房和租房会重定向到电脑IP所在地的页面，所以用优质房源来防止重定向
                    newHouseUrl = "https://newhouse.fang.com/house/s/"
                    esfHouseUrl = "https://esf.fang.com/integrate/"
                    zuHouseUrl = "https://zu.fang.com/integrate/"

                # 传递给下一个函数进行解析
                yield scrapy.Request(url=newHouseUrl, callback=self.parseNewHouse, meta={"info":(province, city)})
                yield scrapy.Request(url=esfHouseUrl, callback=self.parseEsfHouse, meta={"info":(province, city)})
                yield scrapy.Request(url=zuHouseUrl, callback=self.parseZuHouse, meta={"info":(province, city)})

                # break
            # break


    def parseNewHouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            # 获取小区名字
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            if name:
                name = name.strip()
            # 获取几居室
            houseTypeList = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            houseTypeList = list(map(lambda x:re.sub(r"\s", "", x), houseTypeList))
            rooms = list(filter(lambda x:x.endswith("居"), houseTypeList))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            # 获取面积
            area = re.sub(r"\s|/|－", "", area)
            # 获取地址
            address = li.xpath(".//div[@class='address']/a/@title").get()
            # 获取行政区
            districtText = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            if districtText:
                district = re.search(r".*\[(.+)\].*", districtText).group(1)
            # 是否在售
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            # 获取价格
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            # 获取详情页
            originUrl = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            if originUrl:
                originUrl = response.urljoin(originUrl)

            # 返回数据
            item = NewHouseItem(type="new",province=province, city=city, name=name, price=price, rooms=rooms, area=area, \
            address=address, district=district, sale=sale, originUrl=originUrl)
            yield item
            # break

        # 获取下一页的链接
        nextUrl = lis.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if nextUrl:
            yield scrapy.Request(url=response.urljoin(nextUrl), callback=self.parseNewHouse, meta={"info":(province, city)})


    def parseEsfHouse(self, response):
        province, city = response.meta.get("info")
        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for dl in dls:
            item = EsfHouseItem()
            item['type'] = "esf"
            item['province'] = province
            item['city'] = city
            item['name'] = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            infos = dl.xpath(".//p[contains(@class,'tel_shop')]/text()").getall()
            infos = list(map(lambda x:re.sub(r"\s", "", x), infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif "㎡" in info:
                    item['area'] = info
                elif "层" in info:
                    item['floor'] = info
                elif "向" in info:
                    item['toward'] = info
                elif "年" in info:
                    item['year'] = info
                else:
                    continue
            item['address'] = dl.xpath(".//p[@class='add_shop']//span/text()").get()
            price = dl.xpath(".//dd/span/b/text()").get()
            if price:
                item['price'] = price + "万"
            item['unit'] = dl.xpath(".//dd/span[2]/text()").get()
            originUrl = dl.xpath(".//a/@href").get()
            item['originUrl'] = response.urljoin(originUrl)

            yield item
            # break

        nextUrl = dls.xpath("//div[@class='page_al']//p[1]/a/@href").get()
        if nextUrl:
            yield scrapy.Request(url=response.urljoin(nextUrl), callback=self.parseEsfHouse, meta={"info":(province, city)})



    def parseZuHouse(self, response):
        province, city = response.meta.get("info")
        dls = response.xpath("//div[contains(@class,'houseList')]//dl")
        for dl in dls:
            item = ZuHouseItem()
            item['type'] = "zu"
            item['province'] = province
            item['city'] = city
            item['name'] = dl.xpath(".//dd//p//a[3]/span/text()").get()
            item['district'] = dl.xpath(".//dd//p//a[1]/span/text()").get()
            item['address'] = dl.xpath(".//dd//p//a[2]/span/text()").get()
            infos = dl.xpath(".//dd//p[contains(@class,'font15 mt12')]/text()").getall()
            infos = list(map(lambda x:re.sub(r"\s|\[|\]", "", x), infos))
            for info in infos:
                if "整租" in info or "次卧" in info or "主卧" in info:
                    item['rentType'] = info
                elif "室" and "厅" in info or "户" in info:
                    item['rooms'] = info
                elif "㎡" in info:
                    item['area'] = info
                elif "朝" in info:
                    item['toward'] = info
                else:
                    continue
            traffic = dl.xpath(".//div/p[@class='mt12']/span/text()").getall()
            item['traffic'] = "".join(traffic)
            price = dl.xpath(".//div/p[contains(@class,'mt5')]//text()").getall()
            item['price'] = "".join(price)
            originUrl = dl.xpath(".//dd/p/a/@href").get()
            item['originUrl'] = response.urljoin(originUrl)

            yield item
            # break

        path = dls.xpath("//div[@class='fanye']")
        page = dls.xpath("//div[@class='fanye']//a[@class='pageNow']/text()").get()
        if page == "1":
            nextUrl = path.xpath(".//a[7]/@href").get()
        nextUrl = path.xpath(".//a[8]/@href").get()
        yield scrapy.Request(url=response.urljoin(nextUrl), callback=self.parseZuHouse, meta={"info":(province, city)})

