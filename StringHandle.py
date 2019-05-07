a = input("name:").strip() #String trim : strip()  /  strip("A")
b = input("age:").strip() #String trim : strip()

# msg = '''
# Your inputs :
#     Name : %s
#     Age %s
# '''%(a, b)
# print(msg)
# print("your inputs: Name : %s \n Age %s \n" %(a, b))
# %d number %f


#list
nameList = ['a', 'b', 'c']
# nameList.append('d')
# nameList.index('b')
# nameList.count('c')
# nameList.insert(2,'e')
# print(nameList)
# nameList.pop()
# nameList.remove('a')
# print(nameList)
# nameList.reverse()
# print(nameList)
# nameList.sort()
# print(nameList)

#切片
a = nameList[0:2]
b = nameList[1:]
c = nameList[-1:]
print(nameList)
print(a)
print(b)
print(c)
a.extend(b)
print(a)
if 'b' in a:
    print('yes')

#元祖 tuple
t = (1,2,3,4)
list(t) #tuple transfer to list