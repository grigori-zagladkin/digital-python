a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c   
if d > 0:
    try:
        if a == 0:
            print(round(-c/b, 3))
        else:
            x1 = (-b + d**0.5)/(2*a)
            x2 = (-b - d**0.5)/(2*a)
            print(round(x1, 3), round(x2, 3))
    except:
        print('ERROR')
elif d == 0: 
    try:
        print(round(-b/(2*a), 3), round(-b/(2*a), 3))
    except:
        print('ERROR')
else:
    print('ERROR')
       
