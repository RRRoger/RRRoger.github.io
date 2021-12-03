# 若依框架(前后端分析版本)

>   https://gitee.com/y_project/RuoYi-Vue

## 技术栈

-   数据库
    -   Mysql
    -   redis
-   前端
    -   [Vue](https://cn.vuejs.org/index.html)
    -   [Vuex](https://vuex.vuejs.org/zh/)
    -   [Element UI](https://element.eleme.io/#/zh-CN)
    -   [Axios](https://axios-http.com/)
        -   Axios 是可以发出 http 请求的 JavaScript 库，在 浏览器 和 node.js 环境中都可以运行。
    -   [SASS](https://sass-lang.com/documentation/js-api)
        -   一个 css 的预编译工具
    -   [Quill](https://quilljs.com/)
        -   Quill是一个所见即所得的富文本编辑器，拥有很好的交互体验，目前在github上的星数是编辑器中最高的。 用户可以在基础上进行自定义的开发，来完成自己的编辑器功能。
-   后端
    -   Spring Boot
    -   Sprint Security
    -   MyBatis
    -   [JWT](https://jwt.io/) 
        -   JSON Web Token（缩写 JWT）是目前最流行的跨域认证解决方案，本文介绍它的原理和用法。
        -   https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html
    -   Fastjson
        -   Fastjson 是一个 Java 库，可以将 Java 对象转换为 JSON 格式，当然它也可以将 JSON 字符串转换为 Java 对象。
    -   [Druid](http://druid.io)
        -   "Druid是Java语言中最好的数据库连接池。"

## Features

1.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。
2.  部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。
3.  **岗位管理**：配置系统用户所属担任职务。
4.  菜单管理：配置系统菜单，操作权限，按钮权限标识等。
5.  **角色管理**：角色菜单权限分配、设置角色按机构进行数据范围权限划分。
6.  **字典管理**：对系统中经常使用的一些较为固定的数据进行维护。
7.  **参数管理**：对系统动态配置常用参数。
8.  通知公告：系统通知公告信息发布维护。
9.  **操作日志**：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
10.  登录日志：系统登录日志记录查询包含登录异常。
11.  在线用户：当前系统中活跃用户状态监控。
12.  **定时任务**：在线（添加、修改、删除)任务调度包含执行结果日志。
13.  代码生成：前后端代码的生成（java、html、xml、sql）支持CRUD下载 。
14.  系统接口：根据业务代码自动生成相关的api接口文档。
15.  服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。
16.  缓存监控：对系统的缓存信息查询，命令统计等。
17.  在线构建器：拖动表单元素生成相应的HTML代码。
18.  连接池监视：监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。

## 简介

-   直接使用,减少工作量
-   学习优秀开源项目底层的编程思想,设计思路,提高自己的编程能力
-   3个项目版本:
    -   前后端不分离: https://gitee.com/y_project/RuoYi
    -   **前后端分离**: https://gitee.com/y_project/RuoYi-Vue
    -   微服务: https://gitee.com/y_project/RuoYi-Cloud
-   基础: Spring boot + vue
-   环境要求
    -   JDK 1.8+
    -   Mysql
    -   Redis
    -   Maven
    -   Vue

## 安装步骤

-   下载安装IDEA
-   安装Java JDK1.8
-   安装mysql
-   安装redis
    -   `redis-server &`
-   手动安装maven
    -   下载 && 解压 && 添加环境变量
-   下载并运行 gitee下载源码
    -   https://gitee.com/y_project/RuoYi-Vue
-   **New Project Get From Version Control**

![image-20211201190056267](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20211201190056267.png)

-   配置redis和mysql

```bash
# mysql
/ruoyi-admin/src/main/resources/application-druid.yml

# redis
/ruoyi-admin/src/main/resources/application.yml
```

-   创建数据库

```sql
CREATE DATABASE `ry-vue` CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ry-vue`;
```

-   执行sql文件载入数据

```sql
source /Users/chenpeng/IdeaProjects/RuoYi-Vue/sql/quartz.sql
source /Users/chenpeng/IdeaProjects/RuoYi-Vue/sql/ry_20210908.sql
```

-   项目结构

```bash
.
├── LICENSE
├── README.md
├── bin
├── doc
├── dump.rdb
├── pom.xml
├── ruoyi-admin
├── ruoyi-common
├── ruoyi-framework
├── ruoyi-generator
├── ruoyi-quartz
├── ruoyi-system
├── ruoyi-ui                     # 前端代码目录
│   ├── bin
│   ├── build
│   ├── node_modules
│   ├── public
│   └── src
└── sql

```

-   修改日志存放路径

```
/ruoyi-admin/src/main/resources/logback.xml

把 /home/ruoyi -> /Users/chenpeng
```

-   启动后台 port:8080

-   启动前端 port:80

```bash
cd /Users/chenpeng/IdeaProjects/RuoYi-Vue/ruoyi-ui
npm install --registry=https://registry.npm.taobao.org
npm run dev
```

-   访问[http://localhost:8080](http://localhost:8080)

![WechatIMG31486](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/WechatIMG31486.png)

-   访问[http://localhost:1024](http://localhost:1024)

![WechatIMG31488](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/WechatIMG31488.png)

---

---

---

### 通过反向代理解决跨域问题

![image-20211201193049743](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20211201193049743.png)


---
### 数据表ER图

>   权限组呢?

![image-20211202140756191](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20211202140756191.png)

### 验证码方案

2+1?@3

-   2+1? -> 生成图片
-   3结合uuid 存到redis 2min 时效性

### 登录具体流程

-   后端
    -   校验验证码
    -   校验用户名密码
    -   生成token

### 异步线程池

使用异步任务管理器， 结合线程池，实现异步

```java
AsynvManager.me().execute(....)
```

-   记录日志
-   解耦

### 验证

-   使用Spring security

### 用户角色与权限

```bash
*:*:*  # 所有的权限

```

### 异步任务管理器

线程池原理

### 代码自动生成

<iframe src="//player.bilibili.com/player.html?aid=933941110&bvid=BV1HT4y1d7oA&cid=438883763&page=16" width="100%" height="450px" > </iframe>

```sql
use ry-Vue;

create table test_user(
    id int primary key auto_increment,
    name varchar(11),
    password varchar(11)
);
```



### 参考链接:

-   https://gitee.com/y_project/RuoYi-Vue
-   https://www.bilibili.com/video/BV1HT4y1d7oA



---

-   技术栈完备
    -   权限
-   开发模式
    -   