#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/10 7:20 
# @Author : Payiz 
# @File : 深度清洗.py
# @project: 项目名称
# 
# -----------------------------------


import pandas as pd
# from 短文本相似度 import baidu_Similarity
from snownlp import SnowNLP


def snow_nlp(text):
    what = SnowNLP(text)
    # print('原句：', text)
    # print('情感', what.sentiments)
    # print('分词', what.words)
    res = 1 if what.sentiments > 0.6 else 0
    return res


def clear_sp2(file_name):
    # 第二步数据清洗，主要工作为筛选包含限制词，情感异常的数据
    file_name2 = file_name + '.csv'
    data = pd.read_csv(file_name2, header=0)
    # print(data)
    # 限制词检查

    star = []
    coment = []
    star1 = []
    coment1 = []
    with open('./敏感词库.txt', 'r', encoding='utf-8')as f:
        mingan = list(f.readlines())
    for index, rows in data.iterrows():
        s = str(rows['评论'])
        t = rows['情感倾向']
        is_mingan = 0
        for i in mingan:
            if s.find(str(i)) != -1:
                is_mingan = 1
                break
        if is_mingan == 0:
            coment.append(s)
            star.append(t)
        else:
            coment1.append(s)
            star1.append(t)

    # 写入csv文件
    # 继续保留的
    data_f = pd.DataFrame({
        '情感倾向': star,
        '评论': coment
    })
    # 筛除的：字数少
    data_f1 = pd.DataFrame({
        '情感倾向': star1,
        '评论': coment1
    })
    out_file1 = file_name.replace('.xlsx', '') + '--限制词.csv'
    data_f1.to_csv(out_file1, sep=',', header=True, index=False,encoding='utf-8-sig')

    # 情感异常

    star2 = []
    coment2 = []
    star3 = []
    coment3 = []
    count = 0
    for index, rows in data_f.iterrows():
        s = str(rows['评论'])
        t = rows['情感倾向']
        count += 1
        # print('当前比较：', count, ' : 已保留', len(coment2))
        # 使用snowNLP计算情感极性，不过效果太差了，这里还可以用百度NLP API
        if snow_nlp(s) == t:
            coment2.append(s)
            star2.append(t)
        else:
            coment3.append(s)
            star3.append(t)

    # 写入csv文件
    # 继续保留的
    data_f2 = pd.DataFrame({
        '情感倾向': star2,
        '评论': coment2
    })
    # 筛除的：情感异常的
    data_f3 = pd.DataFrame({
        '情感倾向': star3,
        '评论': coment3
    })
    out_file2 = file_name.replace('.xlsx', '') + '--第二步清洗留下.csv'
    data_f2.to_csv(out_file2, sep=',', header=True, index=False,encoding='utf-8-sig')

    out_file3 = file_name.replace('.xlsx', '') + '--情感异常.csv'
    data_f3.to_csv(out_file3, sep=',', header=True, index=False,encoding='utf-8-sig')
    print('深度清洗阶段：已完成，恭喜！')
    print('筛除：')
    print('限制词：', len(coment1))
    print('情感异常：', len(coment3))
    print("\n-------------------------------------------\n")
    # 将通过深度清洗后的数据存到训练集
    # for index, rows in data_f.iterrows():
    #     with open('./训练集.txt', 'a+', encoding='utf-8') as f:
    #         s = str(rows['评论'])
    #         t = rows['情感倾向']
    #         ss = s + '\t' + str(t) + '\n'
    #         f.write(ss)

if __name__ == '__main__':
    name = '../原始数据/作业帮/作业帮--第一步清洗留下'
    clear_sp2(name)

# 长度筛选
# gg = []
# with open('./敏感词库.txt', 'r', encoding='utf-8')as f:
#     res = list(f.readlines())
#     print(res)
#
#     all = 0
#     count = 0
#     for i in res:
#         all += 1
#         if len(i) >= 8:
#             count += 1
#             gg.append(i)
#
# with open('./新的.txt', 'w+', encoding='utf-8')as f:
#     for g in gg:
#         f.write(g)
#
# print(count, '  /  ',  all)
