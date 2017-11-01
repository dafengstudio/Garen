#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
from unittest import TestCase

from Garen import Garen


# @timger http://weibo.com/zhanghaibo
class TestGaren(TestCase):
    def setUp(self):
        import os
        pack_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')

        self.config_list = [
            os.path.join(pack_path, 'config.yml')
        ]

    def get_garen_object(self, config_path):
        o = Garen(port=9999,
                  config_fpath=config_path)
        return o

    def test_config_fpath(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            assert o.config_fpath == c_path, self.fail()

    def test_config(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            assert type(o.config) == dict, self.fail()

    def test_browser_cookie(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            print o.browser_cookie
            assert (not o.browser_cookie is None), self.fail()

    def test_update_request_headers(self):
        _default_headers = {"A": "b"}
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            _ = o.update_request_headers(_default_headers)
            print _
            assert 'Access-Control-Allow-Headers' in _.keys(), self.fail()

    def test_get_dest_origin_str_by_host(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            _1 = o.get_dest_origin_str_by_host('test.timger.info:9999')
            _2 = o.get_dest_origin_str_by_host('test.timger.info')
            print _1, _2
            assert _1 == 'baidu.com:80', self.fail()
            assert _2 == '127.0.0.1:80', self.fail()

    def _test_get_dest_ip_by_host(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            assert o.get_dest_origin_str_by_host('test.timger.info:9999') == 'baidu.com:80', self.fail()
            assert o.get_dest_origin_str_by_host('test.timger.info') == 'test.timger.info:80', self.fail()

    def _test_get_dest_port_by_host(self):
        for c_path in self.config_list:
            o = self.get_garen_object(c_path)
            assert o.get_dest_origin_str_by_host('test.timger.info:9999') == 'baidu.com:80', self.fail()
            assert o.get_dest_origin_str_by_host('test.timger.info') == 'test.timger.info:80', self.fail()

    def _test_get_host_port_from_headers(self):
        self.fail()

    def _test_get_path_prefix_from_headers(self):
        self.fail()

    def test_proxy_request(self):
        c_path = self.config_list[0]
        o = self.get_garen_object(c_path)
        o.start()

        def get_mock_request(url):
            import requests
            headers = {
                "PROXY": url
            }
            _url = "http://127.0.0.1:8899"
            response = requests.get(_url, headers=headers)
            return response

        # 测试域名转发

        response = get_mock_request('http://test.timger.info:9999/hello')
        print response

        # 测试静态资源


        # 测试
