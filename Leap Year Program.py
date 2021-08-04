# Take an input from user and print if the date that user gave is leap year or not
# leap year = 366 days 
# A leap year occurs every 4 years. However, in centuries, century year is considered as a leap year only if it is divisible by 400 (xx00)

year = int(input("Type A Date (Year || Ex: 2005): "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

    

