users = ['admin', 'steve', 'alice', 'bob']

username = []


if username:
    for user in username:
        if user in users:
            if user == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {user}, thank you for logging in again.")
        else:
            print(f"Sorry, user does not exist.")
else:
    [print("You need to enter a username.")]
