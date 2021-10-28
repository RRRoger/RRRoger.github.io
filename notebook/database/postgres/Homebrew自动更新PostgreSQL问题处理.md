# Homebrew自动更新PostgreSQL问题处理

>   今天想安装其他的库, 导致homebrew自动更新其他的工具包, 致使postgres出问题
>   
>   本次小事故收获是, 遇到问题先冷静面对, 看别人的帖子不要无脑复制粘贴

## 写在前面

#### Homebrew锁定不想更新的包

brew update 一次更新所有的包是非常方便。但有时候会担自动升级不希望更新的包。数据库就属于这一类，尤其是 PostgreSQL 跨 minor 版本升级都要迁移数据库的。

这时可用 brew pin 去锁定这个包，然后 brew update 就会略过它了。

```bash
brew list | grep postgresql # 查看你的应用版本 

brew list --pinned  # 查看pin列表

brew pin postgresql@13 # 固定版本

brew unpin postgresql@13 # 取消固定
```

## 问题描述

#### homebrew升级后的提示

```bash
==> Upgrading postgresql
  13.4 -> 14.0

==> Pouring postgresql-14.0.big_sur.bottle.tar.gz
==> Caveats
To migrate existing data from a previous major version of PostgreSQL run:
  brew postgresql-upgrade-database

This formula has created a default database cluster with:
  initdb --locale=C -E UTF-8 /usr/local/var/postgres
...
```

之前也遇到过类似的问题, 因为我已经备份了相关的数据库, 所以我就放任不管了

#### 启动postgres报错

```bash
waiting for server to start... FATAL: database files are incompatible with server
[58146] DETAIL: The data directory was initialized by PostgreSQL version 9.6, which is not compatible with this version
10.0.
 stop waiting
pg_ctl: could not start server
Examine the log output.
```

如果你也是这样的问题,那么可以继续往下看了.

## 解决方案

>    因为版本不一样, 这里不建议你复制我的代码, 建议手敲.

```bash
brew tap caskroom/versions # 或者 brew tap homebrew/cask-versions

# 此处是旧版本
# 如果你的版本不是 13 请执行 $brew search postgresql 选择对应的版本
brew install postgresql@13
```

#### 初始化14.0数据库(即brew更新后的数据库)

```bash
initdb /usr/local/var/postgres10.0 -E utf8
```

#### 执行 pg_upgrade, *建议手敲*

```bash
pg_upgrade -d /usr/local/var/postgres \
           -D /usr/local/var/postgres14.0 \
           -b /usr/local/Cellar/postgresql@13/13.4/bin \
           -B /usr/local/Cellar/postgresql/14.0/bin \
           -v
```

在一大堆的 ok 过后, 看到 **Upgrade Complete** 就说明安装成功了.

#### 重新加载服务

```bash
/usr/local/bin/pg_ctl -D /usr/local/var/postgres14.0 start
```

如果显示**server started**则表示成功

## 参考链接

-   https://juejin.cn/post/6844903504427876366