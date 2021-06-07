# pymongo使用

> pip install pymongo
>
> `import pymongo`

## 1. 创建数据库

```python
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_test"]
```

## 2. 判断数据库存在

```python
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
if "db_test" in dblist: print("数据库已存在！")
```

## 3. ...

