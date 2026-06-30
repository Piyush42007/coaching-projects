class Book:
    def __init__(self, title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available == False:
            return False
        self.is_available = False
        return True
    
    def return_book(self):
        self.is_available = True

    



    
