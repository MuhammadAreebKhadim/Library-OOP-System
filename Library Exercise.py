# class Library:
#     def __init__(self):
#         self.no_of_books = 0
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         self.no_of_books += 1

#     def get_no_of_books(self):
#         return self.no_of_books

#     def print_books(self):
#         for book in self.books:
#             print(book)

# # Create an instance of the Library class
# my_library = Library()

# # Add books to the library
# my_library.add_book("The Great Gatsby")
# my_library.add_book("1984")
# my_library.add_book("To Kill a Mockingbird")

# # Print all books in the library
# print("Books in the library:")
# my_library.print_books()

# # Get the number of books in the library
# print("\nNumber of books in the library:", my_library.get_no_of_books())

# Demonstrating non-persistence
# # Stop the program and run it again to see that the library starts fresh
# print("\nRestarting the program...")

# # Create a new instance of the Library class
# new_library = Library()

# # Print all books in the new library instance
# print("Books in the new library instance:")
# new_library.print_books()  # Should print nothing as the library is empty again

# # Get the number of books in the new library instance
# print("\nNumber of books in the new library instance:", new_library.get_no_of_books())  # Should be 0



# Library Program:
import emoji

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def get_no_of_books(self):
        return self.no_of_books

    def print_books(self):
        for book in self.books:
            print(book)

    def print_books_with_emojis(self):
        for book in self.books:
            print(emoji.emojize(f"{book} :books:"))

# Create an instance of the Library class
my_library = Library()

# Add books to the library
my_library.add_book("The Great Gatsby")
my_library.add_book("1984")
my_library.add_book("To Kill a Mockingbird")

# Print all books in the library
print("Books in the library:")
my_library.print_books()

# Print all books in the library with emojis
print("\nBooks in the library:")
my_library.print_books_with_emojis()

# Get the number of books in the library
print("\nNumber of books in the library:", my_library.get_no_of_books())



