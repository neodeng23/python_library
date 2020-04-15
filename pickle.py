# -*- coding: utf-8 -*-
"""pickle模块用法"""
import pickle

'''在机器学习中，我们常常需要把训练好的模型存储起来，这样在进行决策时直接将模型读出，而不需要重新训练模型，这样就大大节约了时间。
Python提供的pickle模块就很好地解决了这个问题，它可以序列化对象并保存到磁盘中，并在需要的时候读取出来，任何对象都可以执行序列化操作。'''

pickle.dump(obj, file, [,protocol])  #将obj对象序列化存入已经打开的file中。
# obj：想要序列化的obj对象。
# file:文件名称。
#protocol：序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。

pickle.load(file)  #将file中的对象序列化读出。
# file：文件名称。

pickle.dumps(obj[, protocol])  #将obj对象序列化为string形式，而不是存入文件中。
# obj：想要序列化的obj对象。
# protocal：如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。

pickle.loads(string)  #从string中读出序列化前的obj对象。
# string：文件名称

