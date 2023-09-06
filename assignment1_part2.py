class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"case 1 = The book {self.title} was written by {self.author}")
        print("case 2 = The book {v1} was written by {v2}".format(v1=self.title, v2=self.author))


if __name__ == "__main__":
    new_book = Book("Michael Lewis", "Liar's Poker")
    new_book.display()
