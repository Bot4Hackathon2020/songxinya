#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/11/28 15:01 
# @Author : Payiz 
# @File : demo.py
# @project: 项目名称
# pip --default-timeout=100 install -i https://pypi.tuna.tsinghua.edu.cn/simple XXX
# -----------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/7 16:57
# @Author : Payiz
# @File : ds_2.py
# @project: 项目名称
#
# -----------------------------------


import os
import re
import pandas as pd
import stylecloud
from IPython.display import Image, display
from PIL import Image


if __name__ == '__main__':
    style = 'fas fa-'+'heart'
    in_file = './词频源数据.txt'
    out_file = './词频统计结果2.png'

    stylecloud.gen_stylecloud(file_path = in_file, collocations=False,
                              font_path=r'‪C:\Windows\Fonts\msyh.ttc',
                              output_name=out_file,
                              icon_name=style,
                              background_color='black',
                              size = 2000,
                              max_font_size=200,
                              max_words=6000
                              )
    print('词云完成')
    # display(Image(filename='./图片.png')) # 这个是jupyter里才有效

    im = Image.open(out_file)
    im.show()
    # print(im)  # like this: <PIL.PngImagePlugin.PngImageFile image mode=RGB size=1000x1000 at 0x27EC3BA20D0>
