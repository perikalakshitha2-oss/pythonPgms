from book import Book
class Author:
    total_authors=0
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
        self.books=[]
        self.total_authors+=1
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,isbn):
        for book in self.books:
            if isbn==book.isbn:
                self.books.remove(book)
                return "book removed"
        return "isbn is not valid"
    def getinfo(self):
        print("Author details:",self.name,self.dob)
        for book in self.books:
            print("Book list:",book)
author1=Author("Willam Smith","1975-01-09")
book1=Book("java","wiiliam Smith",12345)
book2=Book("c++","wiiliam Smith",12346)
author1.add_book(book1)
author1.add_book(book2)
author1.getinfo()
author1.remove_book(12346)
author1.getinfo()
        
                 
