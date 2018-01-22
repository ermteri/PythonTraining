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
    import random
    def get_second_choice():
        choice =['r','s','p']
        return choice[random.randint(0,2)]
    first = ""
    second = ""
    first_points = 0
    second_points = 0
    print("Use r for rock, s for scissor, p for paper and q for quit.")
    while first !="q" or second != "q":
        first = input("First player, enter your choice (r,s,p,q):")
        if first == "q":
            break
        #second = input("Second player, enter your choice (r,s,p,q):")
        if second == "q":
            break
        second = get_second_choice()
        print("Second choose:",second)
        if first == "r":
            if second == "r":
                # even
                print("Even")
            elif second == "s":
                # second win
                print("First win")
                first_points+=1
            elif second == "p":
                # first win
                print("Second win")
                second_points+=1
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
        else:
                print("Invalid choice:",first)
        print("First {}, second {}".format(first_points,second_points))
    print("Final result: First {}, second {}".format(first_points,second_points))

def ex9():
    import random
    guess = ""
    number_of_guesses = 0
    number = random.randint(1, 9)
    while guess != 'exit':
        guess = str(input("Guess number:"))
        number_of_guesses+= 1
        if int(guess) == number:
            print("Great you were right")
            break
        elif int(guess) > number:
            print("Too high!")
        elif int(guess) < number:
            print("Too low!")
    print("You guessed ", number_of_guesses)

def ex10():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [x for x in a for y in b if x==y]
    d  =[]
    d = [x for x in c if c.count(x) == 1 ]
    print(list(c))
    print (list(d))

def ex11(max):
    #max = int(input("Enter an integer:"))
    #print(list(range(2,number)))
    #print(number%2)
    #result = [x for x in range(2,number) if number % x == 0]
    #print(list(result))
    #if len(result) > 0:
    result = []
    for number in range(1,max):
        if len([x for x in range(2,number) if number % x == 0]) > 0 or number == 1:
            #print("Prime-number")
            #print("Not a prime number")
            x=1
        else:
            result.append(number)
    return result
    #print("Number of primes:", count)
def ex11_ets(number):
    import math
    #number = int(input("Enter an integer:"))
    #Step 1 and 2
    nums = [x for x in range(2,number+1) if x%2!=0 or x == 2]
    i=1
    # step 3
    next = nums[i]
    #print(next,list(nums))
    # step 4 5
    while next < math.sqrt(number):
        nums = [x for x in nums if x%next!=0 or x == next]
        #print(list(nums))
        i+=1
        next = nums[i]
        #print(next)
    # step 6
    return nums
    #print(list(nums))

import time
number = int(input("Enter an integer:"))
start = time.time()
result1 = ex11(number)
print(time.time() - start)
print(list(result1))
print(len(result1))
start = time.time()
result2 = ex11_ets(number)
print(time.time() - start)
print(list(result2))
print("Len:",len(result2))
print(result1 == result2)

