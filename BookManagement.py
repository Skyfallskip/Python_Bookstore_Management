from Database import insert_book, view_books, delete_book, update_book

def add_book(title, author, year, isbn):
    insert_book(title, author, year, isbn)

def get_books():
    return view_books()

def remove_book(book_id):
    delete_book(book_id)

def edit_book(book_id, title, author, year, isbn):
    update_book(book_id, title, author, year, isbn)