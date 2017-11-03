#coding=utf-8
import unittest
import requests
import os, sys
import hashlib
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://bossdev.epoque.cn/auth/entry'

    def tearDown(self):
        print self.result

    def test_login_success(self):
        md5 = hashlib.md5()
        sign_str = '000000'
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        password = md5.hexdigest()
        s = requests.Session()
        payload = {'username':'admin','password':password}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 0)
        self.assertEqual(self.result['data'],{u'rolename': u'\u603b\u7ba1\u7406\u5458', u'nickname': u'Admin'})

    def test_username_password_null(self):
        s = requests.Session()
        payload = {'username':'','password':''}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 100001)
        self.assertEqual(self.result['errmsg'],u'\u8bf7\u8f93\u5165\u7528\u6237\u540d')

    def test_loginname_null(self):
        md5 = hashlib.md5()
        sign_str = '000000'
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        password = md5.hexdigest()
        s = requests.Session()
        payload = {'username':'','password':password}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'],100001)
        self.assertEqual(self.result['errmsg'],u'\u8bf7\u8f93\u5165\u7528\u6237\u540d')

    def test_password_null(self):
        s = requests.Session()
        payload = {'username':'admin','password':''}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'],100002)
        self.assertEqual(self.result['errmsg'],u'\u8bf7\u8f93\u5165\u5bc6\u7801')

    def test_password_error(self):
        md5 = hashlib.md5()
        sign_str = '111111'
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        password = md5.hexdigest()
        s = requests.Session()
        payload = {'username':'admin','password':password}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'],100003)
        self.assertEqual(self.result['errmsg'],u'\u8f93\u5165\u7684\u7528\u6237\u540d\u5bc6\u7801\u9519\u8bef\uff0c\u8bf7\u91cd\u65b0\u8f93\u5165')

    def test_admin_error(self):
        md5 = hashlib.md5()
        sign_str = '111111'
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        password = md5.hexdigest()
        s = requests.Session()
        payload = {'username':'AAA','password':password}
        r = s.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errcode'],100003)
        self.assertEqual(self.result['errmsg'],u'\u8f93\u5165\u7684\u7528\u6237\u540d\u5bc6\u7801\u9519\u8bef\uff0c\u8bf7\u91cd\u65b0\u8f93\u5165')

if __name__ == '__main__':
    unittest.main()
