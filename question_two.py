class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages =pages

Book1 = Book("The Amazing Facts", "Gordan MC", 150)

print(Book1.title)
print(Book1.author)
print(Book1.pages)


#EBook
class EBook:
    def __init__(self, title, author, pages, format):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format

EBook1 = EBook("The Amazing Facts", "Gordan MC", 150, "Novel")

print(EBook1.title)
print(EBook1.author)
print(EBook1.pages)
print(EBook1.format)

#Returns book title and its author

Book = Book1.title
Book = Book1.author

print(f"BOOK TITLE: {Book1.title}")
print(f"BOOK AUTHOR: {Book1.author}")

#Class is like the title like here the class is (title,author,pages,format)
#Object is like the sub-title (Amazing Facts, GordanMC, 150, novel)
        