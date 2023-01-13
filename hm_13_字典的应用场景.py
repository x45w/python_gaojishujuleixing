# 将 多个字典 放在 一个列表 中,在进行遍历
card_list = [
    {"name": "张三",
      "qq": "12345",
      "phone": "110"},
    {"name": "李四",
      "qq": "54321",
      "phone": "10086"}
]

for card_info in card_list:
    print(card_info)