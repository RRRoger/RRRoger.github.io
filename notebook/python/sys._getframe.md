# Python sys._getframe

因代码需要封装了一个日志函数, 想记录当前被调用函数的**名称**，**所处模块**，以及**被调用代码行**，因此了解到`sys`的`_getframe`函数.

> `sys._getframe`([*depth*])[^链接1]
>
> 从调用堆栈返回一个对象结构。 如果给出了可选的整数 *depth*，则返回在堆栈顶部以下调用多次的对象。 如果它比调用堆栈更深，则会引发 `ValueError`。 *depth* 的默认值为零，返回调用堆栈顶部的结构。

- 演示环境：`python3.8`

```python
import sys

def test_func():
    caller = sys._getframe(1)
    file_name = caller.f_code.co_filename  # 获取调用函数名所在路径
    func_name = caller.f_code.co_name  # 获取调用函数名
    line_number = caller.f_lineno  # 获取调用函数行号
    print(f"被调用函数名路径: {file_name}")
    print(f"被调用函数名: {func_name}")
    print(f"被调用函数行号: {line_number}")
    
    cur_func = sys._getframe()
    file_name = cur_func.f_code.co_filename  # 获取调用函数名所在路径
    func_name = cur_func.f_code.co_name  # 获取调用函数名
    line_number = cur_func.f_lineno  # 获取调用函数行号; 结果为当前行
    print(f"当前函数名路径: {file_name}")
    print(f"当前函数名: {func_name}")
    print(f"当前函数行号: {line_number}")


def caller_func():
    test_func()

if __name__ == '__main__':
    caller_func()
```



### 参考链接

- [^链接1]: https://docs.python.org/3/library/sys.html#sys._getframe

- [^链接2]: https://docs.python.org/3/library/sys.html

