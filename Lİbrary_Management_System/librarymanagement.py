class Book:
    #attributes of book

    def __init__(self, title, author, year, pages) -> None:
        
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    #returns attributes of book as string
    def __str__(self) -> str:
        
        return f"{self.title},{self.author},{self.year},{self.pages}"

class Library:

    def __init__(self) -> None:
        #opens the txt file
        self.file = open('books.txt', 'a+')
    
    def __del__(self):
        #closes the file
        self.file.close()
    
    def list_books(self):

        self.file.seek(0)
        
        #stores each string on a new line in a list
        books = self.file.read().splitlines()

        if len(books) == 0:
            print("File is empty!")
        
        else:
            for book in books:
                title, author, year, pages = book.split(',')
                print(f"Title: {title}, Author: {author}")
    
    
    def add_book(self, book):
        
        self.file.write(str(book) + "\n")
    

    def remove_book(self, title_to_remove):

        self.file.seek(0)
        books = self.file.read().splitlines()
        books = [book for book in books if book.split(',')[0] != title_to_remove]
        self.file.truncate(0)
        self.file.seek(0)
        for book in books:
            self.file.write(f"{book}\n")

class Program:

    def main():
        lib = Library()

        print("===Library Management System===")
        user_choice = input("Press enter to continue...")

        while user_choice != "q":

            print("===Menu===")
            print("[1] List Books")
            print("[2] Add Book")
            print("[3] Remove Book")
            print("[q] Quit")

            user_choice = input("Enter your choice: ")

            match user_choice.lower():

                case "1":

                    print("==Book List==")
                    lib.list_books()

                        
        
                case "2":
            
                    print("==Add Book==")
            
                    b_title = input("Enter title of the book: ")
                    b_author = input("Enter the author of the book: ")
                    b_year = input("Enter year of release of the book: ")
                    b_pages = input("Enter number of pages of the book: ")
            
                    book = Book(b_title.title(), b_author.title(), b_year, b_pages)
                    lib.add_book(book)
            
            
                case "3":
            
                    print("==Remove Book==")
                    b_title_to_remove = input("Enter the title of the book that you want to remove: ")
                    lib.remove_book(b_title_to_remove.title())
            
                
                case "q":
                
                    break

        
                case _:
                    print("Please choose from options of the menu.")



Program.main()