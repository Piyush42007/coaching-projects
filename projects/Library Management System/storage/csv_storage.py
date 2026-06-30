import csv
import os
from models.Book import Book

FILEPATH = "data/library.csv"

class CSV_Storage:
    books = {}

    def load_data(self):
        if not os.path.exists(FILEPATH):
            print("Can't find storage(csv) file!")
            return
        
        with open(FILEPATH, "r") as f:
            reader = csv.reader(f)

            for title,author,isbn,is_availability in reader:
                CSV_Storage.books[int(isbn)] = Book(title,author,int(isbn),bool(is_availability))
        return CSV_Storage.books

        

    def save_data(self):
        if not os.path.exists(FILEPATH):
            print("Can't find storage(csv) file!")
            return

        with open(FILEPATH, "w", newline="") as f:
            writer = csv.writer(f)

            for book in CSV_Storage.books.values():
                writer.writerow([book.title, book.author, book.isbn, book.is_available])
    


