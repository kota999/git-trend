FROM pritunl/archlinux
#FROM serverless-crawler
MAINTAINER kota999 <kota99949@gmail.com>

#
# set HOME
#
ENV HOME=/root

#
# install requirement library
#
RUN echo Y | pacman -S git wget zeromq gcc make tk readline
#RUN echo Y | pacman -S git wget zeromq gcc make tk mesa-libgl texlive-bin readline

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
# install python 3.6.6
#
RUN pyenv install 3.6.6
RUN pyenv rehash
# set using python-distribution
RUN pyenv global 3.6.6
# confirm using python version
RUN pyenv version
# pip upgrade
RUN echo y | pip install --upgrade pip


# install requirements for scrapig
RUN echo y | pip install boto3 beautifulsoup4 scrapy

#
## clean trash
##
RUN rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/local/* /var/lib/pacman/sync/* ${HOME}/.cache/pip/*

