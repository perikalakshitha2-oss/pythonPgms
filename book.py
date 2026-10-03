class Book:
    total_books=0
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        Book.total_books+=1
    def updateTitle(self,newtitle):
        self.title=newtitle
    def updateAuthor(self,newauthor):
        self.author=newauthor
    @classmethod
    def bookCount(cls):
        return cls.total_books
    def bookInfo(self):
        print("Book details:",self.title,self.author,self.isbn,self.total_books)
    def __str__(self):
        return "Book details:"+self.title+self.author
book1=Book("java","wiiliam Smith",12345)
#book1.bookInfo()
book1.updateTitle("New_java")
#book1.bookInfo()
