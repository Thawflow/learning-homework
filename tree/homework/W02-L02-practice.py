name = "VioletShine"
print(len(name))
print(name.upper())
print(name.lower())

cn="cat"
print(len(cn))
print(cn.upper())

icepaw = "冰爪"
print(len(icepaw))
print(icepaw.upper()) # 汉字也有大写？ 为什么不出错
print(icepaw.lower())

dirty = " IcePaw  "
print(len(dirty))
print(len(dirty.strip()))


story = "I like dogs"
print(story.replace("dogs","cats"))

cat = "Thawpaw"

print(cat.replace("w","W")) # 所有的都要替代


s = "Fireheart"
print(s[0])
print(s[-1])
print(s[1:3])
print(s[:4])
print(s[4:])


print("fire" in "fireheart")
print("Fire" in "fireheart")
print("a" in "cat")

name = "fireheart"
name = name.upper()
print(name)



