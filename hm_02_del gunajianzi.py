name_list = ["zhangsan", "lisi", "wangwu"]

# zhidao shiyong del guanjianzi(delete) shanchu liebiao yuansu

# del guanjianzi benzhishang shiyonglai jiang yige bianliang cong neicun zhong shanchu de
del name_list[1]
name = "xiaoming"

del name
# zhuyi:如果使用del 关键字将变量从内存中删除,后续de daima jiubuneng zaishiyong zhege bianliang le 
print(name)

print(name_list)
