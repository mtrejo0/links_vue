import requests
import json
import random
import time

class API():

    def __init__(self):
        self.users_file = 'users.json'
       
        self.items_file = 'items.json'
        self.new_item_id = 0
        
        # users = []
        # items = [
        #     {
        #     "name": "6.170 Final Project",
        #     "tags": ["school", "project"],
        #     "link": "",
        #     "description": "fdsfd",
        #     "link": "https://www.google.com",
        #     "id": -1,
        #     "username": "moi"
        #     },
        #     {
        #     "name": "Twitter SWE",
        #     "tags": ["school", "project"],
        #     "link": "",
        #     "description": "",
        #     "link": "https://www.google.com",
        #     "id": -2,
        #     "username": "moi"
        #     },
        #     {
        #     "name": "6.170 Final Project",
        #     "tags": ["school", "project"],
        #     "link": "",
        #     "description": "",
        #     "id": -3,
        #     "username": "moi"
        #     },
        # ]
        # with open(self.items_file, 'w') as f:
        #     json.dump(items, f)
        # with open(self.users_file, 'w') as f:
        #     json.dump(users, f)

    ## ITEMS

    def get_items(self, username = None):
        with open(self.items_file) as f:
            items = json.load(f)
            if not username is None:
                items = [item for item in items if item["username"] == username]
            return items
    
    def save_items(self, items):
        with open(self.items_file, 'w') as f:
            json.dump(items, f)
        
    
    def add_item(self, item):
        item['id'] = self.new_item_id
        self.new_item_id += 1
        item["timestamp"] = time.time()
        self.save_items(self.get_items() + [item])
        return item
        

    def delete_item(self, id):
        id = int(id)
        items = [ item for item in self.get_items() if not item['id'] == id]
        self.save_items(items)
    
    

    ## USERS

    def get_users(self):
         with open(self.users_file) as f:
            return json.load(f)
    
    def save_users(self, users):
        with open(self.users_file, 'w') as f:
            json.dump(users, f)

    def create_user(self, username, password):
        self.is_valid_user(username, password)

        new_user = {
            'username': username,
            'password': password
        }
        self.save_users(self.get_users() + [new_user])
        return new_user
    
    def is_valid_user(self,username, password):
        assert not self.user_exists(username), "Username already exists!"
        assert len(username) >= 3, "Username needs to be at least 3 characters!"
        assert len(password) >= 3, "Password needs to be at least 3 characters!"

    def user_exists(self, username):
        for user in self.get_users():
            if user['username'] == username:
                return True
        return False
    
    def read_user(self, username, password):
        for user in self.get_users():
            if user['username'] == username and user['password'] == password:
                return user
        raise Exception("Wrong username or password!")

    def delete_user(self, username):
        self.users = [user for user in self.get_users() if not user["username"] == username]


if __name__ == "__main__":
    pass
    

