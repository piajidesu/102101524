import handle_response
import handle_danmu
import 可视化
import time
import get_response

kw = input("输入要搜索的关键词:")
sum = input("输入需要爬取视频的数量:")
sum = int(sum)
kt = time.time()
page = {}
cids = {}



#搜索界面格式f"https://search.bilibili.com/all?keyword={kw}&page={page}"
url_1 = f"https://search.bilibili.com/all?keyword={kw}&page="#b站搜索界面网址格式
for i in range(0,int(sum)//42+1,1):
    page[i] = i + 1
responses_1 = {}

responses_1 = get_response.run(page,len(page),url_1)
#print(responses_1[1])
f = open("bv号.txt", "w", encoding="utf-8")#存放bv号的文件
for i in range(0,len(responses_1),1):
    #print(responses_1[1])
    handle_response.get_bv(responses_1[i],f)
f.close()
print("bv号获取完毕")##########################################bv号获取完毕

url_2 = f"https://api.bilibili.com/x/web-interface/view/detail?bvid="
f = open("bv号.txt","r",encoding="utf-8")#打开存放bv号的文件
bvs = list(f)#将文件转换为列表
responses_2 = {}
responses_2 = get_response.run(bvs,sum,url_2)
#print(len(responses_2))
#print(responses_2[0])
for i in range(0,len(responses_2),1):
    #print(responses_1[1])
    cid = handle_response.get_cid(responses_2[i])
    cids[i] = cid
print(cids)
f.close()
print("cid获取完毕")#cid获取完成

url_3 = f"https://api.bilibili.com/x/v1/dm/list.so?oid="
f = open("弹幕.txt","w",encoding="utf-8")
responses_3 = {}
responses_3 = get_response.run(cids,sum,url_3)
for i in range(0,len(responses_3),1):
    dms = handle_response.get_danmu(responses_3[i])
    for dm in dms:
        f.write(dm+"\n")
#print(len(responses_3))
#print(responses_3[299])
f.close()
print("获取弹幕完毕")#获取弹幕结束


handle_danmu.handle_danmu(kw)
可视化.show(kw)



lt = time.time()
print(lt-kt)