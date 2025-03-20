import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importando ttk separadamente
from BookManagement import add_book, get_books, remove_book, edit_book
from UserManagement import add_user, get_users, remove_user, edit_user

def refresh_book_list():
    for row in book_list.get_children():
        book_list.delete(row)
    for book in get_books():
        book_list.insert("", "end", values=book)

def refresh_user_list():
    for row in user_list.get_children():
        user_list.delete(row)
    for user in get_users():
        user_list.insert("", "end", values=user)

def add_book_command():
    add_book(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    refresh_book_list()

def remove_book_command():
    selected_item = book_list.selection()[0]
    book_id = book_list.item(selected_item)['values'][0]
    remove_book(book_id)
    refresh_book_list()

def edit_book_command():
    selected_item = book_list.selection()[0]
    book_id = book_list.item(selected_item)['values'][0]
    edit_book(book_id, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    refresh_book_list()

def add_user_command():
    add_user(name_text.get(), email_text.get())
    refresh_user_list()

def remove_user_command():
    selected_item = user_list.selection()[0]
    user_id = user_list.item(selected_item)['values'][0]
    remove_user(user_id)
    refresh_user_list()

def edit_user_command():
    selected_item = user_list.selection()[0]
    user_id = user_list.item(selected_item)['values'][0]
    edit_user(user_id, name_text.get(), email_text.get())
    refresh_user_list()

app = tk.Tk()
app.title("Library Management System")

# Book Management
book_frame = tk.LabelFrame(app, text="Book Management")
book_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(book_frame, text="Title").grid(row=0, column=0)
title_text = tk.Entry(book_frame)
title_text.grid(row=0, column=1)

tk.Label(book_frame, text="Author").grid(row=1, column=0)
author_text = tk.Entry(book_frame)
author_text.grid(row=1, column=1)

tk.Label(book_frame, text="Year").grid(row=2, column=0)
year_text = tk.Entry(book_frame)
year_text.grid(row=2, column=1)

tk.Label(book_frame, text="ISBN").grid(row=3, column=0)
isbn_text = tk.Entry(book_frame)
isbn_text.grid(row=3, column=1)

tk.Button(book_frame, text="Add Book", command=add_book_command).grid(row=4, column=0, columnspan=2)
tk.Button(book_frame, text="Remove Book", command=remove_book_command).grid(row=5, column=0, columnspan=2)
tk.Button(book_frame, text="Edit Book", command=edit_book_command).grid(row=6, column=0, columnspan=2)

book_list = ttk.Treeview(book_frame, columns=("ID", "Title", "Author", "Year", "ISBN"), show="headings")
book_list.heading("ID", text="ID")
book_list.heading("Title", text="Title")
book_list.heading("Author", text="Author")
book_list.heading("Year", text="Year")
book_list.heading("ISBN", text="ISBN")
book_list.grid(row=7, column=0, columnspan=2)

# User Management
user_frame = tk.LabelFrame(app, text="User Management")
user_frame.grid(row=0, column=1, padx=10, pady=10)

tk.Label(user_frame, text="Name").grid(row=0, column=0)
name_text = tk.Entry(user_frame)
name_text.grid(row=0, column=1)

tk.Label(user_frame, text="Email").grid(row=1, column=0)
email_text = tk.Entry(user_frame)
email_text.grid(row=1, column=1)

tk.Button(user_frame, text="Add User", command=add_user_command).grid(row=2, column=0, columnspan=2)
tk.Button(user_frame, text="Remove User", command=remove_user_command).grid(row=3, column=0, columnspan=2)
tk.Button(user_frame, text="Edit User", command=edit_user_command).grid(row=4, column=0, columnspan=2)

user_list = ttk.Treeview(user_frame, columns=("ID", "Name", "Email"), show="headings")
user_list.heading("ID", text="ID")
user_list.heading("Name", text="Name")
user_list.heading("Email", text="Email")
user_list.grid(row=5, column=0, columnspan=2)

refresh_book_list()
refresh_user_list()

app.mainloop()