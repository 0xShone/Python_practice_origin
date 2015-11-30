#coding: UTF-8
import sys

fruit_list = sys.argv[1:]
fruit_list.sort()
i = 0
while i + 1 < len(fruit_list) :
    print (fruit_list[i]),
    i += 1
else :
    print (fruit_list[i])
