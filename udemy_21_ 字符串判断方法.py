# 判断空白符
# space_str = " \t\n\r"
# print(space_str.isspace())

# 判断字符串中是否只包含数字
# num_str = "\u00b2"
num_str = "一千零一"
print(num_str)

# 下列3个方法只能判断数字,不能判断小数
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
