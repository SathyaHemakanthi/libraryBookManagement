import Variable


class remove():
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    a= int(input("Select resorce Type\n\n 1\tBook\n 2\tMagazines\n 3\tEducational DVDs\n 4\tLecture CDs\nEnter your choice:- "))
    
    

    y = input(" Enter Your password ")
    
    
    
    if a==1:
        if (Variable.lpass==y):
            print(Variable.books)
            w=""
            x = input(" Enter resorce registation number No :- ")
            for r in Variable.books:
                if(x in r):
                    w="found"
                    place=Variable.books.index(r)
                    Variable.books.pop(place)
                    print(Variable.books)
                    
                    
                
            if w=="found":
                print("\n Success")
                import main
            else:   
                print("Sorry,I Can't Find This Resource")
                import main
        else:
            print("you can't remove resources")
            import main
        
        
        
            
            
    elif a==2:
        if (Variable.lpass==y):
            print(Variable.magazine)
            w=""
            x = input(" Enter Resource registation number No :- ")
            for r in Variable.magazine:
                if(x in r):
                    w="found"
                    place=Variable.magazine.index(r)
                    Variable.magazine.pop(place)
                    print(Variable.magazine)
                    
                
            if w=="found":
                print("\n Success")
                import main
            else:   
                print("Sorry,I Can't Find This Resource")
                import main
        else:
            print("you can't remove resources")
            import main
            
            
    elif a==3:
        if (Variable.lpass==y):
            w=""
            print(Variable.edudvd)
            x = input(" Enter Resource registation number No :- ")
            for r in Variable.edudvd:
                if(x in r):
                    w="found"
                    place=Variable.edudvd.index(r)
                    Variable.edudvd.pop(place)
                    print(Variable.edudvd)
                    
                
            if w=="found":
                print("\n Success")
                import main
            else:   
                print("Sorry,I Can't Find This Resource")
                import main
        else:
            print("you can't remove resources")
            import main
            
            
    elif a==4:
        if (Variable.lpass==y):
            w=""
            print(Variable.lecdvd)
            x = input(" Enter Resource registation number No :- ")
            for r in Variable.lecdvd:
                if(x in r):
                    w="found"
                    place=Variable.lecdvd.index(r)
                    Variable.lecdvd.pop(place)
                    print(Variable.lecdvd)
                    
            if w=="found":
                print("\n Success")
                import main
            else:   
                print("Sorry,I Can't Find This Resource")
                import main
        else:
            print("you can't remove resources")
            import main
            
    
    else:
                print("please enter valid Details")
                import main
    