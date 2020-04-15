
pyenv
###在开发Python程序的时候，有时候可能需要在不同版本的Python上进行测试。pyenv就是这么一个管理多版本Python的工具

#安装
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

#更新
$ pyenv update

#要卸载pyenv的话更加简单，直接删除目录即可,别忘了把.bashrc中的对应部分一并删掉

#列出所有可安装的Python版本
pyenv install -l|--list

#安装某个Python
pyenv install <version>

#列出所有已安装的Python，当前使用的Python会用星号标出
pyenv versions

#通过写~/.pyenv/version文件的方式设置全局Python：
$ pyenv global 2.7.6

pipenv
#虚拟环境
$ pip install pipenv
$ pip install --upgrade pipenv

#安装依赖包
$ pipenv install xxx

#删除依赖包
$ pipenv uninstall xxx

#进入虚拟环境
pipenv shell
pipenv run xxx
