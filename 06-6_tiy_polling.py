favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

participant = ['jen', 'sarah', 'jack', 'steve']
for name in favorite_languages.keys():
    if name in participant:
        print(f"{name.title()}, thank you for participating in the poll.")
    else:
        print(f"{name.title()}, please complete the poll.")