import Variable


class book:
    print("\t--------------------------")
    print("\tWelcome TO OUSL library System")
    print("\t--------------------------\n")
    print("Please Enter Following Details For Add Book\n")

    lnumber = input("Your librarian Password :- ")
    if (lnumber == Variable.lpass):

        isbn_number = input("ISBN Number :- ")
        title = input("Book title :- ")
        print("Select Book Subject\n")
        print("\t 01\t Science ")
        print("\t 02\t History ")
        print("\t 03\t Literature ")
        subject = ""
        subc = int(input("Choose number :- "))

        if (subc == 1):
            subject = "Science"

        elif (subc == 2):
            subject = "History"
        elif (subc == 3):
            subject = "Literature"
        else:
            print("Enter correct Number")
            import main

        print("Select Book format\n")
        print("\t 01\t Hardcover ")
        print("\t 02\t Paperback ")
        formatc = int(input("Choose number :- "))
        format = ""
        if (formatc == 1):
            format = "Hardcover"

        elif (formatc == 2):
            format = "Paperback"
        else:
            print("Enter correct Number")
            import main

        RPPD = int(input("Rental Price per Day :- "))
        NOC = int(input("Number Of Copy :- "))

        # print(Variable.books)

        for x in Variable.books:
            if (isbn_number in x):
                if (title in x):
                    place = Variable.books.index(x)
                    Variable.books[place][5] += 1
                else:
                    print("This ISBN Number Alredy Exists")
            else:
                finalarr = [isbn_number, title, subject, format, RPPD, NOC]
                Variable.books.append(finalarr)
                break

        print(Variable.books)
        import main
    else:
        print("Only librarian can add or remove resorces \n Please enter Valin Password")
        import main
