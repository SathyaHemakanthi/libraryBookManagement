print("\t--------------------------")
print("\tWelcome TO OUSL library System")
print("\t--------------------------\n")
print("What Are You Try To Add ?\n")
print("\t 01\t Books")
print("\t 02\t Magazines ")
print("\t 03\t Educational DVDs ")
print("\t 04\t Lecture CDs ")

x=int(input(" Enter Your Choice :- "))

if x==1:
    import Books
elif x==2:
    import Magazines
elif x==3:
    import EduDVD
elif x==4:
    import LecDVD
else:
    import main
