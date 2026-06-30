from models import Book, Library
from validation.validation import prompt_text, valid_isbn
from storage.csv_storage import CSV_Storage

# books = {
#     9780451524935: Book("1984", "george orwell", 9780451524935),
#     9780451526342: Book("animal farm", "george orwell", 9780451526342),
#     9780061120084: Book("mockingbird", "harper lee", 9780061120084),
#     9780743273565: Book("the great gatsby", "f. scott fitzgerald", 9780743273565),
#     9780316769488: Book("catcher in rye", "j.d. salinger", 9780316769488),
#     9780062315007: Book("the alchemist", "paulo coelho", 9780062315007),
#     9780307743657: Book("the shining", "stephen king", 9780307743657),
#     9781501142970: Book("it", "stephen king", 9781501142970),
#     9780141439518: Book("pride and prej.", "jane austen", 9780141439518),
#     9780141439662: Book("sense & sens.", "jane austen", 9780141439662),
#     9780307474278: Book("da vinci code", "dan brown", 9780307474278),
#     9781416524793: Book("angels & demons", "dan brown", 9781416524793),
#     9781594631931: Book("the kite runner", "khaled hosseini", 9781594631931),
#     9781594489501: Book("splendid suns", "khaled hosseini", 9781594489501),
#     9780547928227: Book("the hobbit", "j.r.r. tolkien", 9780547928227),
#     9780618640157: Book("the two towers", "j.r.r. tolkien", 9780618640157),
#     9780747532743: Book("hp stone", "j.k. rowling", 9780747532743),
#     9780747538486: Book("hp chamber", "j.k. rowling", 9780747538486),
#     9780064471046: Book("narnia", "c.s. lewis", 9780064471046),
#     9780066238500: Book("prince caspian", "c.s. lewis", 9780066238500),
# }

def show_add_book(library):
    title = prompt_text("Enter Book title: ")
    author = prompt_text("Enter Author: ")
    isbn = valid_isbn()

    library.add_book(title, author, isbn)
    print("Book successfully added.")

def show_remove_book(library):
    isbn = valid_isbn()

    if library.remove_book(isbn):
        print(f"Book with isbn no. {isbn} is successfully removed.")
    else:
        print(f"Book with isbn no. {isbn} is not exist in library.")

def show_borrow_book(library):
    isbn = valid_isbn()
    
    try:
        if library.borrow_book(isbn):
            print("Book successfully borrowed.")
        else:
            print("This book is not available now.")
    except ValueError as e:
        print(e)

def show_return_book(library):
    isbn = valid_isbn()

    if library.return_book(isbn):
        print("Book successfully returned.")
    else:
        print("This book is not from our library.")

def show_search(library):
    author = prompt_text("Enter Author name: ")

    library.search_by_author(author)

def show_display_available_books(library):
    library.display_available_books()


    



def menu():
    storage = CSV_Storage()
    books = storage.load_data()
    print(books)
    library = Library(books)


    print("="*100)
    print("                                   Library Management System")
    print("="*100)

    while True:
        print("\n1. Add book\n2. Remove book\n3. Borrow book\n4. Return book\n5. Search by author\n6. Display available books\n7. Exit")

        try:
            user_input = int(input("Enter your choice(1-7): "))
        except ValueError:
            print("please choose from 1-7")
            continue

        if user_input == 1:
            show_add_book(library)
            
        elif user_input == 2:
            show_remove_book(library)
            
        elif user_input == 3:
            show_borrow_book(library)
            
        elif user_input == 4:
            show_return_book(library)
            
        elif user_input == 5:
            show_search(library)
            
        elif user_input == 6:
            show_display_available_books(library)
            
        elif user_input == 7:
            storage.save_data()
            break






if __name__ == "__main__":
    menu()


