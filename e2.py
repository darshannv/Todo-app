import  webbrowser

user_term = input("Enter the search word: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)