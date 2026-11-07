x = 5

if(type (x) is int):
    
    print("True")
    
else:
    
    print("False")
    
x = 5.5

if(type (x) is not float):
    
    print("True")
    
else:
    
    print("False")
    
x = 20

y = 20

if (x is y):
    
    print("They are same identity")
    
else:
    
    print("False, They are different identity")
    
y = 30

if(x is not y):
    
    print("They have a different value")