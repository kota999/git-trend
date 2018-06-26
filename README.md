# git-trend
Crawl & Scraping scripts for Github - Trending

## Installation

    pip install -r requirements.txt

## Usage

    scrapy crawl github_trend_crawler -o <output_jl_path> [-a timescale=<keyword>]
    # timescale default: all
    #    keyword:
    #            all: crawl for daily and weekly, monthly trending
    #            daily: crawl for daily trending
    #            weekly: crawl for weekly trending
    #            monthly: crawl for monthly trending
    #            ! optional !
    #               keyword combination is ","
    #               ex) timescale=daily,weekly: crawl for daily and weekly trending

## Crawl Language
 + All Language
 + UnKnown Language
 + C
 + C#
 + C++
 + CUDA
 + DockerFile
 + Dart
 + Elixir
 + Erlang
 + Go
 + GraphQL
 + Haskell
 + Java
 + Javascript
 + Julia
 + Jupyter-notebook
 + llvm
 + markdown
 + numpy
 + Objective-C
 + Objective-C++
 + PHP
 + PowerShell
 + Python
 + R
 + Ruby
 + Rust
 + Scala
 + Shell
 + Swift
 + Vim Script

### Configure
Replace [GITHUB_TREND_LANGS](github_rookie/settings.py)
