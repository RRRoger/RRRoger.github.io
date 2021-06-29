# ELK操作日志管理系统探索

> ![](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/elk.png)
>
> 官方demo: https://demo.elastic.co/app/discover

# 一、背景

当前odoo系统与各个系统之间的接口交互越来越频繁, 

在odoo的业务数据库里记录的日志越来越多(***与自动化工站的日志就有100w条***), 

占用的相当多的资源,并且日志查询也很缓慢,

所以想用`ELK`来统一管理各个系统的之间的`接口日志`以及`操作日志`

# 二、ELK介绍

`ELK`是对`Elasticsearch`、`Logstash`、`Kibana`整合平台的简称。在日常的运维工作中，要实时监控服务器的业务、系统和硬件状态，除了使用监控之外，还需要搜集大量的日志来进行分析。但是在面对海量的服务器和集群时，通过单台登录查询的方式显然是不可能的，对于不同时间段和集群日志的分析仅仅通过简单的脚本来统计也是难以实现。ELK日志平台通过日志搜集，查询检索和前端展示的方式帮我们实现了这样的功能。

`Elasticsearch`: 提供了一个分布式多用户能力的全文搜索引擎

`Logstash`: 一款强大的数据处理工具，可以实现数据传输、格式处理、格式化输出
数据输入、数据加工(如过滤，改写等)以及数据输出

`Kibana`: 一个针对Elasticsearch的开源分析及可视化平台
搜索、查看存储在Elasticsearch索引中的数据
通过各种图表进行高级数据分析及展示

![image-20210616103954832](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20210616103954832.png)

![image-20210616142808879](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20210616142808879.png)

# 三、使用ELK的优势

