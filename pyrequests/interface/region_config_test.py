#coding=utf-8
import unittest
import requests
import os, sys
import hashlib
import json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class ScanCountTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://bossdev.epoque.cn'
        self.maxDiff = None
        md5 = hashlib.md5()
        sign_str = '000000'
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        password = md5.hexdigest()
        self.session = requests.Session()
        payload = {'username': 'admin', 'password': password}
        url = self.base_url + '/auth/entry'
        self.login_success = self.session.post(url, data=payload)
        self.cookie = self.login_success.cookies

    def tearDown(self):
        print self.result

    def test_count_region(self):
        url = self.base_url + '/regions/region'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],[{u'code': u'100010', u'name': u'\u610f\u7934\u6d4b\u8bd5'}, {u'code': u'100009', u'name': u'\u4e91\u8d35'}, {u'code': u'100008', u'name': u'\u897f\u5357'}, {u'code': u'100007', u'name': u'\u897f\u5317'}, {u'code': u'100006', u'name': u'\u9c81\u8c6b'}, {u'code': u'100005', u'name': u'\u4e1c\u5317'}, {u'code': u'100004', u'name': u'\u534e\u4e1c'}, {u'code': u'100003', u'name': u'\u534e\u5317'}, {u'code': u'100002', u'name': u'\u534e\u4e2d'}, {u'code': u'100001', u'name': u'\u534e\u5357'}])

    def test_count_province(self):
        url = self.base_url + '/regions/province'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],[{u'code': u'910000', u'name': u'\u5e7f\u4e1c\u7701'}, {u'code': u'650000', u'name': u'\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a'}, {u'code': u'640000', u'name': u'\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a'}, {u'code': u'630000', u'name': u'\u9752\u6d77\u7701'}, {u'code': u'620000', u'name': u'\u7518\u8083\u7701'}, {u'code': u'610000', u'name': u'\u9655\u897f\u7701'}, {u'code': u'530000', u'name': u'\u4e91\u5357\u7701'}, {u'code': u'520000', u'name': u'\u8d35\u5dde\u7701'}, {u'code': u'510000', u'name': u'\u56db\u5ddd\u7701'}, {u'code': u'500000', u'name': u'\u91cd\u5e86\u5e02'}, {u'code': u'460000', u'name': u'\u6d77\u5357\u7701'}, {u'code': u'450000', u'name': u'\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a'}, {u'code': u'440000', u'name': u'\u5e7f\u4e1c\u7701'}, {u'code': u'430000', u'name': u'\u6e56\u5357\u7701'}, {u'code': u'420000', u'name': u'\u6e56\u5317\u7701'}, {u'code': u'410000', u'name': u'\u6cb3\u5357\u7701'}, {u'code': u'370000', u'name': u'\u5c71\u4e1c\u7701'}, {u'code': u'360000', u'name': u'\u6c5f\u897f\u7701'}, {u'code': u'350000', u'name': u'\u798f\u5efa\u7701'}, {u'code': u'340000', u'name': u'\u5b89\u5fbd\u7701'}, {u'code': u'330000', u'name': u'\u6d59\u6c5f\u7701'}, {u'code': u'320000', u'name': u'\u6c5f\u82cf\u7701'}, {u'code': u'310000', u'name': u'\u4e0a\u6d77\u5e02'}, {u'code': u'230000', u'name': u'\u9ed1\u9f99\u6c5f\u7701'}, {u'code': u'220000', u'name': u'\u5409\u6797\u7701'}, {u'code': u'210000', u'name': u'\u8fbd\u5b81\u7701'}, {u'code': u'150001', u'name': u'\u5185\u8499\u53e4\u81ea\u6cbb\u533a'}, {u'code': u'150000', u'name': u'\u5185\u8499\u53e4\u81ea\u6cbb\u533a'}, {u'code': u'140000', u'name': u'\u5c71\u897f\u7701'}, {u'code': u'130000', u'name': u'\u6cb3\u5317\u7701'}, {u'code': u'120000', u'name': u'\u5929\u6d25\u5e02'}, {u'code': u'110000', u'name': u'\u5317\u4eac\u5e02'}])

    def test_count_city(self):
        url = self.base_url + '/regions/city'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],[{u'code': u'920100', u'name': u'\u6df1\u5733\u5e02'}, {u'code': u'659000', u'name': u'\u81ea\u6cbb\u533a\u76f4\u8f96\u53bf\u7ea7\u884c\u653f\u533a\u5212'}, {u'code': u'654000', u'name': u'\u4f0a\u7281\u54c8\u8428\u514b\u81ea\u6cbb\u5dde'}, {u'code': u'652900', u'name': u'\u963f\u514b\u82cf\u5730\u533a'}, {u'code': u'652800', u'name': u'\u5df4\u97f3\u90ed\u695e\u8499\u53e4\u81ea\u6cbb\u5dde'}, {u'code': u'652300', u'name': u'\u660c\u5409\u56de\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'650200', u'name': u'\u514b\u62c9\u739b\u4f9d\u5e02'}, {u'code': u'650100', u'name': u'\u4e4c\u9c81\u6728\u9f50\u5e02'}, {u'code': u'640500', u'name': u'\u4e2d\u536b\u5e02'}, {u'code': u'640400', u'name': u'\u56fa\u539f\u5e02'}, {u'code': u'640300', u'name': u'\u5434\u5fe0\u5e02'}, {u'code': u'640200', u'name': u'\u77f3\u5634\u5c71\u5e02'}, {u'code': u'640100', u'name': u'\u94f6\u5ddd\u5e02'}, {u'code': u'632800', u'name': u'\u6d77\u897f\u8499\u53e4\u65cf\u85cf\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'630100', u'name': u'\u897f\u5b81\u5e02'}, {u'code': u'621000', u'name': u'\u5e86\u9633\u5e02'}, {u'code': u'620900', u'name': u'\u9152\u6cc9\u5e02'}, {u'code': u'620500', u'name': u'\u5929\u6c34\u5e02'}, {u'code': u'620400', u'name': u'\u767d\u94f6\u5e02'}, {u'code': u'620200', u'name': u'\u5609\u5cea\u5173\u5e02'}, {u'code': u'620100', u'name': u'\u5170\u5dde\u5e02'}, {u'code': u'610900', u'name': u'\u5b89\u5eb7\u5e02'}, {u'code': u'610800', u'name': u'\u6986\u6797\u5e02'}, {u'code': u'610600', u'name': u'\u5ef6\u5b89\u5e02'}, {u'code': u'610500', u'name': u'\u6e2d\u5357\u5e02'}, {u'code': u'610400', u'name': u'\u54b8\u9633\u5e02'}, {u'code': u'610300', u'name': u'\u5b9d\u9e21\u5e02'}, {u'code': u'610100', u'name': u'\u897f\u5b89\u5e02'}, {u'code': u'533500', u'name': u'\u666e\u6d31\u5e02'}, {u'code': u'533100', u'name': u'\u5fb7\u5b8f\u50a3\u65cf\u666f\u9887\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'532900', u'name': u'\u5927\u7406\u767d\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'532800', u'name': u'\u897f\u53cc\u7248\u7eb3\u50a3\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'532600', u'name': u'\u6587\u5c71\u58ee\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'532500', u'name': u'\u7ea2\u6cb3\u54c8\u5c3c\u65cf\u5f5d\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'532300', u'name': u'\u695a\u96c4\u5f5d\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'530700', u'name': u'\u4e3d\u6c5f\u5e02'}, {u'code': u'530600', u'name': u'\u662d\u901a\u5e02'}, {u'code': u'530500', u'name': u'\u4fdd\u5c71\u5e02'}, {u'code': u'530400', u'name': u'\u7389\u6eaa\u5e02'}, {u'code': u'530300', u'name': u'\u66f2\u9756\u5e02'}, {u'code': u'530100', u'name': u'\u6606\u660e\u5e02'}, {u'code': u'522800', u'name': u'\u5174\u4e49\u5e02'}, {u'code': u'522700', u'name': u'\u9ed4\u5357\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'522600', u'name': u'\u9ed4\u4e1c\u5357\u82d7\u65cf\u4f97\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'522400', u'name': u'\u6bd5\u8282\u5e02'}, {u'code': u'522300', u'name': u'\u9ed4\u897f\u5357\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'522200', u'name': u'\u94dc\u4ec1\u5e02'}, {u'code': u'520400', u'name': u'\u5b89\u987a\u5e02'}, {u'code': u'520300', u'name': u'\u9075\u4e49\u5e02'}, {u'code': u'520200', u'name': u'\u516d\u76d8\u6c34\u5e02'}, {u'code': u'520100', u'name': u'\u8d35\u9633\u5e02'}, {u'code': u'513400', u'name': u'\u51c9\u5c71\u5f5d\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'512000', u'name': u'\u8d44\u9633\u5e02'}, {u'code': u'511800', u'name': u'\u96c5\u5b89\u5e02'}, {u'code': u'511700', u'name': u'\u8fbe\u5dde\u5e02'}, {u'code': u'511600', u'name': u'\u5e7f\u5b89\u5e02'}, {u'code': u'511500', u'name': u'\u5b9c\u5bbe\u5e02'}, {u'code': u'511400', u'name': u'\u7709\u5c71\u5e02'}, {u'code': u'511300', u'name': u'\u5357\u5145\u5e02'}, {u'code': u'511100', u'name': u'\u4e50\u5c71\u5e02'}, {u'code': u'511000', u'name': u'\u5185\u6c5f\u5e02'}, {u'code': u'510900', u'name': u'\u9042\u5b81\u5e02'}, {u'code': u'510800', u'name': u'\u5e7f\u5143\u5e02'}, {u'code': u'510700', u'name': u'\u7ef5\u9633\u5e02'}, {u'code': u'510600', u'name': u'\u5fb7\u9633\u5e02'}, {u'code': u'510500', u'name': u'\u6cf8\u5dde\u5e02'}, {u'code': u'510400', u'name': u'\u6500\u679d\u82b1\u5e02'}, {u'code': u'510300', u'name': u'\u81ea\u8d21\u5e02'}, {u'code': u'510100', u'name': u'\u6210\u90fd\u5e02'}, {u'code': u'500100', u'name': u'\u91cd\u5e86\u5e02'}, {u'code': u'460200', u'name': u'\u4e09\u4e9a\u5e02'}, {u'code': u'460100', u'name': u'\u6d77\u53e3\u5e02'}, {u'code': u'451300', u'name': u'\u6765\u5bbe\u5e02'}, {u'code': u'451200', u'name': u'\u6cb3\u6c60\u5e02'}, {u'code': u'451100', u'name': u'\u8d3a\u5dde\u5e02'}, {u'code': u'451000', u'name': u'\u767e\u8272\u5e02'}, {u'code': u'450900', u'name': u'\u7389\u6797\u5e02'}, {u'code': u'450800', u'name': u'\u8d35\u6e2f\u5e02'}, {u'code': u'450700', u'name': u'\u94a6\u5dde\u5e02'}, {u'code': u'450600', u'name': u'\u9632\u57ce\u6e2f\u5e02'}, {u'code': u'450500', u'name': u'\u5317\u6d77\u5e02'}, {u'code': u'450400', u'name': u'\u68a7\u5dde\u5e02'}, {u'code': u'450300', u'name': u'\u6842\u6797\u5e02'}, {u'code': u'450200', u'name': u'\u67f3\u5dde\u5e02'}, {u'code': u'450100', u'name': u'\u5357\u5b81\u5e02'}, {u'code': u'445200', u'name': u'\u63ed\u9633\u5e02'}, {u'code': u'445100', u'name': u'\u6f6e\u5dde\u5e02'}, {u'code': u'442000', u'name': u'\u4e2d\u5c71\u5e02'}, {u'code': u'441900', u'name': u'\u4e1c\u839e\u5e02'}, {u'code': u'441800', u'name': u'\u6e05\u8fdc\u5e02'}, {u'code': u'441700', u'name': u'\u9633\u6c5f\u5e02'}, {u'code': u'441600', u'name': u'\u6cb3\u6e90\u5e02'}, {u'code': u'441500', u'name': u'\u6c55\u5c3e\u5e02'}, {u'code': u'441400', u'name': u'\u6885\u5dde\u5e02'}, {u'code': u'441300', u'name': u'\u60e0\u5dde\u5e02'}, {u'code': u'441200', u'name': u'\u8087\u5e86\u5e02'}, {u'code': u'440900', u'name': u'\u8302\u540d\u5e02'}, {u'code': u'440800', u'name': u'\u6e5b\u6c5f\u5e02'}, {u'code': u'440700', u'name': u'\u6c5f\u95e8\u5e02'}, {u'code': u'440600', u'name': u'\u4f5b\u5c71\u5e02'}, {u'code': u'440500', u'name': u'\u6c55\u5934\u5e02'}, {u'code': u'440400', u'name': u'\u73e0\u6d77\u5e02'}, {u'code': u'440300', u'name': u'\u6df1\u5733\u5e02'}, {u'code': u'440200', u'name': u'\u97f6\u5173\u5e02'}, {u'code': u'440100', u'name': u'\u5e7f\u5dde\u5e02'}, {u'code': u'433100', u'name': u'\u6e58\u897f\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'431300', u'name': u'\u5a04\u5e95\u5e02'}, {u'code': u'431200', u'name': u'\u6000\u5316\u5e02'}, {u'code': u'431100', u'name': u'\u6c38\u5dde\u5e02'}, {u'code': u'431000', u'name': u'\u90f4\u5dde\u5e02'}, {u'code': u'430900', u'name': u'\u76ca\u9633\u5e02'}, {u'code': u'430800', u'name': u'\u5f20\u5bb6\u754c\u5e02'}, {u'code': u'430700', u'name': u'\u5e38\u5fb7\u5e02'}, {u'code': u'430600', u'name': u'\u5cb3\u9633\u5e02'}, {u'code': u'430500', u'name': u'\u90b5\u9633\u5e02'}, {u'code': u'430400', u'name': u'\u8861\u9633\u5e02'}, {u'code': u'430300', u'name': u'\u6e58\u6f6d\u5e02'}, {u'code': u'430200', u'name': u'\u682a\u6d32\u5e02'}, {u'code': u'430100', u'name': u'\u957f\u6c99\u5e02'}, {u'code': u'429000', u'name': u'\u7701\u76f4\u8f96\u53bf\u7ea7\u884c\u653f\u533a\u5212'}, {u'code': u'422800', u'name': u'\u6069\u65bd\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'421300', u'name': u'\u968f\u5dde\u5e02'}, {u'code': u'421200', u'name': u'\u54b8\u5b81\u5e02'}, {u'code': u'421100', u'name': u'\u9ec4\u5188\u5e02'}, {u'code': u'421000', u'name': u'\u8346\u5dde\u5e02'}, {u'code': u'420900', u'name': u'\u5b5d\u611f\u5e02'}, {u'code': u'420800', u'name': u'\u8346\u95e8\u5e02'}, {u'code': u'420700', u'name': u'\u9102\u5dde\u5e02'}, {u'code': u'420600', u'name': u'\u8944\u9633\u5e02'}, {u'code': u'420500', u'name': u'\u5b9c\u660c\u5e02'}, {u'code': u'420300', u'name': u'\u5341\u5830\u5e02'}, {u'code': u'420200', u'name': u'\u9ec4\u77f3\u5e02'}, {u'code': u'420100', u'name': u'\u6b66\u6c49\u5e02'}, {u'code': u'411800', u'name': u'\u7701\u76f4\u8f96\u53bf\u7ea7\u884c\u653f\u533a\u5212'}, {u'code': u'411700', u'name': u'\u9a7b\u9a6c\u5e97\u5e02'}, {u'code': u'411600', u'name': u'\u5468\u53e3\u5e02'}, {u'code': u'411500', u'name': u'\u4fe1\u9633\u5e02'}, {u'code': u'411400', u'name': u'\u5546\u4e18\u5e02'}, {u'code': u'411300', u'name': u'\u5357\u9633\u5e02'}, {u'code': u'411200', u'name': u'\u4e09\u95e8\u5ce1\u5e02'}, {u'code': u'411100', u'name': u'\u6f2f\u6cb3\u5e02'}, {u'code': u'411000', u'name': u'\u8bb8\u660c\u5e02'}, {u'code': u'410900', u'name': u'\u6fee\u9633\u5e02'}, {u'code': u'410800', u'name': u'\u7126\u4f5c\u5e02'}, {u'code': u'410700', u'name': u'\u65b0\u4e61\u5e02'}, {u'code': u'410600', u'name': u'\u9e64\u58c1\u5e02'}, {u'code': u'410500', u'name': u'\u5b89\u9633\u5e02'}, {u'code': u'410400', u'name': u'\u5e73\u9876\u5c71\u5e02'}, {u'code': u'410300', u'name': u'\u6d1b\u9633\u5e02'}, {u'code': u'410200', u'name': u'\u5f00\u5c01\u5e02'}, {u'code': u'410100', u'name': u'\u90d1\u5dde\u5e02'}, {u'code': u'371700', u'name': u'\u83cf\u6cfd\u5e02'}, {u'code': u'371600', u'name': u'\u6ee8\u5dde\u5e02'}, {u'code': u'371500', u'name': u'\u804a\u57ce\u5e02'}, {u'code': u'371400', u'name': u'\u5fb7\u5dde\u5e02'}, {u'code': u'371300', u'name': u'\u4e34\u6c82\u5e02'}, {u'code': u'371200', u'name': u'\u83b1\u829c\u5e02'}, {u'code': u'371100', u'name': u'\u65e5\u7167\u5e02'}, {u'code': u'371000', u'name': u'\u5a01\u6d77\u5e02'}, {u'code': u'370900', u'name': u'\u6cf0\u5b89\u5e02'}, {u'code': u'370800', u'name': u'\u6d4e\u5b81\u5e02'}, {u'code': u'370700', u'name': u'\u6f4d\u574a\u5e02'}, {u'code': u'370600', u'name': u'\u70df\u53f0\u5e02'}, {u'code': u'370500', u'name': u'\u4e1c\u8425\u5e02'}, {u'code': u'370400', u'name': u'\u67a3\u5e84\u5e02'}, {u'code': u'370300', u'name': u'\u6dc4\u535a\u5e02'}, {u'code': u'370200', u'name': u'\u9752\u5c9b\u5e02'}, {u'code': u'370100', u'name': u'\u6d4e\u5357\u5e02'}, {u'code': u'361100', u'name': u'\u4e0a\u9976\u5e02'}, {u'code': u'361000', u'name': u'\u629a\u5dde\u5e02'}, {u'code': u'360900', u'name': u'\u5b9c\u6625\u5e02'}, {u'code': u'360800', u'name': u'\u5409\u5b89\u5e02'}, {u'code': u'360700', u'name': u'\u8d63\u5dde\u5e02'}, {u'code': u'360600', u'name': u'\u9e70\u6f6d\u5e02'}, {u'code': u'360500', u'name': u'\u65b0\u4f59\u5e02'}, {u'code': u'360400', u'name': u'\u4e5d\u6c5f\u5e02'}, {u'code': u'360300', u'name': u'\u840d\u4e61\u5e02'}, {u'code': u'360200', u'name': u'\u666f\u5fb7\u9547\u5e02'}, {u'code': u'360100', u'name': u'\u5357\u660c\u5e02'}, {u'code': u'350900', u'name': u'\u5b81\u5fb7\u5e02'}, {u'code': u'350800', u'name': u'\u9f99\u5ca9\u5e02'}, {u'code': u'350700', u'name': u'\u5357\u5e73\u5e02'}, {u'code': u'350600', u'name': u'\u6f33\u5dde\u5e02'}, {u'code': u'350500', u'name': u'\u6cc9\u5dde\u5e02'}, {u'code': u'350400', u'name': u'\u4e09\u660e\u5e02'}, {u'code': u'350300', u'name': u'\u8386\u7530\u5e02'}, {u'code': u'350200', u'name': u'\u53a6\u95e8\u5e02'}, {u'code': u'350100', u'name': u'\u798f\u5dde\u5e02'}, {u'code': u'341800', u'name': u'\u5ba3\u57ce\u5e02'}, {u'code': u'341500', u'name': u'\u516d\u5b89\u5e02'}, {u'code': u'341300', u'name': u'\u5bbf\u5dde\u5e02'}, {u'code': u'341200', u'name': u'\u961c\u9633\u5e02'}, {u'code': u'341100', u'name': u'\u6ec1\u5dde\u5e02'}, {u'code': u'341000', u'name': u'\u9ec4\u5c71\u5e02'}, {u'code': u'340800', u'name': u'\u5b89\u5e86\u5e02'}, {u'code': u'340700', u'name': u'\u94dc\u9675\u5e02'}, {u'code': u'340600', u'name': u'\u6dee\u5317\u5e02'}, {u'code': u'340500', u'name': u'\u9a6c\u978d\u5c71\u5e02'}, {u'code': u'340400', u'name': u'\u6dee\u5357\u5e02'}, {u'code': u'340300', u'name': u'\u868c\u57e0\u5e02'}, {u'code': u'340200', u'name': u'\u829c\u6e56\u5e02'}, {u'code': u'340100', u'name': u'\u5408\u80a5\u5e02'}, {u'code': u'331100', u'name': u'\u4e3d\u6c34\u5e02'}, {u'code': u'331000', u'name': u'\u53f0\u5dde\u5e02'}, {u'code': u'330900', u'name': u'\u821f\u5c71\u5e02'}, {u'code': u'330800', u'name': u'\u8862\u5dde\u5e02'}, {u'code': u'330700', u'name': u'\u91d1\u534e\u5e02'}, {u'code': u'330600', u'name': u'\u7ecd\u5174\u5e02'}, {u'code': u'330500', u'name': u'\u6e56\u5dde\u5e02'}, {u'code': u'330400', u'name': u'\u5609\u5174\u5e02'}, {u'code': u'330300', u'name': u'\u6e29\u5dde\u5e02'}, {u'code': u'330200', u'name': u'\u5b81\u6ce2\u5e02'}, {u'code': u'330100', u'name': u'\u676d\u5dde\u5e02'}, {u'code': u'321300', u'name': u'\u5bbf\u8fc1\u5e02'}, {u'code': u'321200', u'name': u'\u6cf0\u5dde\u5e02'}, {u'code': u'321100', u'name': u'\u9547\u6c5f\u5e02'}, {u'code': u'321000', u'name': u'\u626c\u5dde\u5e02'}, {u'code': u'320900', u'name': u'\u76d0\u57ce\u5e02'}, {u'code': u'320800', u'name': u'\u6dee\u5b89\u5e02'}, {u'code': u'320700', u'name': u'\u8fde\u4e91\u6e2f\u5e02'}, {u'code': u'320600', u'name': u'\u5357\u901a\u5e02'}, {u'code': u'320500', u'name': u'\u82cf\u5dde\u5e02'}, {u'code': u'320400', u'name': u'\u5e38\u5dde\u5e02'}, {u'code': u'320300', u'name': u'\u5f90\u5dde\u5e02'}, {u'code': u'320200', u'name': u'\u65e0\u9521\u5e02'}, {u'code': u'320100', u'name': u'\u5357\u4eac\u5e02'}, {u'code': u'310100', u'name': u'\u4e0a\u6d77\u5e02'}, {u'code': u'231200', u'name': u'\u7ee5\u5316\u5e02'}, {u'code': u'231000', u'name': u'\u7261\u4e39\u6c5f\u5e02'}, {u'code': u'230900', u'name': u'\u4e03\u53f0\u6cb3\u5e02'}, {u'code': u'230800', u'name': u'\u4f73\u6728\u65af\u5e02'}, {u'code': u'230700', u'name': u'\u4f0a\u6625\u5e02'}, {u'code': u'230600', u'name': u'\u5927\u5e86\u5e02'}, {u'code': u'230500', u'name': u'\u53cc\u9e2d\u5c71\u5e02'}, {u'code': u'230400', u'name': u'\u9e64\u5c97\u5e02'}, {u'code': u'230300', u'name': u'\u9e21\u897f\u5e02'}, {u'code': u'230200', u'name': u'\u9f50\u9f50\u54c8\u5c14\u5e02'}, {u'code': u'230100', u'name': u'\u54c8\u5c14\u6ee8\u5e02'}, {u'code': u'222400', u'name': u'\u5ef6\u8fb9\u671d\u9c9c\u65cf\u81ea\u6cbb\u5dde'}, {u'code': u'220800', u'name': u'\u767d\u57ce\u5e02'}, {u'code': u'220700', u'name': u'\u677e\u539f\u5e02'}, {u'code': u'220600', u'name': u'\u767d\u5c71\u5e02'}, {u'code': u'220500', u'name': u'\u901a\u5316\u5e02'}, {u'code': u'220400', u'name': u'\u8fbd\u6e90\u5e02'}, {u'code': u'220300', u'name': u'\u56db\u5e73\u5e02'}, {u'code': u'220200', u'name': u'\u5409\u6797\u5e02'}, {u'code': u'220100', u'name': u'\u957f\u6625\u5e02'}, {u'code': u'211400', u'name': u'\u846b\u82a6\u5c9b\u5e02'}, {u'code': u'211300', u'name': u'\u671d\u9633\u5e02'}, {u'code': u'211200', u'name': u'\u94c1\u5cad\u5e02'}, {u'code': u'211100', u'name': u'\u76d8\u9526\u5e02'}, {u'code': u'211000', u'name': u'\u8fbd\u9633\u5e02'}, {u'code': u'210900', u'name': u'\u961c\u65b0\u5e02'}, {u'code': u'210800', u'name': u'\u8425\u53e3\u5e02'}, {u'code': u'210700', u'name': u'\u9526\u5dde\u5e02'}, {u'code': u'210600', u'name': u'\u4e39\u4e1c\u5e02'}, {u'code': u'210500', u'name': u'\u672c\u6eaa\u5e02'}, {u'code': u'210400', u'name': u'\u629a\u987a\u5e02'}, {u'code': u'210300', u'name': u'\u978d\u5c71\u5e02'}, {u'code': u'210200', u'name': u'\u5927\u8fde\u5e02'}, {u'code': u'210100', u'name': u'\u6c88\u9633\u5e02'}, {u'code': u'153000', u'name': u'\u51c6\u683c\u5c14\u65d7'}, {u'code': u'152900', u'name': u'\u963f\u62c9\u5584\u76df'}, {u'code': u'152500', u'name': u'\u9521\u6797\u90ed\u52d2\u76df'}, {u'code': u'150900', u'name': u'\u4e4c\u5170\u5bdf\u5e03\u5e02'}, {u'code': u'150800', u'name': u'\u5df4\u5f66\u6dd6\u5c14\u5e02'}, {u'code': u'150701', u'name': u'\u547c\u4f26\u8d1d\u5c14\u5e02'}, {u'code': u'150600', u'name': u'\u9102\u5c14\u591a\u65af\u5e02'}, {u'code': u'150500', u'name': u'\u901a\u8fbd\u5e02'}, {u'code': u'150400', u'name': u'\u8d64\u5cf0\u5e02'}, {u'code': u'150300', u'name': u'\u4e4c\u6d77\u5e02'}, {u'code': u'150200', u'name': u'\u5305\u5934\u5e02'}, {u'code': u'150100', u'name': u'\u547c\u548c\u6d69\u7279\u5e02'}, {u'code': u'141100', u'name': u'\u5415\u6881\u5e02'}, {u'code': u'141000', u'name': u'\u4e34\u6c7e\u5e02'}, {u'code': u'140900', u'name': u'\u5ffb\u5dde\u5e02'}, {u'code': u'140800', u'name': u'\u8fd0\u57ce\u5e02'}, {u'code': u'140700', u'name': u'\u664b\u4e2d\u5e02'}, {u'code': u'140600', u'name': u'\u6714\u5dde\u5e02'}, {u'code': u'140500', u'name': u'\u664b\u57ce\u5e02'}, {u'code': u'140400', u'name': u'\u957f\u6cbb\u5e02'}, {u'code': u'140300', u'name': u'\u9633\u6cc9\u5e02'}, {u'code': u'140200', u'name': u'\u5927\u540c\u5e02'}, {u'code': u'140100', u'name': u'\u592a\u539f\u5e02'}, {u'code': u'131200', u'name': u'\u8fc1\u5b89\u5e02'}, {u'code': u'131100', u'name': u'\u8861\u6c34\u5e02'}, {u'code': u'131000', u'name': u'\u5eca\u574a\u5e02'}, {u'code': u'130900', u'name': u'\u6ca7\u5dde\u5e02'}, {u'code': u'130800', u'name': u'\u627f\u5fb7\u5e02'}, {u'code': u'130700', u'name': u'\u5f20\u5bb6\u53e3\u5e02'}, {u'code': u'130600', u'name': u'\u4fdd\u5b9a\u5e02'}, {u'code': u'130500', u'name': u'\u90a2\u53f0\u5e02'}, {u'code': u'130400', u'name': u'\u90af\u90f8\u5e02'}, {u'code': u'130300', u'name': u'\u79e6\u7687\u5c9b\u5e02'}, {u'code': u'130200', u'name': u'\u5510\u5c71\u5e02'}, {u'code': u'130100', u'name': u'\u77f3\u5bb6\u5e84\u5e02'}, {u'code': u'120100', u'name': u'\u5929\u6d25\u5e02'}, {u'code': u'110100', u'name': u'\u5317\u4eac\u5e02'}])

    def test_getConfig(self):
        url = self.base_url + '/admin/home/getConfig'
        r = requests.get(url, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],[{u'y': 1, u'index': u'region_wx_scan', u'x': 1}, {u'y': 2, u'index': u'city_wx_scan_rank', u'x': 1}, {u'y': 1, u'index': u'province_wx_scan_ten', u'x': 5}, {u'y': 2, u'index': u'shop_wx_scan_rank', u'x': 5}, {u'y': 1, u'index': u'city_wx_scan_ten', u'x': 10}, {u'y': 2, u'index': u'province_wx_scan_map', u'x': 10}, {u'y': 1, u'index': u'shop_wx_scan_ten', u'x': 15}, {u'y': 2, u'index': u'region_target_rate', u'x': 15}, {u'y': 1, u'index': u'city_target_rate_ten', u'x': 20}, {u'y': 2, u'index': u'shop_target_rate_ten', u'x': 20}])

    def test_Config(self):
        url = self.base_url + '/admin/home/Config'
        data=[
            {'index': 'region_wx_scan', 'x': 1, 'y': 1}, {'index': 'city_wx_scan_rank', 'x': 1, 'y': 2},
            {'index': 'province_wx_scan_ten', 'x': 5, 'y': 1},{'index': 'shop_wx_scan_rank', 'x': 5, 'y': 2},
            {'index': 'city_wx_scan_ten', 'x': 10, 'y': 1},{'index': 'province_wx_scan_map', 'x': 10, 'y': 2},
            {'index': 'shop_wx_scan_ten', 'x': 15, 'y': 1},{'index': 'region_target_rate', 'x': 15, 'y': 2},
            {'index': 'city_target_rate_ten', 'x': 20, 'y': 1},{'index': 'shop_target_rate_ten', 'x': 20, 'y': 2}
        ]
        payload = json.dumps(data)
        r = requests.post(url, cookies=self.cookie,data={'cfg':payload})
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],[u'\u914d\u7f6e\u6210\u529f'])