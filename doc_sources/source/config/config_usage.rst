配置格式
======================

配置格式基于 YAML
附加支持 header 和 cookie 的转发定义

.. code-block:: yml

    edas.console.aliyun.com:
        target: 127.0.0.1:80
        headers:
            key: value
        cookie:
            key: value