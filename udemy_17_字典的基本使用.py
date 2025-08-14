xiaoming = {"name":"小明"}
# 取值
print(xiaoming["name"])
# 增加/修改
xiaoming["age"] = 18
xiaoming["name"] = "小晓明"
print(xiaoming)
# 统计键值对数量
print(len(xiaoming))
# 合并字典
temp_dict = {"height":1.75}

# 如果被合并的字典中包含已经存在的键值对时,会覆盖原来的键值对
xiaoming.update(temp_dict)
# 清空字典
xiaoming.clear()

# 删除
# xiaoming.pop("age")
#print(xiaoming)