#cording: UTF-8

list_int = range(0, 5)
print list_int

list_mix = [0, "Tokyo", 1, "Osaka", 2, "Aichi"]
print list_mix

new_list = list_int + list_mix
print new_list

list_int.extend(list_mix)
print list_int

print "Osaka" in list_mix
