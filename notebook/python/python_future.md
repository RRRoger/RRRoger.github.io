# Python Future Usage

> 用法：只能放置于当前运行代码片段的最开头。
>
> 否则会报错 `SyntaxError: from __future__ imports must occur at the beginning of the file`
>
> 最常用的是`division`;`unicode_literals`这两个

## 0. 列出所有`__future__ `的特性

```python
>>> from pprint import pprint
>>> import __future__
>>> pprint(__future__.all_feature_names)
['nested_scopes',
 'generators',
 'division',
 'absolute_import',
 'with_statement',
 'print_function',
 'unicode_literals']
```

## 1. division

> 整数除法

```python
# Python 2.7.15
>>> from __future__ import division
>>> 2 / 3
0.6666666666666666
```

## 2. unicode_literals

> 兼容编码

```python
# Python 2.7.15
>>> from __future__ import unicode_literals
>>> a = u"中文"
>>> b = "中文"
>>> a
u'\u4e2d\u6587'
>>> b
u'\u4e2d\u6587'
>>> a == b
True
```

## 3. print_function

> 打印函数, py2里print不是一个函数, 导入后print将会是一个函数; 具体函数特性

```python
>>> from __future__ import print_function
>>> print "hello, world"
  File "<stdin>", line 1
    print "hello, world"
                       ^
SyntaxError: invalid syntax
>>>
```

## 4. absolute_import

> 这是一个在py2.x中导入3.x的导入特性的语句, 是为了区分出绝对导入和相对导入
>
> 声明为绝对引用。因为在Python 2.4或之前默认是相对引用，即先在本目录下寻找模块。但是如果本目录中有模块名与系统(sys.path)模块同名冲突，而想要引用的是系统模块时，该声明就能够起作用了。这样你调用import string时引入的就是系统的标准string.py，调用from pkg import string来引入当前目录的string.py

## 5. nested_scopes

> 这个是修改嵌套函数或lambda函数中变量的搜索顺序，
>
> 从`当前函数命名空间->模块命名空间`的顺序更改为了`当前函数命名空间->父函数命名空间->模块命名空间`,
>
> python2.7.5中默认使用

## 6. generators

> 生成器，对应yield的语法，python2.7.5中默认使用

## 7. with_statement

> 是使用with关键字，python2.7.5是默认使用
