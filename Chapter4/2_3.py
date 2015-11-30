#coding: UTF-8

list_mix = [0, "Osaka", 1, "Tokyo", 2, "Nagano"]

print list_mix[3]
print len(list_mix)
print list_mix[3:]

list_mix[3] = "Nagoya"
print list_mix

list_mix.append(3)
print list_mix

list_mix.insert(0, -1)
list_mix.insert(1, "Aomori")
print list_mix
