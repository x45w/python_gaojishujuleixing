name_list = ["张三", "李四", "王五","王小二", "张三"]

# len(length长度)函数可以统计列表中元素的总数
list_len = len(name_list)

print("%d" %list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")

print("%d" %count)

name_list.remove("张三")

print(name_list)
