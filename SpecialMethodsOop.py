class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    #string representation of the object
    def __str__(self):

        return f"{self.title} by {self.author}"

    #length of the object
    def __len__(self):

        return self.pages

    def __del__(self):

        print("A book object has been deleted")

book= Book("Mistborn","Brandon Sanderson",400)
book_two= Book("Stormlight Archive","Brandon Sanderson",1000)
print(book)
print(len(book))

print(book_two)
print(len(book_two))

#Deleting the book from the memory
del book_two

