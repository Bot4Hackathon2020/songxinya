#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/10 8:48 
# @Author : Payiz 
# @File : ee.py
# @project: 项目名称
# 
# -----------------------------------

from snownlp import SnowNLP
import numpy as np

s = '用日益显著。移动应用程序（Application Program，简称APP）作为移动端设备的功能延伸，具备获取成本低、操作便捷易懂、交互界面舒适、功能强大全面等特征，极受人们追捧。移动应用商店（Mobile Application Store）是专门以移动应用及游戏等为产品，提供产品发布、展示、评价、交易等功能的商店类平台。2008年7月10日苹果公司率先推出的第一款移动应用商店——Apple App Store上线，人类进入“智能手机+应用程序”时代。经过十余年的发展，不仅成为全球规模最大、最安全、最挣钱的应用商店，也为广大APP开发者带来了巨大的收入。'
d = '功能延伸d'
# print(s.find(d))
ff = '良心社区;没什么好说的。|实在是众荒拾珍搬;也祝越办越好。'
a = SnowNLP(ff)
print(a.sentiments)
# b=a.sim(d)
# print(a.words)
# print(b)

#欧式距离
# npvec1, npvec2 = np.array(det_a), np.array(det_b)
# similirity=math.sqrt(((npvec1 - npvec2) ** 2).sum())
# print('similirity:',similirity)

# # 余弦相似度
# def cos_sim(vector_a, vector_b):
#     """
#     计算两个向量之间的余弦相似度
#     :param vector_a: 向量 a
#     :param vector_b: 向量 b
#     :return: sim
#     """
#     vector_a = np.mat(vector_a)
#     vector_b = np.mat(vector_b)
#     num = float(vector_a * vector_b.T)
#     denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
#     cos = num / denom
#     sim = 0.5 + 0.5 * cos
#     return sim
#
# # 余弦值的范围在[-1,1]之间，值越趋近于1，代表两个向量的方向越接近；
# # 越趋近于-1，他们的方向越相反；接近于0，表示两个向量近乎于正交。
# vector_a, vector_b = np.array(a.words), np.array(a.words)
# similirity2=cos_sim(vector_a, vector_b)
# print('similirity2:',similirity2)