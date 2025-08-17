def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))

    # 定义一个字符串变量

    result = "hello"
    print("函数要返回数据的内存是 %d" % id(result))


    # 将字符串变量返回
    return result

# 定义一个变量
a = 10

print("a 变量保存数据的内存地址是 %d " % id(a))

# 调用 test函数,本质上传递的是实参保存数据的引用,不是实参保存的数据
test(a)