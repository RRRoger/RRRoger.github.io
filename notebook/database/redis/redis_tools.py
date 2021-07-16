# -*- encoding: utf-8 -*-
##############################################################################
#
#    Redis Connections Pool
#    Author: Roger
#
##############################################################################

try:
    import redis
except ImportError:
    _logger.error("[Hesai Main] No module named redis")

SESSION_TIMEOUT = 60 * 60 * 24 * 7  # 1 weeks in seconds


# 单例模式
def singleton(cls):
    _instance = {}
    def inner(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return inner

@singleton
class RedisWrapper(object):

    def __init__(self, host="localhost", port=6379, password=None):
        pool = redis.ConnectionPool(
            host=host,
            port=port,
            password=password
        )
        self.conn = redis.Redis(connection_pool=pool)

    def set(self, key, value, time=None):
        """
            #非空即真非0即真
        :param key:
        :param value:
        :param time: expire time
        :return:
        """
        if not time:
            time = SESSION_TIMEOUT
        return self.conn.setex(name=key, time=time, value=value)

    def get(self, key):
        """
        :param key:
        :return:
        """
        return self.conn.get(key)#.decode()

    def delete(self, key):
        """
        :param key:
        :return:
        """
        return self.conn.delete(key)

    def set_hash(self, name, key, value):
        """
        :param name:
        :param key:
        :param value:
        :return:
        """
        res = self.conn.hset(name, key, value)
        return res

    def get_hash(self, name, key=None):
        """
            判断key是否我为空，不为空，获取指定name内的某个key的value; 为空则获取name对应的所有value
        :param name:
        :param key:
        :return:
        """
        if key:
            res = self.conn.hget(name, key)
        else:
            res = self.conn.hgetall(name)
        return res

    def del_hash(self, name, key=None):
        """
        :param name:
        :param key:
        :return:
        """
        return self.conn.hdel(name, key=key)

    def ping(self):
        return self.conn.ping()

    def lpush(self, name, value):
        # 将一个或多个值插入到已存在的列表头部，列表不存在时操作无效。
        return self.conn.lpush(name, value)

    def rpush(self, name, value):
        #
        return self.conn.rpush(name, value)

    def blpop(self, keys, timeout=0):
        # Lpop 命令用于移除并返回列表的第一个元素。
        return self.conn.blpop(keys=keys, timeout=timeout)

    def brpop(self, keys, timeout=0):
        # Rpop 命令用于移除并返回列表的最后一个元素。
        return self.conn.brpop(keys=keys, timeout=timeout)

    def lrange(self, name, start, end):
        return self.conn.lrange(name, start, end)


if __name__ == "__main__":
    KEY = "KEY"
    VALUE = "Value"

    rw = RedisWrapper("172.16.1.36", 6379, "odookNcpe473")

    # assert rw.ping()
    # assert rw.set(KEY, VALUE)
    # assert rw.get(KEY) == VALUE
    # assert rw.delete(KEY)
    #
    # rw2 = RedisWrapper()
    # print(id(rw))
    # print(id(rw2))
    # assert id(rw) == id(rw2)

    # print(rw.get("e56419f4-d967-4b1f-bf6d-febdc2f14a66"))

    data = """{
        "name": "创建交货单",
        "@timestamp": "2021-07-16T06:21:11.641Z",
        "operator": "Bot",
        "tenant": "roger-localhost",
        "call_time": "2021-07-16 14:21:11",
        "level": "INFO",
        "main_data": "",
        "type": "sap-odoo-api",
        "response": "{\"msg\":\"系统错误: 'unicode' object has no attribute 'get'\",\"success\":false}",
        "success": false,
        "client_ip": "127.0.0.1",
        "method": "/webapi/create/tracker_schedule"
    }"""

    rw.lpush("api_log", data)


