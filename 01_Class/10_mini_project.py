# Mini Project using classes and Objects

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_issued = False
    
    def issue_book(self):
        
        if self.is_issued:
            print("Book already issued")
        else:
            self.is_issued = True
            print("Book issued successfully")
    
    def return_book(self):
        self.is_issued = False
        print("book returned")
        
book1 = Book("Deep Learning","Ian Goodfellow")

book1.issue_book()
book1.issue_book()
book1.return_book()