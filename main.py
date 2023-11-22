print("\t--------------------------")
print("\tWelcome TO OUSL library System")
print("\t--------------------------\n")
print("What Are You Looking For ?\n")
print("\t 01\t Add a new resource ")
print("\t 02\t Remove a resource ")
print("\t 03\t View currently available resources ")
print("\t 04\t View currently unavailable resources ")
print("\t 05\t View all resources ")
print("\t 06\t Lend a resource ")
print("\t 07\t Update resource ")
print("\t 08\t Exit ")

x=int(input(" Enter Your Choice :- "))

if x==1:
    import add_res
elif x==2:
    import Remove
elif x==3:
    import Available
elif x==4:
    import Not_available
elif x==5:
    import View_all
elif x==6:
    import Lend
elif x==7:
    import receive
elif x==8:
    print("Have a nice day!")
else:
    print("please enter valid number!!!")
    import __main__
