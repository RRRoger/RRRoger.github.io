# -*- coding: utf-8 -*-

import itertools
"""
    [] list列表   {}dict字典  ()tuple元组
"""
data=[
  {
    "priority": 10, 
    "delivery_order": "SFD1609160002", 
    "product_name": "Apple", 
    "delivery_date": "2016-09-16", 
    "dispatch_qty": 1.0
  }, 
  {
    "priority": 11, 
    "delivery_order": "SFD1609160002", 
    "product_name": "Apple", 
    "delivery_date": "2016-09-16", 
    "dispatch_qty": 2.0
  }, 
  {
    "priority": 11, 
    "delivery_order": "SFD1609160002", 
    "product_name": "Apple", 
    "delivery_date": "2016-09-16", 
    "dispatch_qty": 3.0
  }, 
  {
    "priority": 10, 
    "delivery_order": "SFD1609160003", 
    "product_name": "Apple", 
    "delivery_date": "2016-09-17", 
    "dispatch_qty": 4.0
  }, 
  {
    "priority": 11, 
    "delivery_order": "SFD1609160003", 
    "product_name": "Apple", 
    "delivery_date": "2016-09-17", 
    "dispatch_qty": 5.0
  }
]

sorted(data,key=lambda x:(x["delivery_date"],x["delivery_order"]))
        
a = itertools.groupby(data, key=lambda x: (x["delivery_date"],x["delivery_order"]))
b = dict([(str(g or ''), list(k)) for g, k in a])

# print  b
for m,n in b.items():
    
    print n
    print '========='

    
    

for i in range(8):
    print i 





# #分组
# res = dict([(str(g or ''), list(k)) for g, k in \
#   itertools.groupby(data, key=lambda x: x["delivery_order"])])
# a = []

# for k,v in res.items():
#   for i in range(0,len(v),3):
#       value = v[i:i+3]
#       a.append(value)
# print a



# list_res = [
# {'date': '2021-06-03', 'outer_code': '211121211225', 'product_id': 3928, 'laser_code': 'R01HLDJ580TE'},
#     {'date': '2021-06-03', 'outer_code': '211121211225', 'product_id': 3928, 'laser_code': 'R01HLDJ579TD'},
#     {'date': '2021-06-03', 'outer_code': '211121211221', 'product_id': 3926, 'laser_code': 'R01HLDJ576T5'},
#     {'date': '2021-06-03', 'outer_code': '211121211221', 'product_id': 3926, 'laser_code': 'R01HLDJ576T6'},
#     {'date': '2021-06-03', 'outer_code': '211121211222', 'product_id': 3926, 'laser_code': 'R01HLDJ576T7'},
#     {'date': '2021-06-03', 'outer_code': '211121211222', 'product_id': 3926, 'laser_code': 'R01HLDJ576T8'},
#     {'date': '2021-06-03', 'outer_code': '211121211223', 'product_id': 3927, 'laser_code': 'R01HLDJ576T9'},
#     {'date': '2021-06-03', 'outer_code': '211121211224', 'product_id': 3927, 'laser_code': 'R01HLDJ577TB'},
#     {'date': '2021-06-03', 'outer_code': '211121211224', 'product_id': 3927, 'laser_code': 'R01HLDJ578TC'},
#     {'date': '2021-06-03', 'outer_code': '211121211223', 'product_id': 3927, 'laser_code': 'R01HLDJ576TA'},
    
#     ]

# list_res.sort(key=lambda k: (k.get('product_id', 0), k.get('outer_code', 0)))

# print(list_res)

