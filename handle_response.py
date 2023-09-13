
from bs4 import BeautifulSoup
import re


def get_bv(response,f):####用于提取bv号的函数
    print("bv号获取函数正在运行")
    soup = BeautifulSoup(response, "html.parser")
    bv_last = "aaa"  #
    for link in soup.find_all('a'):
        bv = str(link.get('href'))  # 提取href
        if ("www" in bv and "BV" in bv and bv!=bv_last):  # 筛选含有“www”和“BV”的并去重
            print(link.get('href'))
            f.write(bv[25:37])  # 写入BV号
            f.write("\n")
            bv_last = bv  # 去重
            #print(f"count:{count}")



def get_cid(response):############获取cid号的函数
    a = response.find("cid")#查询第一个“cid”的位置
    cid = response[a:a+20]
    cid = re.findall(r'\d+',cid)#提取数字
    cid = cid[0]
    #print(cid)#
    return cid



def get_danmu(response):############获取弹幕的函数
    all_dms = []
    data = re.findall('<d p="(.*?)">(.*?)</d>', response)
    dms = [d[1] for d in data]
    all_dms += dms
    print(all_dms)
    print("ok")
    return all_dms



