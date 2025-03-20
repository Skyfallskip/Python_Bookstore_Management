from Database import insert_user, view_users, delete_user, update_user

def add_user(name, email):
    insert_user(name, email)

def get_users():
    return view_users()

def remove_user(user_id):
    delete_user(user_id)

def edit_user(user_id, name, email):
    update_user(user_id, name, email)