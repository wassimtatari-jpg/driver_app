#greeting
print("Welcome to drive account application".title())

#user check
def creat_user(username):
    valid_user=["wassim","mohamed","salem"]
    block_user=["amal","hassan","ayman"]
    if username.lower()in valid_user:
        print(f'welcome {username} to the application'.title())
    elif username.lower() in block_user:
        print(f"your {username} is block".title())
    else:
        print(f"your username {username} not excist ".title())
username=input("Enter your user name all letters in lowcase :")    
creat_user(username)
    
