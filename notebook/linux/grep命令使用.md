# Linux grep 命令

### 最常用的参数

-   **-n 或 --line-number** : 在显示符合样式的那一行之前，标示出该行的列数编号
-   **-c 或 --count** : 返回符合样式的列数。
-   **-E 或 --extended-regexp** : 将样式为延伸的正则表达式来使用。
-   **-v 或 --invert-match** : 显示不包含匹配文本的所有行。
-   **-i 或 --ignore-case** : 忽略字符大小写的差别。
-   **显示上下文**
    -   **-B<显示行数>** : 除了显示符合样式的那一行之外，并显示该行之前的内容。
    -   **-C<显示行数> ** : 除了显示符合样式的那一行之外，并显示该行之前后的内容。

```bash
# 搜索test.py文件
# -i: 不区分大小写匹配`print`的内容
# -B 1 -C 1: 并显示上下隔一行的文本
# -n: 并显示行号

grep -n -i -B 1 -C 1 'print' test.py

# 或者

cat test.py | grep -n -i -B 1 -C 1 'print'
```

### 正则表达式

正则表达式分为基本正则表达式和扩展正则表达式

##### 扩展正则表达式

```bash
# 匹配gd，god
grep -nE 'go?d' test.py

# 匹配god，good，goood等等字符串
grep -nE 'go+d' test.py

# 搜寻good或者glad
grep -nE 'g(oo|la)' test.py

# 匹配god或者good
grep -nE 'god|good' test.py
```





