用法
===================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    chrome
    command


使用脚手架过程需要满足两个条件

1.  DNS 拦截模式
    1.  浏览器正常发请求
    2.  host 文件拦截请求到代理服务器. 根据请求带上的Header走
        AJAX 需要加 Header 指定目标代理地址,此处 DNS 走本地 HOST
2.  chrome 插件模式
    1.  浏览器发正常的请求,由代理插件转发到代理地址
    2.  插件再根据 HOST 字段走 DNS