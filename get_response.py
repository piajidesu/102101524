#这个文件存的爬虫程序


import asyncio
import aiohttp
import time

kw = "日本核污染水排海"
ks=time.time()
count = -1#用于爬取网址的计数
page = 1#
i = 0#返回response的计数
#def get_danmu_by_cid(cid):

responses = {}#用于存放response

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69",
        'Cookie': "buvid3=B1D9D1CF-FB32-3EF4-6695-A231B0EA43AF05769infoc; b_nut=1679065105; _uuid=10A810D1091-10354-3F52-349E-CF103DD11104DC12986infoc; rpdid=|(J~|Ru|lR|u0J'uY~m|Ylu|m; buvid4=D27C2198-90BA-C3DF-8FB4-9CA3CBED168796798-022112215-nUpjx%2FRbFQPAdrCeo9P%2BDg%3D%3D; CURRENT_QUALITY=120; i-wanna-go-back=-1; b_ut=5; header_theme_version=CLOSE; CURRENT_BLACKGAP=0; CURRENT_PID=d0825820-cd59-11ed-8310-f15ae8fc317a; nostalgia_conf=-1; buvid_fp_plain=undefined; FEED_LIVE_VERSION=V8; hit-new-style-dyn=0; hit-dyn-v2=1; LIVE_BUVID=AUTO6816831109018644; CURRENT_FNVAL=4048; DedeUserID=13627139; DedeUserID__ckMd5=0646defbd3eeb7f1; SESSDATA=8b3e9df2%2C1709451003%2C61bab%2A912flFsCgoEaVldv93EnMABBeltck3a500USKGV0cVA0dGXk2Pz7zaGJDTnAv9y4C_LiFZlwAAJwA; bili_jct=033220ff51edbfb6e55bc3bb2db01529; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxNTkyNjYsImlhdCI6MTY5MzkwMDA2NiwicGx0IjotMX0.w-yJTA7NXksOgvMb9HQFGPOgMeM7S84Ug6ZrYDtV7dE; bili_ticket_expires=1694159266; fingerprint=661ce4850b8444d5f1f539c301a50148; buvid_fp=661ce4850b8444d5f1f539c301a50148; sid=7kuj0sno; home_feed_column=4; browser_resolution=1030-838; is-2022-channel=1; PVID=4; bp_video_offset_13627139=838072682123624533; bsource=search_bing; b_lsid=1B2F69B9_18A6897F9E6"
    }#配置请求头
params={
    'type': '1',
    'order_by': '1m',
    'size': '20',
    'page': '3',
    }


async def get(a,url,bv):#爬取部分
    #print(count)
    print(f"url:{url+bv}")#将固定部分和url拼成完整的网址
    async with a.get(url+bv,headers=headers,params=params) as res:#爬取网页
        return await res.text()#返回爬取内容
async def main(list,url,len):
    async with aiohttp.ClientSession() as s:
        global count
        count = count + 1#
        link = list[count]#遍历表中的关键字
        #print(count)
        link = str(link)
        link.replace("\n",'')
        res = await get(s,url,link)
        #print(res)
        global responses
        global i
        responses[i] = res#将返回文本存入列表
        i +=1
        #print(f"i:{i}")
def run(list,len,url):#按照列表和给定的url爬取多个网页
    #print(p)

    global i
    global count
    count = -1
    i = 0#重置计数
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    taks=[asyncio.ensure_future(main(list,url,len),loop=loop)    for _ in range(len)]#总共进行len轮
    loop.run_until_complete(asyncio.wait(taks))#上个taks结束时开始下一个
    global responses
    return responses

if __name__=='__main__':#用于单独测试
    url = 'https://api.bilibili.com/x/web-interface/view/detail?bvid='
    f_1 = open("bv号.txt","r",encoding="utf-8")
    bvs = list(f_1)
    print(bvs)
    re = run(bvs,len,url)
    print(len(re))
    #print(re[0])
    f_1.close()