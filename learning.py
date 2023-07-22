print('''这是由浙江大学22级大一本科生陈宇俊同学编写的Python程序，参考教材为浙江大学出版社的《Python程序设计（第2版）》
编写这个程序的初衷一方面是为了巩固自己的学习，另一方面是希望能帮助到别的同学
本人水平有限，其中只写了自己认为比较难掌握或者容易疏忽的地方，以及书上某些知识缺少实操示例，在这里尽量补充了
若想要运行查看效果，只需要将对应的章节注释去掉即可（Ctrl+/可以增加或者删除注释）
最后，希望可以真正帮助到大家，同时若有不当之处欢迎指出，祝大家有一段愉快的Python之旅''')
'Section 1 First impression of Python'
# import this
# # help()
# import turtle
#
# print("****************************")
# print(3,end='')
# print(4,end='')
# import turtle as T
# turtle.circle(10)
# turtle.done

'Section 2 types of datas in Python'

'Section 2.1 basic types'
# a=0b10
# b=0o10
# c=0x10
# print(a,b,c)
'an integer in Python can be much larger than you think'
# print(2**2**2**2**2)
'module is different with C'
# print(101/5)
# print(101//5)
# print(1.2e3)
'the number behind e must be an integer'
# a=divmod(9.0,2.0)
# print(a)
# print(int(3.7))
# print(round(80.23456,4))
'complex numbers are allowed in Python'
# print(3+4j,abs(3+4j))
# a=complex(4,-6)
# print(a.real,a.imag)
# import math as M
'empty strings are allowed in Python'
# s1="Python"
# s2="Java"
# s=s1+s2
# print(s)
# print("2"*5)
# print(1<3>2) #this is equal to 1<3 and 3>2,which is totally different to C
# a=None
# print(a)

'Section 2.2 statements'
# a,b=1,2
# a,b=b,a
# print(a,b)
# x=1
# if x%2==0:
#     print("偶数")
# else:
#     print("奇数")
# for i in [1,2,3,4]:
#     print(i,end='')
# print()
# for i in range(0,9,3):
#     print(i,end=' ')
# print()
# l1=[1/i if i%2==1 else -1/i for i in range(1,6) if i>0]
# print(l1)
# for i in range(30,40,2):
#     print("华氏:",i,"摄氏:","{:.1f}".format(5*(i-32)/9))
# s='Python'
# print("{0}".format(s))
# print("{0:>30}".format(s))
# print("{0:$^30}".format(s))
# a=0b00000101
# b=0b00010001
# print(a&b,a|b,a^b,~a,a<<2,a>>1)

'Section 3 lists, strings and tuples'

'Section 3.1 strings'
# l1="hello "
# l2="world"
# print(l1+l2,l1*3,l1[0],l1[0:3:2],len(l1),"h" in l1,"m" not in l1)
# print(l1[-2])
'''positive keys and negative keys can be used without bothering each other,
the step you give would determine where it would go'''
'If you want to copy a list without changing it ,you can do as follows'
# a=list(range(1,6))
# b=a[:]
# b[0]=6
# print(a,b)
'the elements in a list can be of different types, and this is quite different with C'
# b=[[2,3],4,5,6]
'when you want to compare two lists or its elements, you compare their dictionary orders'
# a='''Python
# Java
# C'''
# #this is equal to a='Python\
# #Java\
# #C'
# print(a)
"Strings in Python can't be changed directly, but lists can. That is, if you run 's='hello';s[0]='k'', this is wrong"
# s='hello World'
# print(s.title(),s.lower(),s.upper())
'Section 3.2 lists'

# matrix=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
# print(matrix[0][0])
'Notice that this definition can only do operation on rows,\
you can not directly operating columns through this definition'
'unlike strings, the elements of lists can be changed directly, just like the following shows:'
# a=[1,3,5,7,9]
# a[0]=2
# print(a)
'unlike arrays in C, the elements of lists can be deleted'
# name=['Alice','Kim','Karl','John']
# del name[2]
# print(name)
'del is a statement rather than a function'
# n=list('Perl')
# print(n)
# n[2:]=list('ar')
# print(n)
# number=[1,5]
# number[1:1]=[2,3,4]
# print(number)
'As for the functions of lists, please see page 71'
'''extend is different from +, because when you use a +,
you create a new list while the two lists you want to add together don't change.
But with extend, you change the list you want to change directly.
If you care about the memory, this matters.'''

'lists and strings'
# name='Weng Kai.jpg'
# a=name.split('.')
# print(a)
# a=['C:','Users','pc','Desktop']
# print('\\'.join(a))

'Section 3.3 tuples'
"the elements can be of different types, while a tuple can't be changed"
# print(3*(24))
# print(3*(24,))
'the following shows how to output the letters of a sentence in order'
# s='hello world'
# lst=[(s[index],index) for index in range(0,len(s))]
# lst.sort()
# print(lst)

'Section 3.4 random numbers and generating random numbers, please see page 77'
'you need to import random if you want to use functions to generating random numbers'

'Section 4 condition statements, loops and other statements'

'Section 4.1 condition statements'
"It's almost the same with C, you should mind the indentations"
'Here comes the demonstration: calculate your GPA through your score'
# score=int(input('Please put in your score:'))
# GPA=0
# if(score<60):
#     GPA=0
# elif(score>94):
#     GPA=5
# elif(60<=score<=61):
#     GPA=1.5
# else:
#     GPA=((score-62)//3)*0.3+1.8
# print(GPA)
'You can simplify the condition statements, please see page 89'

'Section 4.2 loops'

'Section 4.2.1 while'
"this is very similar to C, and it's easy to understand"
# num=int(input())
# a=2
# while a<num:
#     if num%a==0:
#         print("Not a prime")
#         break
#     a+=1
# else:
#     print("Is a prime")
"'a++' is forbidden in Python while allowed in C"

'Section 4.2.2 for'
# lst=['a','b','c','d','e']
# for i in lst:
#     print(i,end='')

'Section 4.3 Search and Sort'

'Linear Search vs Binary Search'

'Section 4.4 Matrices'
