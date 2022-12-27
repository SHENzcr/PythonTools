# import keyword
# print(keyword.kwlist)

import sys
# from sys import argv,path

print("Python",end = " ")
print("Hello World")
if True == 1:
	print("1")
else:
	print("2")

def test():
	print("call test func")

test()

for i in sys.argv:
	print(i)

str = "12345"
print(str[0:4])
list = ["a",1,"ss"]	
print(list[0])

if __name__ == "__main__":
	print("main func")

dir()	