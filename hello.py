# print("hello world")
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
#this is a comment
# print("# the hash here doesn't signify a comment")
# the below are important things to know in py programming because they"ll be usesful
p = 'this is the first line and \n this is the second line'
print(p)
# note that since the print() is used here, the output would print the newline in the terminal
#else if p runs without the print() function, the newline would be ignored and pinted as \n
# but to ignore printing as newline, add a r before the qoute in the print() function as seen below
# print(r"this is the first line and \n this is the second line")
#regardless of the string qoute
# print("""\
# This is the best thing I have done ever in my life.
# If you don't believe me, then come here and find out yourself.
# I'm in love with the game man.
# """)
#The below are examples of using list
a = [1, 2, 3, 4]
b = [12, 13, 14]
c = [a, b]
# print(a)
# print(c[1][0])
a.append(12)
a.clear


#First step towards programming; the first exam below is using a while loop
d, f = 0, 1
while d < 10:
    print(d)
    d, f = f, d + f
#To avoid the newline preset in the print() function, the arg end can be passed: print(d, end=',')

#Using the if and else statement
x = int(input("Please fill in an integer  "))
print(x)
if x < 0:
    x = 0
    print('Negative change x to Zero')
elif x == 0:
    print('X is truly Zero')
elif x == 1:
    print("X is Single")
else:
    print('X is more')

#Using for statement
words = ['cat', 'curtain', 'ahmed_loyal']
for w in words:
    print(w, len(w))

i, f = 0, 5
for i in range(f):
    print("I is", i)

#Using break and continue statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')    

#Using match statement
status = 400
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
#Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches,
#none of the branches is executed.
