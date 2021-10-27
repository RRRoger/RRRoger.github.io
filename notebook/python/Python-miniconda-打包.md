# Python miniconda 打包

## 回顾

-   创建环境

```bash
conda create -n DjangoBlog python=3.8 -y
```

-   切换环境

```python
conda activate DjangoBlog
```

## 打包

>   使用`Conda-pack` 命令行工具，用于打包 conda 环境，其中包括该环境中安装的软件包的所有二进制文件。 
>
>   要安装 conda-pack，请确保您位于 root 或 base 环境中，以便 conda-pack 在子环境中可用。

### 安装`conda-pack`

-   使用**conda-forge**安装:

```bash
conda install -c conda-forge conda-pack
```

-   使用**PyPI**安装:

```bash
pip install conda-pack
```

### 打包一个环境

*使用上面DjangoBlog举例*

```bash
# 不指定输出文件, 则使用名称: DjangoBlog.tar.gz
conda pack -n DjangoBlog

# 指定输出名称
conda pack -n DjangoBlog -o MyDjangoBlog.tar.gz

# 选择指定的某个目录下的环境导出为 DjangoBlog.tar.gz
conda pack -p /explicit/path/to/DjangoBlog
```

### 使用包安装环境

```bash
# 新建指定目录
mkdir -p MyDjangoBlog

# 使用已经打的包 并指定目录
tar -xzf MyDjangoBlog.tar.gz -C MyDjangoBlog

# 使用命令测试python环境是否ok
./MyDjangoBlog/bin/python

# 使用目录的方式激活python环境
source MyDjangoBlog/bin/activate

# 运行python环境
(MyDjangoBlog) $ python

# 清除活动环境中的前缀。
# 注意，该命令也可以在不激活环境的情况下运行
# 只要机器上已经安装了某个版本的Python。
(MyDjangoBlog) $ conda-unpack
```

#### 参考链接:

-   https://zhuanlan.zhihu.com/p/87344422

