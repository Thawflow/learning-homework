#1
print(type(42))
print(type("42"))
print(type(4.2))
print(type("ThawPaw"))
print(type(input("随便输入：")))

#2
print("2026" + "2026")
print(2026 + 2026)
print("10" * 3)

#3
cats = int(input("How many cats at home? "))
print(cats + 1)

#4
price = float(input("单价?"))
quantity = int(input("买几袋?"))
amount = float(input("付了多少钱?"))
total = price * quantity
change = amount - total
print(f"总价：{total}，找零：{change}")

#5

seconds = 3661
hour = 3661 // (60 * 60)
minute = (3661 - 60 * 60 * hour) // 60
second = 3661 % 60
print(f"3661秒是{hour}小时{minute}分{second}秒")