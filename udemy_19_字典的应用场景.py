# 将多个字典放在一个列表中,在进行遍历
card_list = [
    {"name":"zhangsan",
     "age":18,
     "iphone":"110"},
    {"name":"lisi",
     "age":18,
     "iphone":"111"},
    {"name":"wangwu",
     "age":18,
     "iphone":"112"}
]
for card_info in card_list:
    print(card_info)