# 1
name = input("Your name?")
print(len(name))
print(name.upper())
print(name.lower())

# 2
s = "Fireheart"

print(s[0])
print(s[-1])
print(s[0:4])
print(s[4:])
print(s[1:3])

# 3
name_with_space = input("Enter you name with some trailing spaces")
print(len(name_with_space))
print(len(name_with_space.strip()))
      
# 4
f_h = "Fireheart"
print(f_h.replace("e","*"))

# 5
fav_cat = input("Your favorite cat in the Cats")
hidden = fav_cat[0] + "..." + fav_cat[-1]

print(hidden)
print("star" in fav_cat)
