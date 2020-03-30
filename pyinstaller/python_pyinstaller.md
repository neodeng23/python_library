####安装
pip install pyinstaller

####命令选项说明
pyinstaller --help

####命令
pyinstaller [options] script [script …] | specfile

####使用说明
制作Windows应用程序，可以在Windows中运行PyInstaller；

制作一个Linux应用程序，你可以在Linux等中运行它。

####使用步骤
最简单的情况下, 在命令行中切换到你的脚本myscript.py所在的目录后, 执行
pyinstaller myscript.py

pyinstaller会分析你的代码myscript.py并且:

1.在脚本所在目录下创建myscript.spec(高级用法)

2.在脚本所在目录下创建build文件夹, 并在其中写入日志文件和程序运行产生的文件

3.在脚本所在目录下创建dist文件夹, 并在其中写入生成的myscript的可执行文件(.exe)

###[option]
|选项|功能|实例|
|  ----  |  ----  | ----  |
|-h 或者 --help|显示帮助功能|pyinstaller -h myscript.py|
|- -distpath [路径]|生成的exe的目录(默认在dist文件夹)|pyinstaller --distpath Myexe|
|----|----|----|
|-D或者--onedir|此为默认选项, 创建一个单一bundle文件夹, 内含可执行文件|pyinstaller -D myscript.py|
|-F或者--onefile|创建一个单一文件, 即是可执行文件|pyinstaller -F myscript.py|
|- -specpath [路径]|保存spec文件的文件夹(默认与脚本在同一目录)|pyinstaller - -specpath MYSPEC|
|----|----|----|
|-p [路径]或者--paths[路径]|搜索 py 文件import的路径.允许设置多个路径, 以 : 分隔, 或者说重复使用这个命令.|一般情况不用设置, 只要你编译器中能成功import就没问题(环境变量中的路径是生效的)|
|- -key [密钥]|	用来加密python字节码的密钥|无特殊情况不用设置|
|----|----|----|
|-c 或者 --console 或者 --nowindowed|打开一个控制台窗口, 这是默认选项, 在windows系统中, 如果入口文件是 .pyw 文件, 此选项无效.|默认的, 不用写|
|-w或者–windowed 或者 --noconsole|不显示控制台窗口(类似cmd的黑框框), 如果你写的是带UI的程序, 此选项基本必选.如果入口程序是pyw文件, 此选项默认生效.|pyinstaller -w myscript.py|
