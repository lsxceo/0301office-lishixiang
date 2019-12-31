#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# deco_http_server.py


class MyApp:
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func
        return func_wrapper

    def call_method(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            func = self.func_map.get('')
        return func()


app = MyApp()


@app.register('')
def error_page_func():
    print('没有资源!')
    response = f"""HTTP/1.1 200 OK

    <H1>404</h1>
    """.encode()
    return response


@app.register('/')
def main_page_func():
    response = f"""HTTP/1.1 200 OK

    <H1>Hello</h1>
    """.encode()
    return response


@app.register('/json')
def json_page_func():
    response = """HTTP/1.1 200 OK

    {"name": "de8ug", "age": 30, "address": "北京"}
    """.encode('gbk')
    return response


@app.register('/picture/1.jpg')
def pic_page_func():
    response = """HTTP/1.1 200 OK

    <a href="/search/detail?ct=503316480&amp;z=undefined&amp;tn=baiduimagedetail&amp;ipn=d&amp;word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&amp;step_word=&amp;ie=utf-8&amp;in=&amp;cl=2&amp;lm=-1&amp;st=undefined&amp;hd=undefined&amp;latest=undefined&amp;copyright=undefined&amp;cs=3353415934,3140282825&amp;os=2662810498,2084218444&amp;simid=0,0&amp;pn=6&amp;rn=1&amp;di=209660&amp;ln=1673&amp;fr=&amp;fmq=1577768744745_R&amp;fm=&amp;ic=undefined&amp;s=undefined&amp;se=&amp;sme=&amp;tab=0&amp;width=undefined&amp;height=undefined&amp;face=undefined&amp;is=0,0&amp;istype=0&amp;ist=&amp;jit=&amp;bdtype=0&amp;spn=0&amp;pi=0&amp;gsm=0&amp;objurl=http%3A%2F%2Fn.sinaimg.cn%2Ftranslate%2Fw1920h1080%2F20171204%2F2r-j-fypikwt7224917.jpg&amp;rpstart=0&amp;rpnum=0&amp;adpicid=0&amp;force=undefined" target="_blank" style="display: block; width: 345px; height: 194px; margin-top: 0.157623px;" name="pn6" class="div_3353415934,3140282825"><img class="main_img img-hover" data-imgurl="http://img5.imgtn.bdimg.com/it/u=3353415934,3140282825&amp;fm=26&amp;gp=0.jpg" src="http://img5.imgtn.bdimg.com/it/u=3353415934,3140282825&amp;fm=26&amp;gp=0.jpg" style="background-color: rgb(195, 177, 157); width: 345px; height: 194px;"></a>
    """.encode('gbk')
    return response
