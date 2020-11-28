#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/10 5:28 
# @Author : Payiz 
# @File : 原exel转换为csv.py
# @project: 项目名称
# 
# -----------------------------------


import pandas as pd


def transform_format(file_name):

    # 将exel格式的评论原数据进行以下操作
    file_name2 =file_name + '.xlsx'
    # 1. 读取
    data = pd.read_excel(file_name2, header=0)
    # data = data.drop('评论时间', axis=1)
    # data = data.drop('评论人', axis=1)
    # data = data.drop('标题', axis=1)

    star = []
    coment = []
    for index, rows in data.iterrows():
        # print(index, ':', rows['内容'])
        # 2. 星级转换：将星级转换为0,1二元指标，即好评、差评
        s = 1 if int(rows['星级'])>3 else 0
        star.append(s)
        # 3. 处理内容中的分隔符号
        ss = str(rows['内容']).replace('\n', '|').replace('\r', '|').replace(',', ';').replace('，', ';')
        coment.append(ss)

    # 4. 写入csv文件
    data_f = pd.DataFrame({
        '情感倾向': star,
        '评论': coment
    })
    out_file = file_name+'.csv'
    data_f.to_csv(out_file, sep=',', header=True, index=False,encoding='utf-8-sig')
    print('数据准备阶段：原exel数据成功处理并写入csv中，恭喜！', ' -----  新文件名：', out_file)


if __name__ == '__main__':
    name = '../原始数据/' + '作业帮' # app名称
    transform_format(name)
