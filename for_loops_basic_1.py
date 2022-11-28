# Basic - Print all integers from 0 to 150.
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# # Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if(i%10 == 0):
        print("Coding Dojo")
    elif(i%5 == 0):
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(0, 500000):
    if i%2  != 0:
        sum += i
print(sum)

for i in range(2018, 0, -4):
    print(i)

lowNum = 4
highNum = 100
mult = 3
for i in range(lowNum, highNum):
    if i%mult == 0:
        print(i)


#extra practice
for i in range(0, 10):
    if i%2 == 0 and i%3 == 0:
        print(i)