# WSGI 是什么？

全称`Python Web Server Gateway Interface`，指定了web服务器和Python web应用或web框架之间的标准接口，以提高web应用在一系列web服务器间的*移植性*。从名字就可以看出来，这东西是一个Gateway，也就是网关。网关的作用就是在协议之间进行转换。

## **WSGI 是什么，因何而生？**

### 引用PEP333内容

> WSGI 接口有服务端和应用端两部分，服务端也可以叫网关端，应用端也叫框架端。服务端调用一个由应用端提供的可调用对象。如何提供这个对象，由服务端决定。例如某些服务器或者网关需要应用的部署者写一段脚本，以创建服务器或者网关的实例，并且为这个实例提供一个应用实例。另一些服务器或者网关则可能使用配置文件或其他方法以指定应用实例应该从哪里导入或获取。

### WSGI 对于 application 对象有如下三点要求:

1.  必须是一个可调用的对象
2.  接收两个必选参数environ、start_response。
3.  返回值是可迭代对象，用来表示http body。

## 我的理解

WSGI是一套接口标准协议/规范，作用于Web服务器和Python Web应用程序之间，目的是制定标准，以保证不同Web服务器可以和不同的Python程序之间相互通信。

![](https://upload-images.jianshu.io/upload_images/1472084-53ea2f2c1c948b6b.png?imageMogr2/auto-orient/strip|imageView2/2/w/300/format/webp)


## 参考链接
- [WSGI是什么，看完一定懂](https://foofish.net/python-wsgi.html)
