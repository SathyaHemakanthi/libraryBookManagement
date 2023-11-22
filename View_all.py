import Variable
class view_all:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("This resourse we have\n")
    print("\t Name \t\t\t Reg No \t Quantity \t type \t \tsubject \n")
    for i in Variable.books:
        r=Variable.books.index(i)
        print(Variable.books[r][1],"\t\t",Variable.books[r][0],"\t",Variable.books[r][5],"\t\tBook","\t\t",Variable.books[r][3])
        
    for i in Variable.magazine:
        r=Variable.magazine.index(i)
        print(Variable.magazine[r][1],"\t\t",Variable.magazine[r][0],"\t\t",Variable.books[r][5],"\t\tMagazine","\t",Variable.magazine[r][3])
        
    for i in Variable.edudvd:
        r=Variable.edudvd.index(i)
        print(Variable.edudvd[r][1],"\t\t",Variable.edudvd[r][0],"\t\t",Variable.edudvd[r][4],"\t\tEdu DVD","\t",Variable.edudvd[r][2])
        
    for i in Variable.lecdvd:
        r=Variable.lecdvd.index(i)
        print(Variable.lecdvd[r][1],"\t\t",Variable.lecdvd[r][0],"\t\t",Variable.lecdvd[r][4],"\t\tLech CD","\t",Variable.lecdvd[r][2])
        