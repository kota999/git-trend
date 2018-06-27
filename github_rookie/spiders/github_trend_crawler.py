# -*- coding: utf-8 -*-
import scrapy
from github_rookie.items import GithubTrendItem
from github_rookie.settings import GITHUB_TRENDING_URL,  GITHUB_TRENDING_LANGS, GITHUB_TRENDING_TIME_SCALES

import re
import bs4


class GithubTrendCrawlerSpider(scrapy.Spider):
    name = 'github_trend_crawler'
    allowed_domains = ['github.com']
    TIME_SCALE_ALL = "all"
    TIME_SCALE_DAILY = "daily"
    TIME_SCALE_WEEKLY = "weekly"
    TIME_SCALE_MONTHLY = "monthly"

    def __init__(self, timescale="all"):
        timescales = []
        if self.TIME_SCALE_ALL in timescale:
            timescales = GITHUB_TRENDING_TIME_SCALES
        else:
            # TODO: check exactly
            if self.TIME_SCALE_DAILY in timescale:
                timescales.append(GITHUB_TRENDING_TIME_SCALES[0])
            if self.TIME_SCALE_WEEKLY in timescale:
                timescales.append(GITHUB_TRENDING_TIME_SCALES[1])
            if self.TIME_SCALE_MONTHLY in timescale:
                timescales.append(GITHUB_TRENDING_TIME_SCALES[2])
            if len(timescales) == 0:
                timescales = GITHUB_TRENDING_TIME_SCALES
        self.start_urls = [GITHUB_TRENDING_URL + lang + "?since=" + ts \
            for lang in GITHUB_TRENDING_LANGS for ts in timescales]
        super().__init__()

    def parse(self, response):
        ti = []
        url = response.url
        soup = bs4.BeautifulSoup(response.body.decode(), "html.parser")
        repos = soup.find("ol", {"class": "repo-list"})
        repos = [] if repos is None else repos.findAll("li")
        timescale = re.findall(GITHUB_TRENDING_URL + ".*?since=(.+)?", url)[0]
        for repo in repos:
            i = GithubTrendItem()
            i["name"] = re.sub(r'\A\/', "", repo.find("h3").a["href"])
            i["description"] = repo.find("div", {"class": "py-1"}).text.strip()
            lang_elm = repo.find("span", {"itemprop": "programmingLanguage"})
            i["lang"] = "Unknown language" if lang_elm is None else lang_elm.text.strip()
            all_stars_elm = repo.find("svg", {"aria-label": "star"})
            i["all_stars"] = 0 if all_stars_elm is None else int(all_stars_elm.findParent().text.strip().replace(",", ""))
            forks_elm = repo.findAll("svg",  {"aria-label": "fork"})
            i["forks"] = 0 if len(forks_elm) == 0 else int(forks_elm[0].findParent().text.strip().replace(",", ""))
            stars_elm = repo.find("span", {"class": "float-sm-right"})
            stars_elm = None if stars_elm is None else re.findall(r'(.+)? stars', stars_elm.text.strip())
            i["stars"] = 0 if stars_elm is None or len(stars_elm) == 0 else int(stars_elm[0].replace(",", ""))
            i["timescale"] = timescale
            ti.append(i)
        return ti

