import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
import xlrd
import pandas as pd
import wordcloud
import cv2
from PIL import  Image
import numpy as np


def show(kw):
    file_path = r'./biao1.xlsx'
    df = pd.read_excel(file_path, sheet_name = "Sheet1")
    print(df)
    plt.figure(figsize=(19.8, 7.2))
    plt.title("弹幕统计")
    x=df['弹幕'][0:20]#弹幕前20
    y=df['count'][0:20]#前20弹幕数量
    plt.barh(x,y)
    plt.yticks(fontsize=7)
    plt.savefig(f'{kw}柱状图.png')
    #plt.show()

    f = open("弹幕.txt","r",encoding="utf-8")
    danmus = list(f)

    img = cv2.imread(r'mask.png',cv2.IMREAD_UNCHANGED)
    img = Image.open(r'mask.png')
    mask = np.array(img)


    wc = wordcloud.WordCloud(height=2500, width=2500 ,min_word_length=5, font_path='simsun.ttc',mask=mask,background_color="white",contour_width=2)

    wc.generate(''.join(danmus))
    # plt.imshow(wc)

    wc.to_file(fr'{kw}云图.png')


if __name__=='__main__':#用于单独测试
    kw="1"
    show(kw)