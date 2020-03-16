import requests

# get 请求
url="http://www.baidu.com"
header = {"User-Agent": "Mozilla/5.0"}  #请求头伪装成浏览器，否则为python发送
res = requests.get(url,headers=header)

# print(res)
print(res.cookies)
print(res.headers)
# print(res.status_code)
# print(res.text) # 文本或json格式的而返回值均可使用
# print(res.json())  #仅返回值为Json格式的返回值才能使用，否则会报错
print(res.request.headers)


# post 请求
# url="http://www.baidu.com"
# res = requests.post(url)
# print(res)
# print(res.cookies)
# print(res.headers)
# print(res.status_code)
# print(res.text)

