import urllib.request
import json
import urllib
from MyModule import *


import click

t = TestClass("Torsten")
m = TestClass("Ming")
print(t+m)
t+=m
t.print()
print (m < t)
p = TestClass("pelle")
P = TestClass("PELLe")
print(p)
print(P)
if p == P:
    print("Same")
else:
    print("Differs")
print(p.className)
print(P.className)

if t:
    print("Is torsten")
else:
    print("Is not Torsten")

def get_xml(what):
    response = urllib.request.urlopen(what).read()
    events = ElementTree.fromstring(response)
    return events

def get_json(what):
    response = urllib.request.urlopen(what).read()
    events = json.loads(response)
    return events

def print_all(*args):
    for item in args:
        print(item)

def toMap(**args):
    return args


#people =toMap(torsten=64,ming=60,mattias=24)
#for person in people:
#    print(person,"is",people[person])


#res = get_json('http://teamtreehouse.com/matthew.json')
#print(json.dumps(res,indent=4,sort_keys=True))

#res = get_xml('https://httpbin.org/xml')
#for  line in res:
#    for node in line:
#        print(node)


people ={'torsten':64,'ming':60,'mattias':24,'pelle':30}
print("before",people)
for person in people:
    #print('{} is {} years old'.format(person,people[person]))
    print("bef",people)
   # import pdb;pdb.set_trace()
  #  people[person.upper()] = people[person]
    #print("mid",people)
   # people.pop(person)
    print("aft",people)

from functools import reduce
#reduce(lambda a,b: print(a,b),people)
print("after:", people)
#print(upperPeople)

def plus(a,b):
    return a+b


print(plus(1,3))

my_max = lambda a,b:a + b if a > b else 3
print(my_max(1,2))
print(my_max(4,3))

with open('test.py') as f:
    for line in f:
        print('Line is {}'.format(line))
f.close()
f = open('test.py')
i=0
for line in f:
    print('{}'.format(i))
    i+=1
import NumPy
a = np.arange(15).reshape(3,5)