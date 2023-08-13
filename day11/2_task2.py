#


hours=int(input("enter a hour worked"))
rate=float(input("enter rate per hour"))
if hours<=40:
    total=hours*rate
    print("total=",total)
elif hours>40:
    remain=hours-40
    total=40*rate+remain*1.5*rate
    print("total=",total)
else:
    print("not worked")
