# -*- coding: utf-8 -*-

# Scrapy settings for github_rookie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'github_rookie'

SPIDER_MODULES = ['github_rookie.spiders']
NEWSPIDER_MODULE = 'github_rookie.spiders'
LOG_LEVEL = 'INFO'  # to only display errors
LOG_FORMAT = '%(levelname)s: %(message)s'
# LOG_FILE = 'log.txt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'github_rookie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
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
#    'github_rookie.middlewares.GithubRookieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'github_rookie.middlewares.GithubRookieDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
# Setting for pgpipelines
#
# ITEM_PIPELINES = {
   # 'pgpipelines.PgPipeline': 300,
# }
# from dataset import types
# PG_PIPELINE = {
    # 'connection': 'postgresql://localhost:5432/postgres',
    # 'table_name': 'github_trend',
    # 'col': {
        # 'name': ('name', types.UnicodeText), 'category': ('category', types.UnicodeText), 'lang': ('lang', types.UnicodeText),
        # 'description': ('description', types.Unicode), 'all_stars': ('all_stars', types.Integer),
        # 'forks': ('forks', types.Integer), 'stars': ('stars', types.Integer),
        # 'timescale': ('timescale', types.Unicode)
    # },
    # 'bulksize': 1000
# }
# ITEM_PIPELINES = {
    # 'dynamodbPipelines.DynamoDBPipeline': 1,
# }

# AWS_ACCESS_KEY_ID = '<acc key id>'
# AWS_SECRET_ACCESS_KEY = '<secret acc key>'
# DYNAMODB_REGION_NAME = '<region>'
# DYNAMODB_TABLE_NAME = '<table name>'
# Optional!
# DYNAMODB_ENDPOINT_URL = 'http://localhost:8000/'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#
# Setting for git-trend
#
GITHUB_TRENDING_URL = "https://github.com/trending/"
GITHUB_TRENDING_LANGS = ["", "python", "unknown", "c", "c%23", "c++", "cuda", "dockerfile", "dart",
    "elixir", "erlang", "go", "graphql", "haskell", "java", "javascript", "julia",
    "jupyter-notebook", "llvm", "markdown", "numpy", "objective-c", "objective-c++",
    "powershell", "php", "r", "ruby", "rust", "scala", "shell", "swift", "vim-script"]
GITHUB_TRENDING_TIME_SCALES = ["daily", "weekly", "monthly"]
