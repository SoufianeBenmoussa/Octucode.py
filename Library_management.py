import os
def cln():
    os.system("cls" if os.name == "nt" else "clear")

book = {}

def add_book():
    while True:
        cln()
        isbn = input("Enter ISBN: ")
        author = input("Enter AUTHOR: ")
        title = input("Enter TITLE: ")
        book[isbn] = {"title":title, "author":author, "avalibale":True}
        print(f'Book {title} by {author} added to the catalog with ISBN {isbn}')
        choice = input("Do you want to add anothor book y/n? ")
        if choice != 'y':
            break

def check_out():
    while True:
        cln()
        isbn = input('Enter ISBN to check out: ')
        if isbn not in book:
            not_in = input('This book is not in the catalog do you want to add another ISBN y/n? ')
            if not_in == 'y':
                continue
            break
        if not book[isbn]['avalibale']:
            not_check = input('This book is already check out do you want to add another ISBN y/n? ')
            if not_check == 'y':
                continue
            break
        print('This book has checked out successfully')
        book[isbn]['avalibale'] = False
        another = input('Do you want to check out another book y/n? ')
        if another != 'y':
            break

def check_in():
    while True:
        cln()
        isbn = input('Enter ISBN to check in: ')
        if isbn not in book:
            not_in = input('This book is not in the catalog do you want to add another ISBN y/n? ')
            if not_in == 'y':
                continue
            break
        if  book[isbn]['avalibale']:
            not_check = input('This book is already check in do you want to add another ISBN y/n? ')
            if not_check == 'y':
                continue
            break
        print('This book has checked in successfully')
        book[isbn]['avalibale'] = True
        another = input('Do you want to check out another book y/n? ')
        if another != 'y':
            break

def show_list():
    cln()
    print('Library Catalog: ')
    for isbn in book:
        print(f'ISBN: {isbn}, Title: {book[isbn]["title"]}, Author: {book[isbn]["author"]}, Avalibale: {book[isbn]["avalibale"]}')

while True:
    cln()
    print('Menu:\n ')
    print('1. Add a book')
    print('2. Check out a book')
    print('3. Check in a book')
    print('4. List books')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if   choice == '1':
        add_book()
    elif choice == '2':
        check_out()
    elif choice == '3':
        check_in()
    elif choice == '4':
        show_list()
    elif choice == '5':
        break
    else:
        print('Invalid choice')
    input('Press any key to continue...')