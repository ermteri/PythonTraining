# Exercises taken from http://www.practicepython.org/
def ex1():
    import datetime
    now = datetime.date.today().year
    name=input("Enter your name:")
    age = int(input("Enter your age:"))
    num = int(input("Enter how many times:"))
    for i in reversed(range(1,99)):
        print(i)
        print('Dear {} you will be 100 {}'.format(name,now+100-age))

def ex2():
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        if num % 4 == 0:
            print("quadruple!!")
        else:
            print("Even number!!")
    else:
        print("Odd number!!")

def ex3():
    a =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print (list(filter(lambda x: x>3,a)))

def ex4():
    num = int(input("Enter an integer: "))
    def isdiv(x):
        return num % x == 0

    print(list(filter(isdiv, range(1, num))))
    print(list(filter(lambda x: num % x == 0, range(1,num))))

def ex5():
    import random
    first = []
    second = []
    for x in range(random.randint(10,20)):
        first.append(random.randint(1,20))
    for y in range(random.randint(10,20)):
        second.append(random.randint(1,20))
    print(sorted(first))
    print(sorted(second))
    print(set(sorted(list(filter(lambda val: val in second,first)))))

ex5()