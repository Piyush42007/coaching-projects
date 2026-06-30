from models.Book import Book

class Library():
    def __init__(self, books: dict):
        self.books = books

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books[isbn] = book

    def remove_book(self, isbn):
        if isbn not in self.books:
            return False
        self.books.pop(isbn)
        return True

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError(f"Book with isbn no. {isbn} is not exist in library.")
        
        book = self.books[isbn]
        if book.borrow_book():
            return True
        else:
            return False

    def return_book(self, isbn):
        if isbn not in self.books:
            return False
        book = self.books[isbn]
        book.return_book()
        return True

    def search_by_author(self, author):
        result = ""
        for book in self.books.values():
            if author in book.author:
                result += f"{book.title:<25}{ book.author:<25}{book.isbn:<18}{book.is_available}\n"

        if result:
            print("\nTitle                    Author                   Isbn no.          available")
            print("-"*80)
            print(result)
        else:
            print(f"No book by {author} in our library.")

                



    def display_available_books(self):
        result = ""
        for book in self.books.values():
            if bool(book.is_available) == True:
                result += f"{book.title:<25}{ book.author:<25}{book.isbn:<18}{book.is_available}\n"

        if result:
            print("\nTitle                    Author                   Isbn no.          available")
            print("-"*80)
            print(result)
        else:
            print("No book available now.")

    

        