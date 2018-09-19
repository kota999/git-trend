FROM basei
MAINTAINER kota999 <kota99949@gmail.com>

#
# set HOME
#
ENV HOME=/root

# ADD program
ADD git-trend-deploy $HOME/git-trend
# install dependency
RUN cd $HOME/git-trend/scrapy-dynamodb && python setup.py install

ADD scrape /usr/local/sbin/
RUN chmod a+x /usr/local/sbin/scrape
#
## clean trash
##
RUN rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/local/* /var/lib/pacman/sync/* ${HOME}/.cache/pip/*

CMD ["/usr/local/sbin/scrape"]
