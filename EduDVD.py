import Variable
class edudvd:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("Please Enter Following Details For Add DVD\n")
    
    
    lnumber=input("Your librarian Password :- ")
    if (lnumber==Variable.lpass):
    
        dvd_number=input("DVD Number :- ")
        title=input("DVD title :- ")           
            
        print("Select Subject\n")
        print("\t 01\t Astronomy ")
        print("\t 02\t Math ")
        print("\t 03\t Technology ")
        subject=""
        subc=int(input("Choose number :- "))
        
        if(subc==1):
            subject="Astronomy"
        
        elif(subc==2):
            subject="Math"
        elif(subc==3):
            subject="Technology"
        else:
            print("Enter correct Number")
            import main
        
        RPPD=float(input("Rental Price per Day :- "))
        NOC=int(input("Number Of Copy :- "))
        
        print(Variable.edudvd)
        
        finalarr=[dvd_number,title,subject,RPPD,NOC]
        Variable.edudvd.append(finalarr)
        
        print(Variable.edudvd)
    else:
        print("Only librarian can add or remove resorces \n Please enter Valin Password")
        import main
        









