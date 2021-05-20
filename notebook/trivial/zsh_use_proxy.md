# 让 Zsh 终端走代理

> 在 ~/.zshrc 配置文件中添加下面一段，
>
> 以后使用的时候输入 `proxy` 打开代理模式，
>
> 关闭代理时输入 `noproxy` 即可。

```bash
vim ~/.zshrc

# where proxy
proxy () {
  export http_proxy="http://127.0.0.1:7890"
  export https_proxy="http://127.0.0.1:7890"
  echo "HTTP Proxy on"
}

# where noproxy
noproxy () {
  unset http_proxy
  unset https_proxy
  echo "HTTP Proxy off"
}
```

我用的clash, 所以默认代理端口为7890，如果使用其他代理软件请注意修改端口。

