from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\WebDrivers\chromedriver.exe")
#driver.get("https://www.google.com/")
print("--------------------------")
print(":swapping numbers")
class reverse():
    def rev(self, m=-24, n=-20):
        print("beforeswap ", m, n)
        m = m+n
        n = m-n
        m= m-n
        print("Afterswap ", m, n)
#m = int(input("m "))
#n = int(input("n "))
swap = reverse()
swap.rev()

class string1():
    def reverse1(self,s):
        abc = ""
        for i in s:
            abc = i + abc
        print(abc)

obj1 = string1()
obj1.reverse1("Race")

class string2():
    def reverse2(self, st):
        st = st[::-1]
        print(st)
obj2 = string2()
obj2.reverse2("Car")

class string3():
    def reverse3(self,s):
        str = "".join(reversed(s))
        print(str)
#s = str(input("plese enter ur string "))
obj3 = string3()
obj3.reverse3("welcome")

class string4():
    def reverse4(self, s):
        word = s.split()
        print(word)
        rev_s = []
        for i in word:
            rev_s.append(i[::-1])
            #print(rev_s)
        print(rev_s)
        res = "".join(rev_s)
        print(res)
obj4 = string4()
obj4.reverse4("python is the best lanugrage")

class string5():
    def reverse5(self, s):
        rev_s = ""
        count = len(s)
        while count>0:
            rev_s = rev_s + s[count-1]
            #print(rev_s)
            count = count - 1
        print(rev_s)
obj5 = string5()
obj5.reverse5("Chnadler")

abc = "fractions"
assert "action" in abc
print("tes")

print("-------------------------")
print("inheritance")

class father():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("This is parent class")
        print(self.name, self.age)

class son(father):
    def display1(self, name, age):
        print("This is child class")
        print("son's name and age ", self.name, self.age)

obj6 = son("karthick", 50)
obj6.display()
obj6.display1("sekar", 40)

print("-----------------")
print("funtion overloading")

class overload():
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            add = a+b+c
        elif a!=None and b!=None:
            add = a+b
        else:
            add = a
        print(add)

obj7 = overload()
obj7.sum(5, 100, 100)

print("----------------")
print("overrinding")
class override():
    def __init__(self):
        self.colour = "red"
    def display(self):
        print(self.colour)

class overridev2(override):
    def display(self):
        self.colour = "Green"
        print(self.colour)

obj8 = overridev2()
obj8.display()

print("----------------")
print("Encapsulation")
class encap():
    def __init__(self):
        self.__value = "Bank"
        #print(self.value)

    def __memfun(self):
        print(self.__value)

obj9 = encap()
obj9._encap__memfun()


class exerc1():
    def strn(self, s):
        count = len(s)
        rev = ""
        while count >0:
            rev = rev + s[count-1]
            count = count -1
        print(rev)


objc = exerc1()
objc.strn("hwllo os the workd")

print("-----------------")
print("practise")
def age(value):
    assert value>0, "please give ct value"
    print(value)
age(10)

print("-------------------")
print("exercise, printing large 3 numbers from list")
class largeEle():
    def input(self, list, num):
        print(list)
        list.sort(reverse=False)
        print(list)
        #num = num -1
        print(list[-1:num:-1])
obn = largeEle()
obn.input([12,45,23,67,23,44,65], 3)

print("------------List----------------")
grp = [3,5,1,7,3,6,5.4,8,9]
grp.append(100)
print(grp)
grp.extend([200,300,400])
print(grp)
grp.insert(3, "python")
print(grp)
grp.remove(3)
print(grp)
grp.pop(2)
print(grp)
print(sorted(grp))
grp.extend([3,5,6,7,6])
print(grp)
print(grp.count(3))

# print("----------Hackkerrank list--------------")
# N= int(input())
# list = []
# for i in range(N):
#     s = input().split()
#     print(s)
#     if s[0] == "insert":
#         list.insert(int(s[1]), int(s[2]))
#     elif s[0] == "append":
#         list.append(int(s[1]))
#     elif s[0] == "remove":
#         list.remove(int(s[1]))
#     elif s[0] == "pop":
#         list.pop(-1)
#     elif s[0] == "sort":
#         list.sort()
#     elif s[0] == "reverse":
#         list.reverse()
#     elif s[0]  == "print":
#         print(list)
#     else:
#         print("wrong input")

sn = "hello"
sn1 = sn[::-1]
print(sn, sn1)
from collections import Counter
my_str = "123445"
counter = Counter(my_str)
st = '4'     #input("enter character: ")
print(counter[st])

print("Lambda")
f = lambda x,y,z: x*y + z
print("f = ", f(2,5,6))

print("---multi-threading---")
#
import _thread
#
# def a(msg):
#     count = 0
#     while count<5:
#         print(msg)
#         count +=1
#         time.sleep(1)
# def b(msg):
#     count = 0
#     while count<5:
#         print(msg)
#         count +=1
#         time.sleep(2)
# _thread.start_new_thread(a,("thread1",))
# _thread.start_new_thread(b,("thread2",))
# while 1:
#     pass
import threading
#
# def display(iter, sleep, msg):
#     for i in range(iter):
#         print(msg)
#         time.sleep(sleep)
#
# t1 = threading.Thread(target=display, args=(5, 2, "Thread1",))
# t1.start()
# t2 = threading.Thread(target=display, args=(3, 5, "Thread2",))
# t2.start()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


lst = [1,3,4,4,5,1,2,3]
count = {}
for i in lst:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print("count : ", count)

dict = {'a':1, 'b':2, 'c':100, 'c':0}
print("dict: ", dict)
for x in dict:
    print(x)
for i in dict:
    print(dict[i])
