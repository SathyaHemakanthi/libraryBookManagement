import Variable
class receive:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("What Are You bring ?\n")
    print("\t 01\t Books")
    print("\t 02\t Magazines ")
    print("\t 03\t Educational DVDs ")
    print("\t 04\t Lecture CDs ")
    
    chooce=int(input("choose number :- "))
    
    print("Fill your details\n")
    
    
    if(chooce==1):
        for x in Variable.books:
            q=Variable.books.index(x)
            print(Variable.books[q])
            
            
        tid=input("Enter Book ID you Bring :- ")
        for x in Variable.books:
                if(tid in x):
                    w="found"
                    place=Variable.books.index(x)
                    
                    print("do you want to return this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        
                        snumber=(input("Enter Your registation Number"))
                        
                        
                        for g in Variable.lend:
                            if(snumber in g):
                                print(Variable.books)
                                Variable.books[place][5]+=1
                                print(Variable.books)
                                print(Variable.lend)
                                place=Variable.lend.index(g)
                                if(Variable.lend[place][2]==tid and Variable.lend[place][1]==snumber):
                                    Variable.lend.pop(place)
                                print(Variable.lend)
                            else:
                                print("Enter Valid Details")
                        import main
                    else:
                        import main
    elif(chooce==2):
        for x in Variable.magazine:
            q=Variable.magazine.index(x)
            print(Variable.magazine[q])
            
            
        tid=input("Enter Magazines ID you Bring")
        for x in Variable.magazine:
                if(tid in x):
                    w="found"
                    place=Variable.magazine.index(x)
                    print("do you want to return this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        snumber=input("Enter Your S Number")
                        
                        for g in Variable.lend:
                            if(snumber in g):
                                print(Variable.magazine)
                                Variable.magazine[place][5]+=1
                                print(Variable.magazine)
                                print(Variable.lend)
                                place=Variable.lend.index(g)
                                if(Variable.lend[place][2]==tid and Variable.lend[place][1]==snumber):
                                    Variable.lend.pop(place)
                                print(Variable.lend)
                            else:
                                print("Enter Valid Details")
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
            
        tid=input("Enter Educational DVDs ID you Bring")
        for x in Variable.edudvd:
                if(tid in x):
                    w="found"
                    place=Variable.edudvd.index(x)
                    print("do you want to return this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        snumber=input("Enter Your S Number")
                        for g in Variable.lend:
                            if(snumber in g):
                                print(Variable.edudvd)
                                Variable.edudvd[place][5]+=1
                                print(Variable.edudvd)
                                print(Variable.lend)
                                place=Variable.lend.index(g)
                                if(Variable.lend[place][2]==tid and Variable.lend[place][1]==snumber):
                                    Variable.lend.pop(place)
                                print(Variable.lend)
                            else:
                                print("Enter Valid Details")
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
            
        tid=input("Enter Lecture CDs ID you Bring")
        for x in Variable.lecdvd:
                if(tid in x):
                    w="found"
                    place=Variable.lecdvd.index(x)
                    print("do you want to return this\n01\tYes\n02\tNo") 
                    ask=int(input("chooce number :-")) 
                    if(ask==1):
                        snumber=input("Enter Your S Number")
                        for g in Variable.lend:
                            if(snumber in g):
                                print(Variable.lecdvd)
                                Variable.lecdvd[place][5]+=1
                                print(Variable.lecdvd)
                                print(Variable.lend)
                                place=Variable.lend.index(g)
                                if(Variable.lend[place][2]==tid and Variable.lend[place][1]==snumber):
                                    Variable.lend.pop(place)
                                print(Variable.lend)
                            else:
                                print("Enter Valid Details")
                                
                        import main
                    else:
                        import main 
                    
        
             
                    
                    