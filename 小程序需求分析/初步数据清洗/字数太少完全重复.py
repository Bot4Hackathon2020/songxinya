#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/10 2:25 
# @Author : Payiz 
# @File : 字数太少完全重复.py
# @project: 项目名称
# 
# -----------------------------------

import pandas as pd
# from 短文本相似度 import baidu_Similarity
# from snownlp import SnowNLP


def clear_sp1(file_name):
    # 第一步数据清洗，主要工作为筛选字数过少、完全重复的数据
    file_name2=file_name+'.csv'
    data = pd.read_csv(file_name2, header=0)
    # print(data)
    #长度检查

    star = []
    coment = []
    star1 = []
    coment1 = []
    for index, rows in data.iterrows():
        s = str(rows['评论'])
        t = rows['情感倾向']
        if len(s) >= 7:
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
    out_file1 = file_name + '--字数过少.csv'
    data_f1.to_csv(out_file1, sep=',', header=True, index=False,encoding='utf-8-sig')

    # 完全重复项检查

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

        if len(coment2) == 0:
            coment2.append(s)
            star2.append(t)
        else:
            is_repit = 0
            for j in coment2:
                # 语义重复
                # how = baidu_Similarity(s, j)
                # if how > 0.7:
                if s == j:
                    is_repit = 1
                    break
            if is_repit == 0:
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
    # 筛除的：重复的
    data_f3 = pd.DataFrame({
        '情感倾向': star3,
        '评论': coment3
    })
    out_file2 = file_name + '--第一步清洗留下.csv'
    data_f2.to_csv(out_file2, sep=',', header=True, index=False,encoding='utf-8-sig')

    out_file3 = file_name+ '--完全重复.csv'
    data_f3.to_csv(out_file3, sep=',', header=True, index=False,encoding='utf-8-sig')
    print('初步清洗阶段：已完成，恭喜！')
    print('筛除：')
    print('字数过少：', len(coment1))
    print('重复：', len(coment3))


if __name__ == '__main__':
    name = '../原始数据/作业帮/作业帮'
    clear_sp1(name)
