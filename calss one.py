# import  requests
# # from lxml import  html
# # url = 'https://b.faloo.com/y_0_1.html'   # 路径
# # import  os
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# # }    # 请求头
# # info = requests.get(url, headers)
# # all = info.text
# # # 建立文档树对象
# # ht = html.etree.HTML(all)
# # if not os.path.exists('./picture'):
# #     os.mkdir('./picture')
# # #  拿到所有的标题
# # infomation = ht.xpath('//div[@class="centerTwo bodyBorderShadow"]/div[@id="BookContent"]//div[@class="TwoBox02_02"]')
# # for item in infomation:
# #     title = item.xpath('.//div[@class="TwoBox02_03"]//a/@title')[0]
# #     img = item.xpath('.//div[@class="TwoBox02_03"]//img/@src')[0]
# #     pic = requests.get(img)
# #     if pic.status_code == 200:  # 去请求每一个图片通过响应状态码看是否可以访问到 如果可以就可以下载图片
# #         with open('./picture/' + str(title) + '.jpg', 'wb')as p:
# #             p.write(pic.content)  # 使用字节




import requests
from lxml import html
url = 'https://b.faloo.com/y_0_1.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
# print(res.text)
page = html.etree.HTML(res.text)
book_li = page.xpath('//div[@class="TwoBox02_01"]/div')
for book in book_li:
    img_link = book.xpath('.//a/img[@class="TYImg"]/@src')[0]   # 从列表里取出来
    name = book.xpath('.//h1/@title')[0]
    print(img_link, name)
    # 获取图片信息
   # img = requests.get(img_link, headers=headers)
    # 将图片写到本地（对于图片和视频---【用二进制的形式写入】）
    # with open(f'imgs/{name}.jpg', 'ab') as f:
    #     f.write(img.content)   #写入图片的方式
    #     pass

# import requests
# from lxml import html
# url = ''
# headers = {
#     ''
# }
# res = requests.get(url,headers=headers)
# print(res.text)
# page = html.etree.HTML(res.text)
# all = page.xpath('//div[@class="TwoBox02_01"]/div')
# for x in all:
#     link = x.xpath('.//a/img[@class="TYImg"]/@src')
#     name = x.xpath('.//h1/@title')
#     print(link,name)
#     img = requests.get(link,headers=headers)
#     with open(f'imgs/{name}.jpg','ab')as f:
#         f.write(img.content)
#         pass