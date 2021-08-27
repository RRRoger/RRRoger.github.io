# VACUUM [undone]

## 1. VACUUM

> 在一般的PostgreSQL 操作里，那些已经 DELETE 的行或者被 UPDATE 过后过时的行并没有从它们所属的表中物理删除； 在完成`VACUUM`之前它们仍然存在。因此有必要周期地运行`VACUUM`， 特别是在经常更新的表上。
>
> vacuum和相关的autovacuum进程是控制PostgreSQL由于mvcc机制导致膨胀的方法

```sql
VACUUM [FULL] [FREEZE] [VERBOSE] [table]

VACUUM [FULL] [FREEZE] [VERBOSE] ANALYZE
            [table [(column [, ...] )]]
```

### 参数

- `FULL`
  - 选择"完全"清理，它可以收回更多空间，并且需要**更长时间**和表上的排他锁。

- `FREEZE`
  - 指定 FREEZE 等价于参数 vacuum_freeze_min_age 设置为0的 VACUUM。

- `VERBOSE`
  - 为每个表**打印**一份详细的清理活动报告。

- `ANALYZE`
  - 更新优化器用以决定最有效执行一个查询的方法的**统计信息**。

- `TABLE`
  - 要清理的表的名称（可以有模式修饰）。缺省时是当前数据库中的所有表。

- `COLUMN`
  - 要分析的指定列的名称。缺省是所有列。

### 示例

清理当前数据库下的所有表：

```sql
VACUUM;
```

只清理一张特定的表：

```sql
VACUUM mytable;
```

清理当前数据库下的所有表同时为查询优化器收集统计信息：

```sql
VACUUM ANALYZE;
```

## 2. MVCC是什么？

> MVCC(***Multiversion concurrency control***)是指多版本并发控制,通俗的讲就是MVCC通过对数据进行**多版本保存**，根据比较版本号来控制数据是否展示，从而达到读取数据时无需加锁就可以实现事务的隔离性。

### MVCC常用实现方法

#### 一般MVCC有2种实现方法：

- 写新数据时，把旧数据**转移**到一个单独的地方，如回滚段中，其他人读数据时，**从回滚段**中把旧的数据读出来，如Oracle数据库和MySQL中的innodb引擎。
- 写新数据时，旧数据不删除，而是把新数据插入。PostgreSQL就是使用的这种实现方法。

#### PostgreSQL的MVCC实现方式优缺点

- 优点
  - 无论事务进行了多少操作，事务回滚可以立即完成
  - 数据可以进行很多更新，不必像Oracle和MySQL的**InnoDB**[^1]引擎那样需要经常保证回滚段不会被用完，也不会像oracle数据库那样经常遇到“ORA-1555”错误的困扰
- 缺点
  - 旧版本的数据需要清理。当然，PostgreSQL 9.x版本中已经增加了自动清理的辅助进程来定期清理
  - 旧版本的数据可能会导致查询需要扫描的数据块增多，从而导致查询变慢

### PostgreSQL中MVCC的具体实现

...

### 总结

为了保证事务的原子性和隔离性，**实现不同的隔离级别**，PostgreSQL引入了MVCC多版本机制，概括起就是：

- 通过元组的头部信息中的xmin，xmax以及t_infomask等信息来定义元组的版本
- 通过事务提交日志来判断当前数据库各个事务的运行状态
- 通过事务快照来记录当前数据库的事务总体状态
- 根据用户设置的隔离级别来判断获取事务快照的时间

如上文所讲，PostgreSQL的MVCC实现方法有利有弊。其中最直接的问题就是**表膨胀**，为了解决这个问题引入了AutoVacuum自动清理辅助进程，将MVCC带来的垃圾数据定期清理。

参考链接: 

- http://www.postgres.cn/docs/9.4/sql-vacuum.html
- http://mysql.taobao.org/monthly/2017/10/01/

[^1]: **InnoDB**是[MySQL](https://zh.wikipedia.org/wiki/MySQL)的数据库引擎之一，InnoDB的最大特色就是支持了[ACID](https://zh.wikipedia.org/wiki/ACID)兼容的[事务](https://zh.wikipedia.org/wiki/数据库事务)（Transaction）功能，类似于[PostgreSQL](https://zh.wikipedia.org/wiki/PostgreSQL)。

