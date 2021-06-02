import requests
import time
import json
import csv
import re


def getData(url, pageNum):
    """获取源码"""
    # 获取时间戳
    t_param = time.time()
    t_list = str(t_param).split(".")
    headers = {
        "Cookie": "cna=vGFCGCWEmRICAXVSh+1WAnn0; xlly_s=1; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb94182218; "
                  "enc=KxMW0uMeulDFkpFN1yKxM8cpBxP76sWFczLAg7jtfps%2BFQTzjIfJEHxIeBwZK2fNtRxiFtuIsx9dwAhUFE7nbw%3D%3D"
                  "; t=925af22c23d016218d77dd95a3ce7507; _tb_token_=386e67d13a886; "
                  "cookie2=133fa2d494ac47cdb15a916b33112f3d; _m_h5_tk=6ab1dca2334629f51511ead8382d6be9_1606281634489; "
                  "_m_h5_tk_enc=1d1a11555b05f5f072126a70683467e5; "
                  "tfstk=cNDGBdtRXfP1nBNnNdws2MjZqYDcZNAa5xkELv7ztiLoBxkFihCFaCs9xP3iHs1..; "
                  "l=eBO1NgRgOlOSpfxWBOfZourza77OSIRYiuPzaNbMiOCP9HCW5rvfWZ7QRuLXC3hVh6VkR37kyyKQBeYBqnV0x6aNa6Fy_Ckmn; isg=BJ-fqOVJPOs9YTj2uJ_-CYsRLvMpBPOmxxusUDHsO86dwL9COdSD9h2Wg1C-4Mse",
        "referer": "https://detail.tmall.com/item.htm?spm=a230r.1.14.29.5b614e76ffR7sP&id=630056407457&ns=1&abbucket"
                   "=20&sku_properties=10004:709990523;5919063:6536025",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.66 Safari/537.36 "
    }
    params = {
        "callback": str(int(t_list[1][3:]) + 1),
        "_ksTS": t_list[0] + t_list[1][:3] + "_" + t_list[1][3:],
        "currentPage": pageNum
    }
    # text[]表示去除res文本前面冗余的部分
    res = requests.get(url, params=params, headers=headers).text[len(str(int(t_list[1][3:]) + 1)) + 3:-1]
    # 字符串转化为字典
    res2 = json.loads(res)
    # 将字典转化为字符串
    res3 = json.dumps(res2, indent=4)
    # 以上两步是为了美化json的输出格式，方便获取内容，省略也可。
    result = json.loads(res3)
    reviews = []
    for i in range(20):
        result_content = result["rateDetail"]["rateList"][i]["rateContent"]
        reviews.append(result_content)
    return reviews


# 存储数据
def storeData(data):
    with open('D:/PycharmProjects/test1/reviews.csv', 'a', encoding='utf-8', newline='') as file:
        file_csv = csv.writer(file, dialect='excel')
        data_len = len(data)
        for length in range(data_len):
            review = data[length]
            file_csv.writerow([review])


# main函数
if __name__ == '__main__':
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId=630056407457&spuId=1868837056&sellerId=2616970884"
    for pageNum in range(5):
        data = getData(url, pageNum)
        storeData(data)

