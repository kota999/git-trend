from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

def handler(event, context):
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl('github_trend_crawler', timescale='daily')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

if __name__ == "__main__":
    handler('', '')
