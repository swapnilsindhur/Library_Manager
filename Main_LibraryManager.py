class Library:
    def __init__(self,libraryname,bookslist):
        self.name=libraryname
        self.list=bookslist
        self.dictonary={}
    def display(self):
        for c in self.list:
            print(c)

        
    def borrow(self,name,book):
        if book  not in self.dictonary.keys():
            print("you have succesfully lended the book\n")
            self.dictonary.update({book:name})
        else :
            print(f"The book is already borrowed by:{self.dictonary[book]}")
    def add(self,book):
        self.list.append(book)
        print("The book has been successfully added\n")
    def returnb(self,book):

        if book  not in self.dictonary.keys():
            print("No such book has been lended hence you cant return this\n\n")
        else:
            self.dictonary.pop(book)
            print("The book has been successfully returned\n")



        
if __name__=="__main__":
    
    swapnil=Library("swapnil",["rich dad poor dad","basics of c","pschology of money","ikigai"])
    while (True):
        print ("welcome to Library")
        a=int(input("press \n 1 - to display the books\n 2- borrow books \n 3-add books to library \n 4-to return book\n Enter your choice:"))
        if a==1:
            print("we have the following books:\n")
            swapnil.display()
        elif a==2:
            book=input("enter the name of book:\n")
            name=input("enter the your name\n")
            swapnil.borrow(name,book)
        elif a==3:
            book=input("enter the name of book:\n")
            swapnil.add(book)
        elif a==4:
            book=input("enter the name of book:\n")
            swapnil.returnb(book)
        else:
            print("invalid entry...........")
        v=input("enter q-exit and c-continue:")
        if v=="q":
            exit()
        elif v=="c":
            continue
        else :
            print("invalid entry...........so try again\nquiting............")
            exit()


        

        






    
