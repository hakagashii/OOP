from book import Book

class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
    
    def __str__(self):
        return f"{self.name} - {self.location}"
        

#4. Define add_book method which takes a Book instance as argument and adds it to books
#instance attribute.

    def add_book(self, book):
        self.books.append(book)

#5.. Define remove_book method which takes a Book instance as argument and removes it from
#books instance attribute.

    def remove_book(self, book):
            self.books.remove(book)

    def number_of_books(self):
            return len(self.books)

    def print_books(self):
        for book in self.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            print('\n')
        
library = Library("Hivzi Sylejmani", "Prishtinë" '\n')
print(library)


bookI = Book("emma.txt", "Tymi i votrës së fikun", "Nazmi Rrahmani", "Novel")
bookII = Book("emma.txt", "Emma", "Jane Austen", "Novel")
library.add_book(bookI)
library.add_book(bookII)
library.print_books()