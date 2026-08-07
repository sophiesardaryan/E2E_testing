import json
from library.data import books_info

#First option
def display_books(books_info):
    print(json.dumps(books_info, indent=4))

# #Second otion
# def display_books():
#     for key, value in books_info.items():
#         print(f"{key}: {value}")


def add_book(title,author,page,year):
    if title not in books_info:
        books_info[title] = {
            "author" : author,
            "page" : page,
            "year": year
        }
    else:
        print("Book with this title already exists")

def get_book(title):
    if title in books_info:
        print(books_info[title])
    else:
        print(f"Book with {title} title is not exist")


def delete_book(title):
    if title in books_info:
        del books_info[title]
        print(f"The {title} book is deleted")
    else:
        print(f"There is no a book with this {title} title")
