# 让 Zsh 终端走代理

> 在 ~/.zshrc 配置文件中添加下面一段，
> 
> 以后使用的时候输入 `proxy` 打开代理模式，
> 
> 关闭代理时输入 `noproxy` 即可。

```bash
vim ~/.zshrc

# cmd: set proxy
proxy () {
  export http_proxy="http://127.0.0.1:7890"
  export https_proxy="http://127.0.0.1:7890"
  echo "HTTP Proxy On."
}

# cmd: unset proxy
noproxy () {
  unset http_proxy
  unset https_proxy
  echo "HTTP Proxy Off."
}

# cmd: show proxy
show_proxy () {
  echo "http_proxy: $http_proxy"
  echo "https_proxy: $https_proxy"
}

# 默认走代理, 注释掉的话需要手动打开代理模式
proxy
```



我用的**clash**, 所以默认代理端口为`7890`，如果使用其他代理软件请注意修改端口。


