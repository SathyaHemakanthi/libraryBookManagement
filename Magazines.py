import Variable
class magazines:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("Please Enter Following Details For Add Magazine\n")
    
    
    lnumber=input("Your librarian Password :- ")
    if (lnumber==Variable.lpass):
    
        m_number=input("Magazine Number :- ")
        title=input("Magazine title :- ")
        
        print("Select Magazine Color\n")
        print("\t 01\t Color ")
        print("\t 02\t Black & white ")
        color=""
        colcc=int(input("Choose number :- "))
        
        if(colcc==1):
            color="Color"
        
        elif(colcc==2):
            color="Black & white"
        else:
            print("Enter correct Number")
            import main
            
            
        print("Select Book Subject\n")
        print("\t 01\t Science ")
        print("\t 02\t Technology ")
        print("\t 03\t Sports ")
        subject=""
        subc=int(input("Choose number :- "))
        
        if(subc==1):
            subject="Science"
        
        elif(subc==2):
            subject="Technology"
        elif(subc==3):
            subject="Sports"
        else:
            print("Enter correct Number")
            import main
        
        RPPD=float(input("Rental Price per Day :- "))
        NOC=int(input("Number Of Copy :- "))
        
        print(Variable.magazine)
        
        finalarr=[m_number,title,color,subject,RPPD,NOC]
        Variable.magazine.append(finalarr)
        
        print(Variable.magazine)
    else:
        print("Only librarian can add or remove resorces \n Please enter Valin Password")
        import main
        









