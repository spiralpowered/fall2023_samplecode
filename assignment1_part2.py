class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"The book {self.title} was written by {self.author}")


if __name__ == "__main__":
    new_book = Book("Michael Lewis", "Liar's Poker")
    new_book.display()
