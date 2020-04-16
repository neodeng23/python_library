#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''argparse介绍
是python的一个命令行解析包，用于编写可读性非常好的程序'''

#base
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

#定义一个指令
parser.add_argument("echo")

'''
一种是通过一个-来指定的短参数，如-h；
一种是通过--来指定的长参数，如--help'''
parser.add_argument("-v", "--verbosity", help="increase output verbosity")

#eg:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
        print "verbosity turned on"

#设定不需要参数值
action="store_true"
parser.add_argument('x', type=int, action="store_true",help="the base")

#设定参数类型 type
parser.add_argument('x', type=int, help="the base")

#设定可选值 choice=[]
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],help="increase output verbosity")

#设定自定义帮助信息help
parser.add_argument("square", type=int, help="display a square of a given number")

#设定程序用法
argparse.ArgumentParser(description="calculate X to the power of Y")

'''定义互斥函数'''
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
#-v -q将不可以同时出现