- 免费且开源
- 应用广泛口碑好
- 解耦, 减轻数据库存储与查询压力
- ELK支持强大的查询功能, 可以更快的定位到日志
  - [Kibana中KQL的使用](https://blog.wj2015.com/2020/08/26/kibana%E4%B8%ADkql%E7%9A%84%E4%BD%BF%E7%94%A8/)
  - [KQL查询语言](https://docs.microsoft.com/zh-cn/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference)
  - [KQL 快速参考](https://docs.microsoft.com/zh-cn/azure/data-explorer/kql-quick-reference)
- 整合各个环境的接口交互日志, 方便统一管理

# 四、日志(***包括但不限于***)

- SAP与odoo之间的接口日志 ***先行探索***
- Odoo与自动化工站之间的接口日志
- SAP与OA之间的接口日志
- Odoo与工站客户端之间的接口日志
- ... 以后的其他系统

# 五、以下是对应的需求细节

- **日志格式**: 
  - 统一用`json`存储
- **存入es后的index索引格式: **
  - 参照日志json格式
- **每天的日志量: **
  - `较大估算`每天会有**10M**左右的日志数据(**10±kb/个 * 1024个/天**)
- **日志保存时间**: 
  - 3年 (*在没有性能和磁盘空间的压力下, 希望能更久*)
- **是否允许短时日志数据丢失**: 
  - 允许

# 六、日志内容

### 基本构成

| Item              | Type In ES | index  | Description   | Data Type | e.g. |
| ----------------- | ------------- | ------------- | ----------------- | ----------------- | ----------------- |
| 时间戳 | @timestamp |  | @timestamp | UTC时间戳 | 2021-06-08T20:08:07.481Z |
| 名称 | keyword | true | name | String | SAP工单同步接口 |
| 客户端ip | keyword | true | client_ip | String | 172.0.0.1; |
| 环境/租户 | keyword | true | tenant | String | odoo-pro; odoo-sit |
| 类型          | keyword   | true      | type          | String | sap_odoo_api; odoo_sap_api |
| 等级 | keyword | true | level | String | `INFO`, `WARNING`, `ERROR`, `DEBUG`... |
| 操作人 | keyword | true | operator | String | Admin \| 陈鹏 |
| 方法         | keyword  | true     | method     | String | /a/b/c \|  ABC |
| 请求报文      | text  |       | main_data | String | {"a":1, "b": 2} \| plain text |
| 返回报文      | text  |       | response | String | {"a":1, "b": 2} \| plain text |
| 调用时间      | keyword |   | call_time     | String | 2021-06-08 20:08:07 |
| 成功/失败 | keyword |  | success       | Boolean | true / false |

![image-20210610100207028](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20210610100207028.png)

### 示例

- 示例1:
  - `用户A` 在 ` 正式使用环境` 于 `2021年06月10日09:22:44` 在 `Sap4Hana` 向 `Odoo系统` `推送` `3个物料` 分别是 A,B,C, 并且推送成功了

- 示例2:
  - `员工A` 在 `odoo正式环境` 于 `2021年06月10日09:22:44` 在 `odoo-pro` `使用扫码过站` `扫描了2台雷达` 分别是 ARES-001;ARES-002 并且扫描成功了

- 示例2是可以拓展到这个日志系统里来的

### Data 示例

```json
// 原始json

{"client_ip": "127.0.0.1", "@timestamp": "2021-06-16T03:13:38.751Z", "call_time": "2021-06-16 11:13:38", "operator": "Admin", "response": {"msg": "current_date_time 请在 18000 秒以内!!", "success": false}, "tenant": "odoo-pro", "success": false, "level": "INFO", "main_data": {"current_date_time": "20210608151422", "workorders": [{"plan_qty": "2.000 ", "product_line": 10, "work_lines": [{"send_location": "A201", "parent_product_code": "000000029100020000", "into_workorder": "", "line_no": "0001", "workcenter": "JC", "scrap_rate": "0.00 ", "product_qty": "2.000 ", "move_type": "531", "product_code": 29003510000, "unit": "ST"}], "end_date": 20210624, "routine_code": 50000090, "workorder_no": "R11000002553", "routines": [{"work_type": "ZP01", "name": "雷达整机工站测试", "produce_location": "镜筒组装", "sequence": "0010", "line_no": "0010", "station_code": "C18", "note": "雷达整机工站测试"}, {"work_type": "ZP01", "name": "雷达整机路测", "produce_location": "道路测试", "sequence": "0020", "line_no": "0020", "station_code": "C23", "note": "雷达整机路测"}, {"work_type": "ZP02", "name": "雷达整机测试组出库", "produce_location": "镜筒组装", "sequence": "0030", "line_no": "0030", "station_code": "C18", "note": "雷达整机测试组出库"}], "factory_code": 1000, "workcenter": "JCH", "production_manager_desc": "成品-机械雷达", "create_user": "HS360", "production_version": 1130, "production_manager": 107, "routine_version": 1, "product_code": 29100020000, "type": "ZP01", "start_date": 20210623, "unit": "ST", "production_version_desc": "整机测试"}], "md5": "bb31728cc0adf3a9ab780d62cd64cc86"}, "type": "sap-odoo-api", "method": "/webapi/workorder/sync"}



// 格式化后的json
{
    "client_ip": "127.0.0.1",
    "@timestamp": "2021-06-16T03:13:38.751Z",
    "call_time": "2021-06-16 11:13:38",
    "operator": "Admin",
    "response": {
        "msg": "current_date_time 请在 18000 秒以内!!",
        "success": false
    },
    "tenant": "odoo-pro",
    "success": false,
    "level": "INFO",
    "main_data": {
        "current_date_time": "20210608151422",
        "workorders": [
            {
                "plan_qty": "2.000 ",
                "product_line": 10,
                "work_lines": [
                    {
                        "send_location": "A201",
                        "parent_product_code": "000000029100020000",
                        "into_workorder": "",
                        "line_no": "0001",
                        "workcenter": "JC",
                        "scrap_rate": "0.00 ",
                        "product_qty": "2.000 ",
                        "move_type": "531",
                        "product_code": 29003510000,
                        "unit": "ST"
                    }
                ],
                "end_date": 20210624,
                "routine_code": 50000090,
                "workorder_no": "R11000002553",
                "routines": [
                    {
                        "work_type": "ZP01",
                        "name": "雷达整机工站测试",
                        "produce_location": "镜筒组装",
                        "sequence": "0010",
                        "line_no": "0010",
                        "station_code": "C18",
                        "note": "雷达整机工站测试"
                    },
                    {
                        "work_type": "ZP01",
                        "name": "雷达整机路测",
                        "produce_location": "道路测试",
                        "sequence": "0020",
                        "line_no": "0020",
                        "station_code": "C23",
                        "note": "雷达整机路测"
                    },
                    {
                        "work_type": "ZP02",
                        "name": "雷达整机测试组出库",
                        "produce_location": "镜筒组装",
                        "sequence": "0030",
                        "line_no": "0030",
                        "station_code": "C18",
                        "note": "雷达整机测试组出库"
                    }
                ],
                "factory_code": 1000,
                "workcenter": "JCH",
                "production_manager_desc": "成品-机械雷达",
                "create_user": "HS360",
                "production_version": 1130,
                "production_manager": 107,
                "routine_version": 1,
                "product_code": 29100020000,
                "type": "ZP01",
                "start_date": 20210623,
                "unit": "ST",
                "production_version_desc": "整机测试"
            }
        ],
        "md5": "bb31728cc0adf3a9ab780d62cd64cc86"
    },
    "type": "sap-odoo-api",
    "method": "/webapi/workorder/sync"
}
```

## PS

### 1. ELK抓取日志方式

> 以下'应用'指sap,oa,sf,crm这些应用

有两种方式去记录日志。

- 由应用主动推送日志信息
- 由ELK拉取各个应用服务器的日志文件进行解析


#### 1) 第一种方式取决于这些应用是否支持写代码，通过接口主动向ELK发数据。

- 优点：只关注需要记录日志的功能模块，日志比较集中
- 缺点：需要写对应的推送代码


#### 2) 第二种方式取决于ELK是否可以获取应用的日志文件。

- 优点：代码量少或者无
- 缺点：日志文件较大，需对日志进行清洗过滤解析，过程繁琐。

#### 总结: 各个应用能否记录日志，取决于该应用支不支持编码或者能不能拿到日志文件

:point_down:
