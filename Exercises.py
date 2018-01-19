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

def ex6():
    palindrome = input("Enter a string: ")
    print(palindrome,palindrome[::-1])
    if palindrome == ''.join((reversed(palindrome))):
        print("Is a palindrome")
    else:
        print("Is NOT a palindrome!!")

def ex7():
    import random
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    a = []
    for x in range(random.randint(90,100)):
        a.append(random.randint(0,1000))

    print(a[::2])
    print(list(filter(lambda x: x % 2 == 0,a)))

def ex8():
    first = ""
    second = ""
    first_points = 0
    second_points = 0
    print("Use r for rock, s for scissor, p for paper and q for quit.")
    while first !="q" or second != "q":
        first = input("First player, enter your choice (r,s,p,q):")
        second = input("Second player, enter your choice (r,s,p,q):")
        if first == "r":
            if second == "r":
                # even
                print("Even")
            elif second == "s":
                # second win
                print("Second win")
                second_points+=1
            elif second == "p":
                # first win
                print("First win")
                first_points+=1
        if first == "s":
            if second == "r":
                # second win
                print("Second win")
                second_points+=1
            elif second == "s":
                # even
                print("Even")
            elif second == "p":
                # first win
                print("First win")
                first_points+=1
        if first == "p":
            if second == "r":
                # first win
                print("First win")
                first_points+=1
            elif second == "s":
                # second win
                print("Second win")
                second_points+=1
            elif second == "p":
                # even
                print("Even")
        print("First {}, second {}".format(first_points,second_points))
ex8()