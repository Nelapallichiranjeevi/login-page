
users={'user1':'password1','user2':'password2','user3':'password3'}

def login():
    while True:
        print("Welcome")
        username=input("enter your name:")
        password=input("enter your password:")

        if username in users and users[username]==password:
            print("login successfully")
        else:
            print("login failed")

login()              