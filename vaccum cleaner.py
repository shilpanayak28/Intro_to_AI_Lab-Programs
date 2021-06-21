flag=True
while flag:
    perc=input("enter the percept")
    loc=input("enter the location")
    if loc=="A":
        if perc=="dirty":
            print("action:suck  turn right")
            
        else:
            print("action:turn right")
            
    elif loc=="B":
        if perc=="dirty":
            print("action:suck  turn left")
            
        else:
            print("action: turn left")
    else:
        
        print("enter either A or B")
    print("do you want to continue?")
    cont=input("enter Y or N")
    if cont=='Y':
       flag=True
    else:
        flag=False
