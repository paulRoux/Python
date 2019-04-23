# -*- coding: utf-8 -*-

# Scrapy settings for imagesPipe project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'imagesPipe'

SPIDER_MODULES = ['imagesPipe.spiders']
NEWSPIDER_MODULE = 'imagesPipe.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'imagesPipe.middlewares.ImagespipeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'imagesPipe.middlewares.ImagespipeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'imagesPipe.pipelines.ImagesDownloadPipe': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default) 启用AutoThrottle扩展
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#说明：启用AutoThrottle扩展时，仍然受到DOWNLOAD_DELAY（下载延迟）和CONCURRENT_REQUESTS_PER_DOMAIN（对单个网站进行并发请求的最大值）以及CONCURRENT_REQUESTS_PER_IP（对单个IP进行并发请求的最大值）的约束
AUTOTHROTTLE_ENABLED = True
# The initial download delay 初始下载延迟(单位:秒)
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies 在高延迟情况下最大的下载延迟(单位秒)
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server 设置 Scrapy应该与远程网站并行发送的平均请求数, 目前是以1个并发请求数
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received: 启用AutoThrottle调试模式
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 存放路径
IMAGES_STORE = 'E:\\code\\Python\\vscode\\imagesPipe\\images'

# 生成缩略图
IMAGES_THUMBS = {
   'small': (50, 50),  # (宽， 高) 小分辨率
   'big': (270, 270),  # 大分辨率
}

# 图片失效期限，防止重复爬取
IMAGES_EXPIRES = 30