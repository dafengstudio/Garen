#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo
import threading
from gevent.server import StreamServer
from gevent.pool import Pool


class Garen(threading.Thread):
    """
    使用线程便于集成到其他系统
    """
    DEFAULT_CONFIG_NAME = ".garen.yml"

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

    def send_stream(self, dist_ip, domain, ):
        pass

    def hander_stream(self, socket, address):
        pass

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
        self._server = StreamServer(('127.0.0.1', self.port), self.hander_stream, spawn=pool)  # creates a new server
        self._server.serve_forever()


def main():
    pass


if __name__ == "__main__":
    main()
