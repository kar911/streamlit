# class S1:
#     def __init__(self) -> None:
#         pass

# class S2(S1):
#     def __init__(self) -> None:
#         pass

# class S3(S2):
#     def __init__(self) -> None:
#         pass

# class S4(S2):
#     def __init__(self) -> None:
#         pass


# import inspect as im
# import re
# # from tkinter import N

# # def v():
# #     f=x+12

# # c= lambda x: x+
# # for i in im.getclasstree([S2,S4]):
# #     print(i)
# # print(im.getsource( c ))


# class NUM:
#     def __init__(self) -> None:
#         self.strr=1000

#     def __repr__(self) -> str:
#         return str(self.strr)+'-------'

#     def __call__(self):
#         print(self.strr+100)

#     def __str__(self) -> str:
#         return str(self.strr)+'++++++'
    
# # cl=NUM()
# # print(f"{cl}")
# # cl()
# # str(cl)

# # META CLASSES 
# #---------------------------------------------------------------
# # class Testt:
# #     pass

# # print(Testt)
# # print(Testt())


# # def greet(self):
# #     self.h=9000
# # #                   |inhetance from Testt
# # test = type("Test",(Testt,),{"value":12,"hello":greet})
# # c=test()
# # c.hello()
# # print(c.value)
# # print(c.h)
# # print(test)
# # print(test())

# # make meta class
# #--------------------------------------------------------------
# # import type
# class Meta(type):
#     def __new__(self, class_name,bases,attrs):
#         if 'x' in attrs:
#             print("found") #  Meta classes are used to check the diffreent perameters before
#                             # used to create any class
#         print(class_name,bases,attrs,sep='\n')
#         return type(class_name,bases,attrs)

# class Dog(metaclass=Meta):
#     x=5 # contain 'x'
#     y=8
#     def __init__(self) -> None:
#         self.l=100
#     def greet(self):
#         print("hello")
# Dog().greet()
# print(Dog.x)


# def wra(x):
#     def do(*args,**kwargs):
#         print("start")
#         r = x(*args,**kwargs)
#         print("end")
#         return r
#     return do
    

# @wra
# def good(y):
#     print("hello32134 \ny=",y)
#     return 10132


# print(good(12))


# class empl:

#     @classmethod
#     def st(cls,str):
#         return cls(*str.split('-'))

#     @staticmethod   # it is used as fuction used internaly without any  used in  email property
#     def __printfff(strr,obj):
#         print(strr,"++++++++===",obj.first)

#     @classmethod # help to change class variable can be edited by class objects also
#     def edit_leaves(cls,num):
#         cls.no_of_leaves =num #class 

#     def __init__(self,first,last) -> None:
#         self.first=first
#         self.last=last
#         # self.email=first+last+"@gmail.com"


#     # @property # first make fuction property  @property tag also works as a getter method
#     # def fullname(self)->str:
#     #     return self.first+self.last

#     @property
#     def fullname():
#         pass

#     @property
#     def email(self)->str:
#         self.__printfff("hello",self) # used static method here
#         return self.first+self.last+"@gmail.com"



#     @fullname.getter # same as @property 
#     def fullname(self)->str:
#         return self.first+'--------'+self.last
    

#     @fullname.setter # then you can use 
#     def fullname(self,name):
#         first,last=name.split(' ')
#         self.first=first
#         self.last=last
    
#     @fullname.deleter
#     def fullname(self):
#         print("deleting name")
    
#     # @fullname.getter
#     # def fullname(se)

# emp1=empl("abc","fdg")

# emp3=empl.st("kartik-m")


# emp2=empl("hbs","mkmk")
# print(emp2.email)
# emp2.fullname = "hbs kmkm"
# print(emp2.fullname)
# print(type(emp1.email))
# print(emp2.email)
# print(emp3.email)




# -------------------------------------------------------===================================


import streamlit as st


class Counter:
    def __init__(self):
        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'title' not in st.session_state:
            st.session_state.title = "Calculator"
        self.col1, self.col2 = st.columns(2)

    def add(self):
        st.session_state.count += 1

    def subtract(self):
        st.session_state.count -= 1

    def tester(self):
        if 'tester' not in st.session_state:
            st.session_state.tester = "Tester"
        else:
            st.session_state.tester = "Already tested"
        with self.col2:
            st.write(f"Hello from the {st.session_state.tester}!")

    def window(self):

        with self.col1:
            st.button("Increment", on_click=self.add)
            st.button("Subtract", on_click=self.subtract)
            st.write(f'Count = {st.session_state.count}')
        with self.col2:
            st.button('test me', on_click=self.tester)



if __name__ == '__main__':
    ct = Counter()
    ct.window()




