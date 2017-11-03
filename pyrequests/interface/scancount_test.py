#coding=utf-8
import unittest
import requests
import os, sys
import hashlib
import datetime
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
        url = self.base_url + '/admin/home/wxScanCount?datatype=region&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&from_compare=2017-07-08&to_compare=2017-07-15'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_compare': u'2017-07-08', u'to_compare': u'2017-07-15', u'from_date': u'2017-07-01',
                                              u'list': [{u'compare': u'34303', u'inquiry': u'23682', u'name': u'\u534e\u5357', u'rate': u'-31'}],
                                              u'to_date': u'2017-07-07'})

    def test_count_province(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=province&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&from_compare=2017-07-08&to_compare=2017-07-15'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_compare': u'2017-07-08', u'to_compare': u'2017-07-15', u'from_date': u'2017-07-01',
                                              u'list': [{u'compare': u'18615', u'inquiry': u'12559', u'name': u'\u5e7f\u4e1c\u7701', u'rate': u'-33'}],
                                              u'to_date': u'2017-07-07'})

    def test_count_city(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=city&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&from_compare=2017-07-08&to_compare=2017-07-15'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_compare': u'2017-07-08', u'to_compare': u'2017-07-15', u'from_date': u'2017-07-01',
                                              u'list': [{u'compare': u'6761', u'inquiry': u'4992', u'name': u'\u6df1\u5733\u5e02', u'rate': u'-26'}],
                                              u'to_date': u'2017-07-07'})

    def test_count_shop(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=shop&key=&top=1&from_date=2017-07-01&to_date=2017-07-07&from_compare=2017-07-08&to_compare=2017-07-15'
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'from_compare': u'2017-07-08', u'to_compare': u'2017-07-15', u'from_date': u'2017-07-01',
                                              u'list': [{u'compare': u'621', u'inquiry': u'624', u'name': u'\u5357\u5b81\u671d\u9633\u8def\u767e\u76db\u8d2d\u7269\u5e7f\u573aBL', u'rate': u'0'}],
                                              u'to_date': u'2017-07-07'})

    def test_count_yesterday(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=region&key=yesterday&top=1&from_date=&to_date=&from_compare=&to_compare='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        before_yesterday = datetime.date.today() - datetime.timedelta(days=2)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],
                         {u'from_compare': u'%s' % str(before_yesterday), u'to_compare': u'%s' % str(before_yesterday),
                          u'from_date': u'%s' % str(yesterday),
                          u'list': [{u'compare': u'0', u'inquiry': u'0', u'name': u'\u9c81\u8c6b', u'rate': u'0'}],
                          u'to_date': u'%s' % str(yesterday)})

    def test_count_day(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=region&key=day&top=1&from_date=&to_date=&from_compare=&to_compare='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],{u'from_compare': u'%s'%str(yesterday), u'to_compare':  u'%s'%str(yesterday),
                                              u'from_date':  u'%s'%str(today),
                                              u'list': [{u'compare': u'0', u'inquiry': u'0', u'name': u'\u9c81\u8c6b', u'rate': u'0'}],
                                              u'to_date':  u'%s'%str(today)})

    def test_count_day7(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=region&key=day7&top=1&from_date=&to_date=&from_compare=&to_compare='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        day14 = datetime.date.today() - datetime.timedelta(days=14)
        day8 = datetime.date.today() - datetime.timedelta(days=8)
        day7 = datetime.date.today() - datetime.timedelta(days=7)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'], {u'from_compare': u'%s' % str(day14), u'to_compare': u'%s' % str(day8),
                                               u'from_date': u'%s' % str(day7),
                                               u'list': [{u'compare': u'1600', u'inquiry': u'0', u'name': u'\u9c81\u8c6b',
                                                          u'rate': u'0'}],
                                               u'to_date': u'%s' % str(yesterday)})
    def test_count_day30(self):
        url = self.base_url + '/admin/home/wxScanCount?datatype=region&key=day30&top=1&from_date=&to_date=&from_compare=&to_compare='
        r = requests.get(url,cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        day60 = datetime.date.today() - datetime.timedelta(days=60)
        day31 = datetime.date.today() - datetime.timedelta(days=31)
        day30 = datetime.date.today() - datetime.timedelta(days=30)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.result['data'],{u'from_compare': u'%s'%str(day60), u'to_compare':  u'%s'%str(day31),
                                              u'from_date':  u'%s'%str(day30),
                                              u'list': [{u'compare': u'212863', u'inquiry': u'94529', u'name': u'\u534e\u5357', u'rate': u'-56'}],
                                              u'to_date':  u'%s'%str(yesterday)})