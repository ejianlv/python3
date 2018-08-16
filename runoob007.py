#!/usr/bin/env python3
#coding=utf-8

def print_hello(name, sex="1"):
    sex_dict = {1:u'先生', 2:'女士'}
    print("hello {0} {1}, welcome to python world!".format(name, sex_dict.get(sex, u'先生')))

print_hello('tanggu', 3)

print_hello(name="tanggu", sex=1)
print_hello(sex=1, name="tanggu")
print_hello("tanggu", sex=1)
#print_hello(1, name='tanggu') 不支持
#print_hello(name="tanggu",1) 不支持
#print_hello(sex=1, "tanggu") 不支持

print_hello("jian lyu")
print_hello("jian lyu",2)
print_hello(sex=1, name="jian lyu")

def print_hs(*args):
    print(type(args))
    for i in args:
        print(i)

print_hs("a","ab","abc",1,2,3)

t1 =("a","ab","abc",1,2,3)
print_hs(t1)
print_hs(*t1)

def print_hss(**kargs):
    print(kargs)
    for k,v in kargs.items():
        print(k,"---",v)
print_hss(p1="a")
print_hss(a="aa",b="bb")
