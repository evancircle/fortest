#coding=utf-8
import unittest
import requests
import os, sys
import hashlib
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class BrandSummaryTest(unittest.TestCase):

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

    def test_search_scanner_id(self):
        url = self.base_url + '/mobile/brand/summary?shop_code=&shop_name=&period_from=2017-07-18&period_to=2017-07-18&scanner_id=BL160080&regionid=0&provinceid=0&cityid=0'
        r = requests.get(url, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'count': {u'scan_num': u'7'}, u'paging': {u'page_count': 1, u'total_count': u'1', u'record_end': u'1', u'record_start': 1}, u'list': [{u'province': u'\u5185\u8499\u53e4\u81ea\u6cbb\u533a', u'city': u'\u547c\u548c\u6d69\u7279\u5e02', u'shop_class': None, u'scanner_id': u'BL160080', u'wxscan': u'7', u'region': u'\u534e\u5317', u'regionid': u'100003', u'brand': u'0', u'shop_name': u'\u547c\u5e02\u5609\u8302\u8d2d\u7269\u4e2d\u5fc3\u5e97BL', u'cityid': u'150100', u'shop_type': u'\u8d2d\u7269\u4e2d\u5fc3', u'shop_code': u'DH13BL', u'scan_date': u'2017-07-18', u'provinceid': u'150000'}], u'page': 1})

    def test_search_shop_name(self):
        url = self.base_url + '/mobile/brand/summary?shop_code=&shop_name=中山石岐假日广场店ST&period_from=2017-07-31&period_to=2017-07-31&scanner_id=&regionid=0&provinceid=0&cityid=0'
        r = requests.get(url, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'count': {u'scan_num': u'12'}, u'paging': {u'page_count': 1, u'total_count': u'1', u'record_end': u'1', u'record_start': 1}, u'list': [{u'province': u'\u5e7f\u4e1c\u7701', u'city': u'\u4e2d\u5c71\u5e02', u'shop_class': None, u'scanner_id': u'BL170590', u'wxscan': u'12', u'region': u'\u534e\u5357', u'regionid': u'100001', u'brand': u'BL', u'shop_name': u'\u4e2d\u5c71\u77f3\u5c90\u5047\u65e5\u5e7f\u573a\u5e97ST', u'cityid': u'442000', u'shop_type': u'\u8d2d\u7269\u4e2d\u5fc3', u'shop_code': u'K502ST', u'scan_date': u'2017-07-31', u'provinceid': u'440000'}], u'page': 1})

    def test_search_shop_code(self):
        url = self.base_url + '/mobile/brand/summary?shop_code=DBI3BL&shop_name=&period_from=2017-07-31&period_to=2017-07-31&scanner_id=&regionid=0&provinceid=0&cityid=0'
        r = requests.get(url, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'count': {u'scan_num': u'1'}, u'paging': {u'page_count': 1, u'total_count': u'1', u'record_end': u'1', u'record_start': 1}, u'list': [{u'province': u'\u5317\u4eac\u5e02', u'city': u'\u5317\u4eac\u5e02', u'shop_class': None, u'scanner_id': u'BL170996', u'wxscan': u'1', u'region': u'\u534e\u5317', u'regionid': u'100003', u'brand': u'BL', u'shop_name': u'\u5317\u4eac\u592a\u9633\u5bab\u51ef\u5fb7\u5e97BL', u'cityid': u'110100', u'shop_type': u'\u8d2d\u7269\u4e2d\u5fc3', u'shop_code': u'DBI3BL', u'scan_date': u'2017-07-31', u'provinceid': u'110000'}], u'page': 1})

    def test_search_cityid(self):
        url = self.base_url + '/mobile/brand/summary?shop_code=&shop_name=&period_from=2017-07-31&period_to=2017-07-31&scanner_id=&regionid=100003&provinceid=150000&cityid=150300'
        r = requests.get(url, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'count': {u'scan_num': u'1'}, u'paging': {u'page_count': 1, u'total_count': u'1', u'record_end': u'1', u'record_start': 1}, u'list': [{u'province': u'\u5185\u8499\u53e4\u81ea\u6cbb\u533a', u'city': u'\u4e4c\u6d77\u5e02', u'shop_class': None, u'scanner_id': u'BL170869', u'wxscan': u'1', u'region': u'\u534e\u5317', u'regionid': u'100003', u'brand': u'0', u'shop_name': u'\u4e4c\u6d77\u4e07\u8fbe\u5e7f\u573a\u5e97MAP', u'cityid': u'150300', u'shop_type': u'\u8d2d\u7269\u4e2d\u5fc3', u'shop_code': u'DH02MA', u'scan_date': u'2017-07-31', u'provinceid': u'150000'}], u'page': 1})