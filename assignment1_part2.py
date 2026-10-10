
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author)



if __name__ == "__main__":
    a = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    a.display()
    b = Book("Walter Scott", "Ivanhoe: A Romance")
    b.display()
    print("This is a assignment 1 part 2")
