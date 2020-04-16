# -*- coding: UTF-8 -*-
##########################################################################
# SCRIPT_NAME     : FindStation.py
# CREATE_TIME     : 2019/09/09
# DESCRIBETION    : make station's message find get easy
# PARAMETER       : need input station
##########################################################################

import os as os
import codecs
import time
import re
from tkinter import *
import subprocess
import threading


# 读取站名，类型强转
# station = input("请输入站码、站名或拼音: ")

def btn_click():
    # 建立字典映射
    # 站码
    dict_num = {
        '111': ['地球站', '11.11.11.11', '奥特曼', '123456789', '银河处', 'NO'],
        '222': ['火星站', '22.22.22.22', '钢铁侠', '987654321', '银河处', 'YES']
    }

    # 站中文名称
    dict_str = {
        '地球站': ['111', '11.11.11.11', '奥特曼', '123456789', '银河处', 'NO'],
        '火星站': ['222', '22.22.22.22', '钢铁侠', '987654321', '银河处', 'YES']
    }

    # 站码拼音
    dict_word = {
        'diqiu': ['111', '地球站', '11.11.11.11', '奥特曼', '123456789', '银河处', 'NO'],
        'huoxing': ['222', '火星站', '22.22.22.22', '钢铁侠', '987654321', '银河处', 'YES']
    }
    # 对错误站名做异常处理
    try:
        # 判断是站码、名称还是拼音
        # 使局部变量高可用
        global station
        station = ipText.get()
        # 正则表达式，匹配带数字的
        pattern1 = re.compile('[0-9]+')
        match_num = pattern1.findall(station)
        pattern2 = re.compile('[a-z]+')
        match_word = pattern2.findall(station)
        # 站码
        if match_num:
            num1 = station
            servername = dict_num[num1][0]
            dbip = dict_num[num1][1]
            linkman = dict_num[num1][2]
            linkphone = dict_num[num1][3]
            location1 = dict_num[num1][4]
            bool1 = dict_num[num1][5]
            # 拼音
        elif match_word:
            num1 = dict_word[station][1]
            servername = dict_word[station][0]
            dbip = dict_word[station][2]
            linkman = dict_word[station][3]
            linkphone = dict_word[station][4]
            location1 = dict_word[station][5]
            bool1 = dict_word[station][6]
        # 中文名称
        else:
            num1 = dict_str[station][0]
            servername = station
            dbip = dict_str[station][1]
            linkman = dict_str[station][2]
            linkphone = dict_str[station][3]
            location1 = dict_str[station][4]
            bool1 = dict_str[station][5]

        ip11 = "银河处仙女处"
        ip22 = "大熊处"
        tips = "该站位于11和22服务器，传输标志位flag2=1"
        # 判断IP归属哪个服务器
        if location1 in ip11:
            tips = "该站位于11服务器，传输标志位flag1=1"
        elif location1 in ip22:
            tips = "该站位于22服务器，传输标志位flag3=1"
        else:
            tips = tips
        # tk的语句插入
        text.insert(INSERT, ("路站码：%s\n路站名：%s\n服务器：%s\n联系人：%s\n手机号：%s\n归属地：%s\n主副站：%s\n其他信息：%s\n\n" %
                             (num1, servername, dbip, linkman, linkphone, location1, bool1, tips)))
    except KeyError:
        print ("Error:未找到该站，请查证")
        text.insert(INSERT, ("未找到该站，请确认！\n"))

    # 实现对网络的ping测试
    v = dbip
    thread_id = []
    j = 1
    # 如果未ping通，重试多少次，这里也可以用字符串组合来ping网段
    for i in range(1):
        loop = v
        thread_id.append(0)
        # Ping类里有两个参数str_ip,sleep_time
        thread_id[i] = Ping(loop, int(j / 20))
        # 开始调用
        thread_id[i].start()
        i = i + 1
        j = j + 10


# enter调用
def btn_click_enter(self):
    btn_click()


# 清空消息
def cleartext():
    text.delete('0.0', END)


class Ping(threading.Thread):
    def __init__(self, str_ip, sleep_time):
        threading.Thread.__init__(self)
        self.str_ip = str_ip
        self.sleep_time = sleep_time

    def run(self):
        time.sleep(self.sleep_time)
        ftp_ret = subprocess.Popen('ping %s -n 3' % self.str_ip, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   shell=True)
        ret = ftp_ret.stdout.read()
        # 这里的字符集一定是gbk,否则会报错
        str_ret = ret.decode("gbk")
        ret_s = re.search("TTL", str_ret)
        if ret_s:
            text.insert(INSERT, ("%s    在线!\n#########################\n" % self.str_ip))
        else:
            text.insert(INSERT, ("%s    无法ping通!\n#########################\n" % self.str_ip))


# 创建窗口对象的背景色
root = Tk()
root.title('便捷式一键查询服务系统')
root.geometry('360x520')

# Frame为布局函数
main_frame = Frame(root)
text_frame = Frame(main_frame)
station_frame = Frame(main_frame)
botton_frame = Frame(station_frame)
# 建立列表
l1 = Label(station_frame, text='输入站名、站码或拼音')
# l2 = Label(station_frame,text='')
ipText = Entry(station_frame)
# 字体显示
# ft = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
# pack是加载到窗口
l1.pack(side='left')
ipText.pack(side='left')
ipText['width'] = 10
# l2.pack(side='left')

'''
两个函数的意义是既能enter运行，又可以点击运行，方便操作，扩大使用
bind绑定enter键
注意里面是return 而不是enter
'''
b = Button(station_frame, text='开始', command=btn_click)
b['width'] = 4
b['height'] = 1
b.pack(side='left')
ipText.bind("<Return>", btn_click_enter)

# 消息输入界面
text = Text(text_frame, width=36, height=25)
text.pack()
main_frame.pack()
c = Button(text='清空', command=cleartext)
c['width'] = 4
c['height'] = 1
c.pack(side='top')

# 输入框的位置
station_frame.pack(side='top', pady='10')
text_frame.pack()

# 进入消息循环
root.mainloop()