# git-trend
Crawl & Scraping scripts for Github - Trending, and insert postgres.

## Installation

    pip install -r requirements.txt
    git clone https://github.com/kota999/pgpipelines
    cd pgpipelines
    python setup.py install

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

## Dockernize

    cp ./github_rookie/settings.py dockernize/settings.py
    cd ./dockernize
    # if want to set crawling conf, edit ./dockernize/scrape
    # Docker Build
    docker build -t serverless-crawler .
    # Docker Run
    docker run -it serverless-crawler

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
 + Select [GITHUB_TREND_LANGS](github_rookie/settings.py)
 + Settings postgresql connection and schema, and INSERT-ON and OFF [PG_PIPELINE](github_rookie/settings.py)
