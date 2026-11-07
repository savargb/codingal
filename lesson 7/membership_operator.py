print("Enter Marks Obtained in 5 subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input")
    
elif avg in range(91, 101):
    print("A+ grade")
    
elif avg in range(81, 91):
    print("A grade")
    
elif avg in range(71, 81):
    print("B+ grade")
    
elif avg in range(61, 71):
    print("B grade")
    
elif avg in range(51, 61):
    print("C+ grade")
    
elif avg in range(41, 51):
    print("C grade")
    
elif avg in range(31, 41):
    print("D+ grade")
    
elif avg in range(21, 31):
    print("D grade")