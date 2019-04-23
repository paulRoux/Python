from scrapy import cmdline

## 执行scrapy爬虫的命令
cmdline.execute('scrapy crawl doubanSpider'.split())

## 将数据进行磁盘保存
## 或者保存为 douban.csv(默认unicode)
# cmdline.execute('scrapy crawl doubanSpider -o douban.json'.split())