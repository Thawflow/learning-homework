# 随堂练习
name = "猴哥"
age = 30
print("我是" + name + "，" + str(age) + "岁") # 转为字符后通过+拼接，没有空格
print("我是" + name + "，",  age , "岁") # 数字会在前后各加一个空格

print(f"我是{name}，{age}岁") # f-string：f"..." 里 {变量} 自动替换
print(f"明年我就{age + 1}岁啦") # { } 里还能直接算式

# 小任务
name = input("你叫什么名字？")
prey = input("最喜欢什么猎物？")
age = int(input("多大了？"))
print(f"我是雷族的{name}，最爱{prey}，明年就{age + 1}岁了")
