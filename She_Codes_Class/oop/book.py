#class is a way to make a blueprint for something. imagine books are digital, kindle load a book on it.
#has a bunch of properties - title, number of pages
#you actually open another book, bookmark on page 239, different author, different word count etc
#open another book different again
#while books different from each other have similar attributes - can have a class

class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1 #don't need to pass iin as have hard value
        self.specific_page = 5

    def go_to_specific_page_number(self):
        self.specific_page

    def move_bookmark(self):
        self.bookmarked_page = self.current_page
    
    def turn_page(self, forward):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def __len__(self):
        return self.num_pages

book_1 = Book("Cats", "Real Person", 213, 1)
print(book_1.current_page)
book_1.turn_page(True)
print(book_1.current_page)
book_1.turn_page(False)
print(book_1.current_page)

book_1.turn_page(True)
book_1.turn_page(True)
book_1.turn_page(True)
book_1.move_bookmark()
book_1.turn_page(True)
print(book_1.current_page, book_1.bookmarked_page)

# print(book_1.title)
# print(book_1.author)
# print(book_1.num_pages)

# book_2 = Book("Dogs", "Fake Person", 198, 1)
# print(book_2.title)

# print(book_1)
# print(len(book_1))

#book_1 = Book()
#shecodes_book = Book("python for shecodes", "hayley", 1024, 1)
#get user input
#which_page = input("which page are you on?")
#call method on class with value from user input
#shecodes_book.set_page(which_page)