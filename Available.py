import Variable
class available:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("What Are You Looking For ?\n")
    print("\t 01\t Books")
    print("\t 02\t Magazines ")
    print("\t 03\t Educational DVDs ")
    print("\t 04\t Lecture CDs ")
    
    check=int(input("Choose number :- "))
    
    if (check==1):
        for x in Variable.books:
            q=Variable.books.index(x)
            if (Variable.books[q][5]>0):
                print(Variable.books[q])
            else:
                continue
            
    elif(check==2):
        for x in Variable.magazine:
            q=Variable.magazine.index(x)
            if (Variable.magazine[q][5]>0):
                print(Variable.magazine[q])
            else:
                continue
            
    elif(check==3 or check=="03"):
        for x in Variable.edudvd:
            q=Variable.edudvd.index(x)
            if (Variable.edudvd[q][4]>0):
                print(Variable.edudvd[q])
            else:
                continue
    
    elif(check==4 or check=="04"):
        
        for x in Variable.lecdvd:
            q=Variable.lecdvd.index(x)
            if (Variable.lecdvd[q][4]>0):
                print(Variable.lecdvd[q])
            else:
                continue
            
    else:
        print("Enter valid number")