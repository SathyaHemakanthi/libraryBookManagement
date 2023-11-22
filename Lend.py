import Variable

class lend:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("What Are You Looking For ?\n")
    print("\t 01\t Books")
    print("\t 02\t Magazines ")
    print("\t 03\t Educational DVDs ")
    print("\t 04\t Lecture CDs ")
    
    chooce=int(input("choose number :- "))
    r=-1
    print("Fill your details\n")
    
    
    if(chooce==1):
        for x in Variable.books:
            q=Variable.books.index(x)
            if (Variable.books[q][5]>0):
                print(Variable.books[q])
            else:
                continue
            
        tid=input("Enter Book ID you want")
        duration=int(input("how meny date you want it"))
        for x in Variable.books:
                if(tid in x):
                    w="found"
                    place=Variable.books.index(x)
                    print(Variable.books[place][4]*duration)
                    print("do you want this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        sname=input("Enter Your Name")
                        snumber=input("Enter Your S Number")
                        print("BEFOR :-\t",Variable.books)
                        Variable.books[place][5]-=1
                        print("AFTER :-\t",Variable.books)
                        print("BEFOR :-\t",Variable.lend)
                        got=[sname,snumber,tid,duration]
                        Variable.lend.append(got)
                        print("AFTER :-\t",Variable.lend)
                        import main
                    else:
                        import main
    elif(chooce==2):
        for x in Variable.magazine:
            q=Variable.magazine.index(x)
            if (Variable.magazine[q][5]>0):
                print(Variable.magazine[q])
            else:
                continue
            
        tid=input("Enter Magazines ID you want")
        duration=int(input("how meny date you want it"))
        for x in Variable.magazine:
                if(tid in x):
                    w="found"
                    place=Variable.magazine.index(x)
                    print(Variable.magazine[place][4]*duration)
                    print("do you want this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        sname=input("Enter Your Name")
                        snumber=input("Enter Your S Number")
                        print("BEFOR :-\t",Variable.magazine)
                        Variable.magazine[place][5]-=1
                        print("AFTER :-\t",Variable.magazine)
                        got=[sname,snumber,tid,duration]
                        print("BEFOR :-\t",Variable.lend)
                        Variable.lend.append(got)
                        print("AFTER :-\t",Variable.lend)
                        import main
                    else:
                        import main
                        
    elif(chooce==3):
        for x in Variable.edudvd:
            q=Variable.edudvd.index(x)
            if (Variable.edudvd[q][5]>0):
                print(Variable.edudvd[q])
            else:
                continue
            
        tid=input("Enter Educational DVDs ID you want")
        duration=int(input("how meny date you want it"))
        for x in Variable.edudvd:
                if(tid in x):
                    w="found"
                    place=Variable.edudvd.index(x)
                    print(Variable.edudvd[place][4]*duration)
                    print("do you want this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        sname=input("Enter Your Name")
                        snumber=input("Enter Your S Number")
                        print("BEFOR :-\t",Variable.edudvd)
                        Variable.edudvd[place][5]-=1
                        print("AFTER :-\t",Variable.edudvd)
                        got=[sname,snumber,tid,duration]
                        print("BEFOR :-\t",Variable.lend)
                        Variable.lend.append(got)
                        print("AFTER :-\t",Variable.lend)
                        import main
                    else:
                        import main 
                        
    elif(chooce==4):
        for x in Variable.lecdvd:
            q=Variable.lecdvd.index(x)
            if (Variable.lecdvd[q][5]>0):
                print(Variable.lecdvd[q])
            else:
                continue
            
        tid=input("Enter Lecture CDs ID you want :- ")
        duration=int(input("how meny date you want it :- "))
        for x in Variable.lecdvd:
                if(tid in x):
                    w="found"
                    place=Variable.lecdvd.index(x)
                    print(Variable.lecdvd[place][4]*duration)
                    print("do you want this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        sname=input("Enter Your Name :- ")
                        snumber=input("Enter Your S Number :- ")
                        print("BEFOR :-\t",Variable.lecdvd)
                        Variable.lecdvd[place][5]-=1
                        print("AFTER :-\t",Variable.lecdvd)
                        got=[sname,snumber,tid,duration]
                        print("BEFOR :-\t",Variable.lend)
                        Variable.lend.append(got)
                        print("AFTER :-\t",Variable.lend)
                        import main
                    else:
                        import main 
                    
        
             
                    
                    