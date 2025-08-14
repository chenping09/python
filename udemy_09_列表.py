name_list =["zhangsan","lisi","wangwu"]

print(name_list.index("zhangsan"))

print(name_list)

name_list[1]="李さん"
print(name_list.index("李さん"))

name_list.append("python")
name_list.insert(1,"python2")

temp_list=["1","2"]
name_list.extend(temp_list)
name_list.sort()
name_list.remove("1")
name_list.pop()
name_list.pop(2)

# del 关键字本质上是将一个变量从内存中删除
del name_list[3]
#name_list.clear()
print(name_list)