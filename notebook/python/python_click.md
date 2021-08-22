

# Python Click 介绍

> 最近发现一个非常nice的python库: `Click`, 对热衷于写脚本的"Script Kid"非常友好.
>
> *可以更方便的编写带有参数脚本*.

- 参考链接： 
  - https://click-docs-zh-cn.readthedocs.io/zh/latest/
- 演示环境：
  - `Python3.x`

## What is click?

> """Click 是一个利用很少的代码以可组合的方式创造优雅命令行工具接口的 Python 库。 它是高度可配置的，但却有合理默认值的“命令行接口创建工具”。"""

- 通常我们执行`script.py`文件, 后面跟参数我们是这么做的.

```bash
python script.py --count=3 --src-dir==/dir
```

```python
import sys

if __name__ == '__main__':
    # arg1 is "--count=3"
    arg1 = sys.args[1]
    
    # arg2 is "--src-dir==/dir"
    arg2 = sys.args[1]
```

- 如果我们使用click方式, 可读性更高, 使用也更方便, demo如下:

```python
import click

help_c = "帮助信息, 描述这个脚本的目的."

@click.command()
@click.help_option("-h", "--help", help=help_c)
@click.option("-c", "--count", "count", type=str)
@click.option("-s", "--src-dir", "src_dir", help="源目录", type=str, required=True)
@click.option("-o", "--out-dir", "out_dir", help="目标目录", type=str)
def main(count, src_dir, out_dir):
    """Doc, 这里的文本也会显示在 --help 里"""
		print(count, src_dir, out_dir)


if __name__ == '__main__':
    main()
```

- 可以使用`python script.py -h`来查阅帮助文档, 显示如下:

```bash
Usage: script.py [OPTIONS]

  Doc, 这里的文本也会显示在 --help 里

Options:
  -h, --help          帮助信息, 描述这个脚本的目的.
  -c, --count TEXT
  -s, --src-dir TEXT  源目录  [required]
  -o, --out-dir TEXT  目标目录
```

## Installation

```bash
pip install click
```

## Usage

- 使用 `click.command` 表示 `main` 是对命令的处理逻辑
- 使用 `click.help_option` 来指定帮助信息
- 使用 `click.option` 来定义参数选项
  - **type**选项:
    -  **str**: 字符串类型参数
    - **int**: 整数类型参数
    - **float**: 浮点数类型参数
    - **bool**: 布尔类型参数, `1`, `yes`, `y` 和 `true`都为真
  - **help**: 参数说明
  - **required**: 是否必填
  - **default**: 默认值
  - **is_flag**:表示一个标记参数; 如其中含有此参数, 则表示真,相较于**bool**少加一个值

## Other

### 1. 帮助文档的排版问题

```python
# merge_pdf.py

help="""
Merge PDF / 合并pdf文件
Author: Roger;
Python Version: python 3.7+;
Python Libraries:
    PyPDF2
    click
"""
@click.help_option("-h", "--help", help=help)
```

输出如下, 换行存在问题

```bash
Usage: merge_pdf.py [OPTIONS]

  Merge PDF

Options:
  -h, --help        Merge PDF / 合并pdf文件 Author: Roger; Python Version: python
                    3.7+; Python Libraries:     PyPDF2     click

  -dir, --dir TEXT  目标路径.  [required]
```

解决方案, 在每个段落前加个`\b`:

```python
# merge_pdf.py

help="""
\b
Merge PDF / 合并pdf文件
Author: Roger;
Python Version: python 3.7+;
Python Libraries:
    PyPDF2
    click
"""
@click.help_option("-h", "--help", help=help)
```

输出如下:

```bash
Usage: merge_pdf.py [OPTIONS]

  Merge PDF

Options:
  -h, --help        Merge PDF / 合并pdf文件
                    Author: Roger;
                    Python Version: python 3.7+;
                    Python Libraries:
                        PyPDF2
                        click

  -dir, --dir TEXT  目标路径.  [required]
```

