#coding=utf-8
import unittest
import requests
import os, sys
import hashlib
import datetime
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class wxScanMapTest(unittest.TestCase):

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
        url = self.base_url + '/admin/home/wxScanMap?datatype=region&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&code='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_date': u'2017-07-01', u'list': [{u'inquiry': u'23682', u'name': u'\u534e\u5357'}], u'to_date': u'2017-07-07'})

    def test_count_province(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=province&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&code=100001'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_date': u'2017-07-01', u'list': [{u'inquiry': u'12559', u'name': u'\u5e7f\u4e1c\u7701'}], u'to_date': u'2017-07-07'})

    def test_count_city(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=city&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&code=520000'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_date': u'2017-07-01', u'list': [{u'inquiry': u'159', u'name': u'\u8d35\u9633\u5e02'}], u'to_date': u'2017-07-07'})

    def test_count_yesterday(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=city&key=yesterday&top=1&from_date=&to_date=&code=440000'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],{u'from_date': u'%s'%str(yesterday), u'list': [{u'inquiry': u'0', u'name': u'\u97f6\u5173\u5e02'}], u'to_date': u'%s'%str(yesterday)})

    def test_count_day(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=city&key=day&top=1&from_date=&to_date=&code=440000'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        today = datetime.date.today()
        self.assertEqual(self.result['data'],{u'from_date': u'%s'%str(today), u'list': [{u'inquiry': u'0', u'name': u'\u97f6\u5173\u5e02'}], u'to_date': u'%s'%str(today)})

    def test_count_day7(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=city&key=day7&top=1&from_date=&to_date=&code=440000'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        day7 = datetime.date.today() - datetime.timedelta(days=7)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],{u'from_date': u'%s'%str(day7), u'list': [{u'inquiry': u'0', u'name': u'\u97f6\u5173\u5e02'}], u'to_date': u'%s'%str(yesterday)})

    def test_count_day30(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=city&key=day30&top=1&from_date=&to_date=&code=440000'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        day30 = datetime.date.today() - datetime.timedelta(days=30)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],{u'from_date': u'%s'%str(day30), u'list': [{u'inquiry': u'13686', u'name': u'\u5e7f\u5dde\u5e02'}], u'to_date': u'%s'%str(yesterday)})

    def test_error(self):
        url = self.base_url + '/admin/home/wxScanMap?datatype=&key=&top=&from_date=&to_date=&code='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], u'800004')
        self.assertEqual(self.result['errmsg'],u'datatype\u53c2\u6570\u6ca1\u6709\u8bbe\u7f6e[ region | province | city | shop ]')