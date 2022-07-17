# 最佳实践 - 关于获取客户端ip

> 参考链接：https://www.cnblogs.com/lovearpu/p/11187215.html

获取客户端ip的方案主要有两种

一种是获取http请求头种的X-Forwarded-For参数，另一种是直接通过remoteAddress获取**TCP层直接连接的客户端的IP**

这两种方案都有一定的问题

![image-20220717095538464](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20220717095538464.png)

# 方案1：获取X-Forwarded-For

HTTP协议头中添加X-Forwarded-For头，用来追踪请求的来源

X-Forwarded-For: client1, proxy1, proxy2, 即 **172.31.1.2,192.168.10.2,192.168.10.3**

X-Forwarded-For包含多个IP地址，每个值通过逗号+空格分开，最左边（client1）是最原始客户端的IP地址，中间如果有多层代理，每一层代理会将连接它的客户端IP追加在X-Forwarded-For右边。

所以我们想要拿到客户端ip，就得取第一个，也就是client1

```javascript
  var forwardedIpsStr = req.header("x-forwarded-for");
  var ip = "";

  if (forwardedIpsStr) {
    ip = forwardedIps = forwardedIpsStr.split(",")[0]; // 取第一个
  };
```

# 方案2：remoteAddress

> **TCP层直接连接的客户端的IP**

```JavaScript
// remoteAddress is "::ffff:127.0.0.1" ::ffff: 是IPV6相关
ip = req.socket.remoteAddress.split(':')[3];
```

# 你以为这就完了

> too young too simple

方案1中**x-forwarded-for**客户端可以伪造的

```JavaScript
curl --location --request GET 'http://127.0.0.1:3000/' \
--header 'x-forwarded-for: 123'

// {"code":0,"msg":"Real Ip is 123"}
```

方案2如果我们使用nginx做反向代理

```JavaScript
curl --location --request GET 'http://127.0.0.1:3000/'

{"code":0,"msg":"Real Ip is 代理IP"}
```

# Why?

我们先查根本原因(*Root Cause*)，

方案1是使用了http协议，但协议不一定会被遵守，可以伪造头信息，

方案2因为使用了代理，导致tcp建立的连接实际是代理的ip

# How to solve

因为我们这里必须要使用反向代理，所以方案2不能直接使用。

这时候我们就要对nginx做配置，把X-Forwarded-For直接改为remote_addr，如下

```Bash
# remote_addr 就是tcp连接的ip
proxy_set_header X-Forwarded-For $remote_addr;
```

或者直接自定义一个头参数**X-Real-Ip**，通过获取X-Real-Ip来获取ip

```Bash
proxy_set_header X-Real-Ip $remote_addr;
```

因为我们还要兼容我们本地测试，所以还是要把方案一方案二结合起来，才是最佳实践。

```JavaScript
function getClientIp(req) {
  /*
    1. 先通过x-forwarded-for获取
    2. 没有就用remoteAddress
  */
  
  var forwardedIpsStr = req.header("x-forwarded-for");
  var ip = "";

  if (forwardedIpsStr) {
    ip = forwardedIps = forwardedIpsStr.split(",")[0];
  };
  
  if(!ip){
    // remoteAddress is "::ffff:127.0.0.1"
    // ::ffff: 是IPV6相关
    ip = req.socket.remoteAddress.split(':')[3];
    console.log(ip);
  };

  return ip;
}
```

# 综上

1. 修改nginx配置

1. 综合上述两个方案