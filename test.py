# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api
import requests

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了

'''
top.setDefaultAppInfo("key", "id")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)

使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")

使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()

'''
a = top.api.TbkItemInfoGetRequest()

'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("appkey","*******"))
'''

a.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
a.num_iids = "542111433099,539423628872,542009245992,542020874449,539425259010,540957233003,539423337850,541806056531,537530163318"


def save_live_good_urls(live_id, good_list):
    url = 'http://127.0.0.1:8000/taobao/live/goods'
    # url = 'http://tao.meione.cc/taobao/live/goods'
    payload = {"live_id": live_id, "goods": good_list}
    print "Post to {} with payload {}".format(url, payload)
    success = False
    try:
        r = requests.post(url, json=payload, timeout=3)
        if r.status_code == requests.codes.ok:
            success = True
    except (requests.RequestException, requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError,
            requests.Timeout) as e:
        print "Error post to {} with payload {}".format(url, payload)

    if success:
        print r.text
        return r.json()
    else:
        data = []
        return data


try:
    f = a.getResponse()
    tbk_items = f['tbk_item_info_get_response']['results']['n_tbk_item']
    save_live_good_urls(34, tbk_items)
    print(f)


except Exception, e:
    print(e)
