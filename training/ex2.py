from book import Book
library = [
    Book("Толстой", "Война и мир"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

for book in library:
    print(f"{book.name} - {book.author}")