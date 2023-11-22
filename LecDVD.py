import Variable
class lecdvd:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("Please Enter Following Details For Add CD\n")
    
    
    lnumber=input("Your librarian Password :- ")
    if (lnumber==Variable.lpass):
    
        cd_number=input("CD Number :- ")
        title=input("CD title :- ")           
            
        print("Select Subject\n")
        print("\t 01\t Music ")
        print("\t 02\t Math ")
        print("\t 03\t Foreign Languages ")
        subject=""
        subc=int(input("Choose number :- "))
        
        if(subc==1):
            subject="Music"
        
        elif(subc==2):
            subject="Math"
        elif(subc==3):
            subject="Foreign Languages"
        else:
            print("Enter correct Number")
            import main
        
        RPPD=float(input("Rental Price per Day :- "))
        NOC=int(input("Number Of Copy :- "))
        
        print(Variable.lecdvd)
        
        finalarr=[cd_number,title,subject,RPPD,NOC]
        Variable.lecdvd.append(finalarr)
        
        print(Variable.lecdvd)
    else:
        print("Only librarian can add or remove resorces \n Please enter Valin Password")
        import main
        









