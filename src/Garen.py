#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo
import threading
from gevent.server import StreamServer
from gevent.pool import Pool
from http_parser.reader import SocketReader
from http_parser.http import HttpStream
import requests

"""
.. automodule:: Garen



"""

class Garen(threading.Thread):
    """
    使用线程便于集成到其他系统
    """
    DEFAULT_CONFIG_NAME = ".garen.yml"
    SESSION_MAP = {}

    def __init__(self, port, browser_name, config_fpath=None):
        """

        :param port:
        :param browser_name:
        :param config_fpath:
        """
        self.port = port
        self.browser_name = browser_name
        self._config_fpath = config_fpath

    @property
    def user_directory(self):
        """

        :return:
        """
        from os import path
        return path.expanduser("~")

    @property
    def config_fpath(self):
        """

        :return:
        """
        from os import path
        if not self._config_fpath:
            self._config_fpath = path.join(self.user_directory, self.DEFAULT_CONFIG_NAME)
        return self._config_fpath

    @property
    def config(self):
        """
        获取到路由配置
        和 HOST 文件类似
        Lazy Load config File

        .. code-block::

            www.aliyun.com 127.0.0.1
            www.google.com 127.0.0.1

        :return:
        """
        import codecs
        import yaml
        if not self._config:
            with codecs.open(self.config_fpath, 'rb+', 'utf8') as fr:
                self._config = yaml.load(fr)
        return self._config

    @property
    def browsercookie(self):
        """

        :return:
        """
        pass

    def response_stream(self, socket):
        """
        1.  修正跨域的header
        2.  修正 Set Header 到对于的域名
        3.  返回正常的结果
        :param socket:
        :return:
        """
        pass

    def proxy_request_stream(self, dist_ip, domain, method, headers, query_string, socket):
        """
        1.  根据 Ddmian 获取到 cookie
        2.  获取到目标地址
        3.  发送 HTTP 包

        :param dist_ip:
        :param domain:
        :param method:
        :param headers:
        :param query_string:
        :param socket:
        :return:
        """
        pass

    def hander_revice_stream(self, socket, address):
        """
        1.  读取 request 流
        2.
        :param socket:
        :param address:
        :return:
        """
        p = HttpStream(SocketReader(socket), decompress=True)
        domain = p['Host']
        dist_ip = self.config[domain].ip
        headers = p.headers()
        method = p.method()
        query_string = p.query_string()
        self.proxy_request_stream(dist_ip, domain, method,
                                  headers, query_string, socket)

    @property
    def server(self):
        if hasattr(self, '_server'):
            return self._server

    def run(self):
        """
        run the gevent Server
        http://www.gevent.org/servers.html
        :return:
        """
        pool = Pool(10000)
        self._server = StreamServer(('127.0.0.1', self.port), self.hander_revice_stream,
                                    spawn=pool)  # creates a new server
        self._server.serve_forever()


def main():
    pass


if __name__ == "__main__":
    main()
