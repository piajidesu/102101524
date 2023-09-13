import pandas as pd
import jieba

import wordcloud
from matplotlib import pyplot as plt
def handle_danmu(kw):
    f = open("弹幕.txt","r",encoding="utf-8")
    danmus = list(f)
    #print(a)
    danmus_new = [danmu for danmu in danmus]#将文件转为列表

    unless_fuhao = ["\n"," ","，",",",".","。","!","！","?","？",'哈']
    for fuhao in unless_fuhao:
        danmus_new = [danmu.replace(fuhao, '') for danmu in danmus_new]#删去一些无意义的字符
    unless_words = ['1','2','3','4','5',''," "]

    danmus_new = [danmu for danmu in danmus_new if danmu not in unless_words]#删去一些无意义的弹幕
    #danmus_new = [danmu for danmu in danmus_new if len(danmu)>1]#删掉单字弹幕


    #print(len(danmus_new))
    f.close()

    cipin1 = pd.DataFrame({'弹幕':danmus_new})#整理弹幕
    cipin1['弹幕'].value_counts().to_excel("biao1.xlsx")#保存为excel
############################################################################
    #danmustr= ''.join(i for i in danmus_new)

    #words = list(jieba.cut(danmustr))

    #print(words)

    #fnl_words = [i for i in words if len(i)>1]

    #file = open("aaa.txt","w",encoding="utf-8")
    #for str in fnl_words:
        #file.write(str+'\n')

    #cipin2 = pd.DataFrame({'弹幕':fnl_words})
    #cipin2['弹幕'].value_counts().to_excel("biao2.xlsx")


if __name__=='__main__':#用于单独测试
    kw = "1"
    handle_danmu(kw)
