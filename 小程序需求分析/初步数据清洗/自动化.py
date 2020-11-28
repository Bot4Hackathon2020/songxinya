#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/10 9:35 
# @Author : Payiz 
# @File : 自动化.py
# @project: 项目名称
# 
# -----------------------------------
from 初步数据清洗.原exel转换为csv import transform_format
from 初步数据清洗.字数太少完全重复 import clear_sp1
# from 初步数据清洗.深度清洗 import clear_sp2

all_apps = ['华为Gorkor', '华为给未来写封信', '华为邮政EMS']

print('批量处理多个APP数据：')

for i in all_apps:
    name = '../原始数据/' + i + '/' + i
    print('当前应用：', name)
    transform_format(name)
    clear_sp1(name)
    # clear_sp2(name)
