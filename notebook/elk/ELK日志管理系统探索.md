# ELK操作日志管理系统探索

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

# 三、使用ELK的优势

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

| Item              | index  | Description   | Data Type | e.g. |
| ----------------- | ------------- | ------------- | ----------------- | ----------------- |
| 时间戳 |  | @timestamp | Time String | 2021-06-08T20:08:07.481Z |
| 用户ip地址 | true | ip_address | ip | 172.0.0.1 |
| 环境/租户 | true | tenant | String | odoo-pro; odoo-sit |
| 类型          | true      | type          | String | sap_odoo_api; odoo_sap_api; oa_odoo_api |
| 操作人 | true | operator | String | Admin \| 陈鹏 |
| 方法         | true     | method     | String | /a/b/c \|  ABC |
| 请求报文      |       | main_data | String | {"a":1, "b": 2} \| plain text |
| 返回报文      |       | response | String | {"a":1, "b": 2} \| plain text |
| 调用时间      | true  | call_time     | String | 2021-06-08 20:08:07 |
| 成功/失败 |  | success       | Boolean | True / False |

![image-20210610100207028](https://cdn.jsdelivr.net/gh/ihatebeans/images@main/img/image-20210610100207028.png)

### 示例

- 示例1:
  - `用户A` 在 ` 正式使用环境` 于 `2021年06月10日09:22:44` 在 `Sap4Hana` 向 `Odoo系统` `推送` `3个物料` 分别是 A,B,C, 并且推送成功了

- 示例2:
  - `员工A` 在 `odoo正式环境` 于 `2021年06月10日09:22:44` 在 `odoo-pro` `使用扫码过站` `扫描了2台雷达` 分别是 ARES-001;ARES-002 并且扫描成功了

- 示例2是可以拓展到这个日志系统里来的

### Data 示例

```json
# 原始json

{"success": true, "response": {"unsynced_list": [], "synced_list": [{"product_code": "Cp_test"}], "success": true, "msg": "全部同步成功"}, "operator": "Admin", "@timestamp": "2021-06-10T02:52:37.100Z", "main_data": {"current_date_time": "20210610101522", "products": [{"in_check_flag": "X", "tracking": "none", "name": "陈鹏测试", "mpn": "mpn", "product_group_code": "8990", "specification": "规格描述123", "old_product_code": "00013246564", "product_des": "物料长文本描述", "default_code": "Cp_test", "uom_code": "U001", "product_type_code": "Z001", "manufacturer": "制造商"}], "md5": "088976aa554f7992ab6b9d9c40964bb1"}, "type": "sap-odoo-api", "method": "/webapi/product/sync", "tenant": "odoo-pro", "call_time": "2021-06-10 10:52:37"}



# 格式化后的json
{
    "success": true,
    "response": {
        "unsynced_list": [],
        "synced_list": [
            {
                "product_code": "Cp_test"
            }
        ],
        "success": true,
        "msg": "全部同步成功"
    },
    "operator": "Admin",
    "@timestamp": "2021-06-10T02:52:37.100Z",
    "main_data": {
        "current_date_time": "20210610101522",
        "products": [
            {
                "in_check_flag": "X",
                "tracking": "none",
                "name": "陈鹏测试",
                "mpn": "mpn",
                "product_group_code": "8990",
                "specification": "规格描述123",
                "old_product_code": "00013246564",
                "product_des": "物料长文本描述",
                "default_code": "Cp_test",
                "uom_code": "U001",
                "product_type_code": "Z001",
                "manufacturer": "制造商"
            }
        ],
        "md5": "088976aa554f7992ab6b9d9c40964bb1"
    },
    "type": "sap-odoo-api",
    "method": "/webapi/product/sync",
    "tenant": "odoo-pro",
    "call_time": "2021-06-10 10:52:37"
}
```



