import webbrowser
website = input("Search Website: ")

if website == "google":
    name = input("Search: ")
    webbrowser.open("https://www.google.com/search?q=" +name)
elif website == "youtube":
    name =input("Search: ")
    webbrowser.open("https://www.youtube.com/results?search_query=" + name)
