FROM pritunl/archlinux
MAINTAINER kota999 <kota99949@gmail.com>
#FROM serverless-crawler

#
# set HOME
#
ENV HOME=/root

#
# install requirement library
#
RUN echo Y | pacman -S git wget zeromq gcc make tk mesa-libgl texlive-bin readline

#
# install pyenv
#
RUN git clone https://github.com/yyuu/pyenv.git ${HOME}/.pyenv
# export PYENV PATH
ENV PATH ${HOME}/.pyenv/bin:${HOME}/.pyenv/shims:$PATH
RUN echo "export PATH=\$PATH:\$HOME/.pyenv/bin:\$HOME/.pyenv/shims" >> ${HOME}/.bashrc
# set eval and source bash
RUN echo "eval \"\$(pyenv init -)\"" >> ${HOME}/.bashrc && source ${HOME}/.bashrc

#
# install anaconda3-4.4.0
#
RUN pyenv install anaconda3-4.4.0
RUN pyenv rehash
# set using python-distribution
RUN pyenv global anaconda3-4.4.0
# confirm using python version
RUN pyenv version
# conda update
RUN echo y | conda update conda
# pip upgrade
RUN echo y | pip install --upgrade pip

#
# install requirements for scrapig
#
RUN echo y | conda install beautifulsoup4 scrapy sqlalchemy psycopg2
RUN echo y | pip install dataset

#
# install scrapig scripts
#
RUN git clone https://github.com/kota999/git-trend.git ${HOME}/git-trend
RUN git clone https://github.com/kota999/pgpipelines.git ${HOME}/pgpipelines
RUN cd ${HOME}/pgpipelines && python setup.py install
COPY settings.py ${HOME}/git-trend/github_rookie/settings.py
ADD scrape /usr/local/sbin/

#
# clean trash
#
RUN rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/local/* /var/lib/pacman/sync/* ${HOME}/.cache/pip/*

CMD ["/usr/local/sbin/scrape"]
