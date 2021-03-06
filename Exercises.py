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

def ex11_ets(number):
    import math
    import time
    start = time.time()
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
    print(time.time() - start)
    print(len(nums),list(nums))
    return nums

def ex11():
    import time
    max = int(input("Enter an integer:"))
    start = time.time()
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
    print(time.time() - start)
    print(len(result),list(result))
    result2 = ex11_ets(max)
    print(result == result2)

def ex12():
    def get_first_last(alist):
        return [x for ind,x in enumerate(alist) if ind== 0 or ind==len(alist)-1]
    a= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
    print(list(get_first_last(a)))

def ex13():
    count = int(input("Enter number of fibonacci numbers:"))
    result = [1,1]
    while len(result) < count:
        result.append(result[len(result)-1] + result[len(result)-2])
    print(list(result))

def ex14():
    def  clean_list(alist):
        return list(set(alist))
    a = [1, 1, 2, 3, 5, 2, 13, 21, 13, 3, 89]
    print(list(clean_list(a)))

def ex15():
    def yoda(message):
        result = message.split()
        return result[::-1]
    sentence = str(input("Enter a sentence"))
    print(" ".join(yoda(sentence)))

def ex16():
    import string
    import random
    # 1. at least one from each group
    # 2. Min-len 4, max any
    pwlen = 10
    source = list()
    source.append(string.ascii_uppercase)
    source.append(string.ascii_lowercase)
    source.append(string.punctuation)
    source.append(string.digits)
    print(list(source))
    pw = ""
    for x in range(pwlen):
        pw += "".join(random.sample(source[x%4],1))
        #print(pw)

    print(pw)


def ex17():
    import requests
    from bs4 import BeautifulSoup
    url = "http://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,"html.parser")
    result = soup.find_all('a')
    for link in result:
        print(link.get('href'),link.contents)

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print(story_heading.contents[0].strip())


def ex18():
    import random
    def check_cows_bulls(n):
        cow = 0
        bull = 0
        for ind,x in enumerate(n):
            if x == number[ind]:
                cow+=1
            elif x in number:
                bull+=1
        print("C:", cow, "B:", bull)

    number = "{0:0>4}".format(random.randint(0,9999))
    print("Secret:",number)
    count = 0
    while True:
        guess = str(input("Enter number: "))
        count += 1
        if guess == number:
            print("Correct!")
            break
        else:
            check_cows_bulls(guess)
    print("You guessed",count,"number of time(s)")

def ex18a():
    import random
    def compare_numbers(number, user_guess):
        cowbull = [0, 0]  # cows, then bulls
        for i in range(len(number)):
            if number[i] == user_guess[i]:
                cowbull[1] += 1
            else:
                cowbull[0] += 1
        return cowbull

    if __name__ == "__main__":
        playing = True  # gotta play the game
        number = str(random.randint(0, 9999))  # random 4 digit number
        print(number)
        guesses = 0
        print("Let's play a game of Cowbull!")  # explanation
        print("I will generate a number, and you have to guess the numbers one digit at a time.")
        print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
        print("The game ends when you get 4 bulls!")
        print("Type exit at any prompt to exit.")
        while playing:
            user_guess = input("Give me your best guess!")
            if user_guess == "exit":
                break
            cowbullcount = compare_numbers(number, user_guess)
            guesses += 1
            print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
            if cowbullcount[1] == 4:
                playing = False
                print("You win the game after " + str(guesses) + "! The number was " + str(number))
                break  # redundant exit
            else:
                print("Your guess isn't quite right, try again.")

def ex21():
    with open('kalle.txt','r') as my_file:
        # my_file.write("Hello world again\n")
        print(my_file.read())
    print("Ready!")

def ex22():
    with open("Exercises.py",'r') as myfile:
        content = myfile.read().split()
        result = {}
        for word in content:
            if word in result.keys():
                result[word]+=1
            else:
                result[word] = 1
        for k in sorted(result):
            print(result[k],k)


def ex23():
    pn = []
    hn = []
    with open("primenumbers.txt",'r') as primes:
        pn = list(primes.read().split())
    with open("happynumbers.txt", 'r') as happy:
        hn = list(happy.read().split())
    res = [x for x in hn if x in pn]
    print(res)

def ex27():
    game = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

    def check_winner():
        for row in game:
            if len(set(row)) == 1:
                if row[0] != '-':
                    print(row[0],"win!")
                    return True
        for col in zip(*game):
            if len(set([i for i in col])) == 1:
                if col[0] != '-':
                    print(col[0],"win!")
                    return True
        if len (set([game[0][0],game[1][1],game[2][2]])) == 1 and game[0][0] != '-':
            print(game[0][0],"win!")
            return True
        if len (set([game[0][2],game[1][1],game[2][0]])) == 1 and game[0][2] != '-':
            print(game[0][2],"win!")
            return True
        return False

    def print_board():
        space_left = False
        for row in game:
            for col in row:
                print(col," ",end='')
                if col == '-':
                    space_left = True
            print()
        if check_winner():
            return True
        elif not space_left:
            print("No winner!")
            return True
        else:
            return False


    def get_input(user):
        answer = str(input(user + "(x,y): "))
        pos = list(answer.split(","))
        if game[int(pos[0])][int(pos[1])] == '-':
            game[int(pos[0])][int(pos[1])] = user
            return False
        else:
            return True
    print_board()
    while True:
        while get_input('X'):
            print("Illegal pos")
        if print_board():
            break
        while get_input('O'):
            print("Illegal pos")
        if print_board():
            break


def ex34():
    import json
    FILENAME = "birthdays.json"
    NAME = "name"
    BIRTHDAY = "birthday"

    def store_new_person(res):
        print(res)
        with open(FILENAME,"w")as bd:
            bd.write(json.dumps(res,indent=2,sort_keys=True))

    with open(FILENAME,'r') as bd:
        result = json.loads(bd.read())

    result.append({"name":"Mattias","birthday":"930725"})
    print("before",result)
    result.append([{"name":"LiQi","birthday":"920914"},{"name":"Ding Fung","birthday":"670430"}])
    print("after",result)

    name = str(input("Enter person to lookup:"))
    found = False
    for person in result:
        if person[NAME] == name:
            print("Birthday:",person[BIRTHDAY])
            found = True
    if not found:
        birthday = str(input("Not, found. Enter birthday:"))
        result.append({NAME: name, BIRTHDAY: birthday})
        store_new_person(result)
ex34()


