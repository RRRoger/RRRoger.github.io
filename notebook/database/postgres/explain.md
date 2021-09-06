# EXPLAIN 使用浅析

## Options:

-   `ANALYZE` 
    -   默认为FALSE
    -   选项为TRUE 会实际执行SQL，并获得相应的查询计划。
    -   如果优化一些修改数据的SQL 需要真实的执行但是不能影响现有的数据，可以放在一个事务中，分析完成后可以直接回滚。

-   `VERBOSE` 
    -   默认为FALSE
    -   选项为TRUE 会显示查询计划的附加信息。
    -   附加信息包括查询计划中每个节点（后面具体解释节点的含义）输出的列（Output），表的SCHEMA 信息，函数的SCHEMA 信息，表达式中列所属表的别名，被触发的触发器名称等。


-   `COSTS` 
    -   默认为TRUE
    -   选项为TRUE 会显示每个计划节点的预估启动代价（找到第一个符合条件的结果的代价）和总代价，以及预估行数和每行宽度。


-   `BUFFERS` 
    -   当ANALYZE 选项打开时, 默认为FALSE
    -   选项为TRUE 会显示关于缓存的使用信息。
    -   缓冲区信息包括共享块（常规表或者索引块）、本地块（临时表或者索引块）和临时块（排序或者哈希等涉及到的短期存在的数据块）的命中块数，更新块数，挤出块数。


-   `TIMING` 
    -   当ANALYZE 选项打开时, 默认为TRUE
    -   选项为TRUE 会显示每个计划节点的实际启动时间和总的执行时间。
    -   因为对于一些系统来说，获取系统时间需要比较大的代价，如果只需要准确的返回行数，而不需要准确的时间，可以把该参数关闭。


-   `SUMMARY` 
    -   当ANALYZE 选项打开时, 默认为TRUE
    -   选项为TRUE 会在查询计划后面输出总结信息，例如查询计划生成的时间和查询计划执行的时间。


-   `FORMAT` 
    -   默认为TEXT
    -   指定输出格式。各个格式输出的内容都是相同的，其中XML | JSON | YAML 更有利于我们通过程序解析SQL 语句的查询计划。

---

## explain 结果 cost、rows、width 的说明

> cost=0.00…234.00 rows=10000 width=74

##### cost=0.00…234.00

- 第一个数字 0.00 表示启动的成本，返回第一行需要多少 cost 值。  
- 第二个数字 234.00 表示返回所有数据的成本。
- cost 基于如下的一些规则计算出的数字(默认)：  
    - 顺序扫描一个块，cost的值为 1  
    - 随机扫描一个块，cost的值为 4  
    - 处理一个数据行的CPU代价，cost的值为 0.01  
    - 处理一个索引行的CPU代价，cost的值为 0.005  
    - 每个操作的CPU代价为 0.0025

##### rows=10000
表示会返回 10000行。

##### width=74
表示每行**平均宽度**为74字节。

## actual time、rows、loops说明
> actual time=0.049..0.049 rows=100 loops=1

##### actual time=0.049..0.049

- 表示此步骤的开始时间是0.049,结束时间0.049,单位为毫秒,因此此实际执行时间是0,实际时间是每次迭代的平均值,可以将值乘以循环次数以获得真实的执行时间

##### loops=1
- 表示索引扫描被执行了1次

##### rows=100

- 表示返回了100行

---

## 参考链接

- 链接1: http://www.postgres.cn/docs/9.5/using-explain.html
- 链接2: http://mysql.taobao.org/monthly/2018/11/06
- 链接3: https://aiolos123.gitee.io/blog/2020/01/10/how-to-use-explain-in-pgsql/
- 链接4: https://blog.csdn.net/ctypyb2002/article/details/109449934
- **链接5**: https://www.zou8944.com/archives/postgresql-yi-wen-kan-dong-explain