'''
Created by auto_sdk on 2016.07.25
'''
from top.api.base import RestApi


class TbkItemDetailGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.fields = None
        self.num_iids = None
        self.platform = None
        self.unid = None

    def getapiname(self):
        return 'taobao.tbk.item.detail.get'
