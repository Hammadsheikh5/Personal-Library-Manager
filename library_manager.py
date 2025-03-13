import os
import json

LIBRARY = "library.json"

def load_library():
    if not os.path.exists(LIBRARY):
        return []
    with open(LIBRARY , "r") as file:
        return json.load(file)

def save_book(book):
    with open(LIBRARY , "w")as file :
        json.dump(book , file ,indent=4)

def add():
    title = input("\nEnter the book title: ")
    author = input("Enter the author: ")
    # Validate year input
    while True:
        try:
            year = int(input("Enter the publication year (e.g., 1992): "))
            break  # Exit loop if input is valid
        except ValueError:
            print("❌ Invalid input! Please enter a valid year as a number (e.g., 1992).")
    genre = input("Enter the genre: ")
    # Validate read input
    while True:
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        if read_input in ["yes", "no"]:
            read = True if read_input == "yes" else False
            break
        else:
            print("❌ Invalid input! Please enter 'yes' or 'no'.")

    # Store book details
    Added_Book = {
        "title": title,
        "author":  author,
        "year": year,
        "genre":genre,
        "read" : read
    }
    return Added_Book

def greeting():
    print("\n\t\t===========================================")
    print("\t\t📚 Welcome to Your Personal Library Manager! 📖")
    print("\t\t===========================================")
    print("\t\t🔹 Manage your book collection with ease.")
    print("\t\t🔹 Add, remove, search, and track your books effortlessly.")
    print("\t\t🔹 Get reading statistics and keep your library organized!")
    print("\t\t-------------------------------------------")
    print("\t\t🚀 Let's get started! Happy reading! 🎉")
    print("\t\t-------------------------------------------\n")

greeting()
library_books = load_library()  # Load library once at the start

while True :
    Options = [
        "Add a book 📖", 
        "Remove a book ❌", 
        "Search for a book 🔍", 
        "Display all books 📚", 
        "Display statistics 📊", 
        "Mark a book as read ✅", 
        "Exit 🚪"] 
    for i, Option in enumerate(Options ,1 ):
        print(f"{i}- {Option}")
    # Get user input safely
    while True:
        try:
            Selected_Option = int(input("Enter Your Choice: "))

            # Check if the input is within the valid range
            if 1 <= Selected_Option <= len(Options):
                break  # Valid input, exit loop
            else:
                print("❌ Invalid choice! Please select a number between 1 and 6.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
   

    if Selected_Option == 1:
        Added_Book = add()
        print(f"{Added_Book['title']} by {Added_Book['author']} ({Added_Book['year']}) - {Added_Book['genre']} - {Added_Book["read"]}")
        library_books.append(Added_Book)
        save_book(library_books)
        print("Book added Succesfully\n")


    elif Selected_Option == 2:      
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else:
            remove_book_title = input("\nEnter the title of the book to remove: ")
            book_found = False  # Flag to check if the book exists
            for book in library_books:
                if remove_book_title.lower() == book["title"].lower():  # Case insensitive match
                    print("\n✅ Book found:")
                    print(f"{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]}")
                    library_books.remove(book)
                    save_book(library_books)
                    print("\n📕 Book removed successfully\n")
                    book_found = True
                    break  # Exit loop after finding the book
            if not book_found:
                print("\n❌ Book not found! Please check the title and try again.\n")


    elif Selected_Option == 3:
        options = ["🔤 Title", "🖊️ Author"]
        print("\n\t\t🔍 Search By : ")
        for i, option in enumerate(options,1) :
            print(f"\t\t{i}. {option}")
        # print("\n")
        while True:
            try:
                search_option = int(input("\nEnter Your Choices 1 or 2 : "))
                if 1 <= search_option <= len(options):
                    break
                else:
                    print("❌ Invalid choice! Please select a number 1 or 2 only.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        search_key = "title" if search_option == 1 else "author"
        user_input = input(f"Enter the {options[search_option - 1]}: ")

        for i, book in enumerate(library_books, 1):
            if user_input.lower() == book[search_key].lower():
                print("\n\t📚 Matching Book:")
                read = "Read" if book["read"] else "Unread"
                emoji = "✅" if book["read"] else "📖"
                print(f"\n\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read} {emoji}\n")
                break
        else:
            print("\n❌ Book not found! Please check the input and try again.\n")


    elif Selected_Option == 4:
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else :
            print("\n\t\t📖 Your Books in Library 📚:\n")
            for i, book in enumerate(library_books, 1):  
                read = "Read" if book["read"] else "Unread"
                emoji = "✅" if book["read"] else "📖"
                print(f"\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read}{emoji}")
            print("\n")


    elif Selected_Option == 5:
        print("\n\t\t📊 Statistics 📊\n")
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else:
            count = 0
            for book in library_books:
                if book["read"]:
                    count = count + 1

            # count = sum(1 for book in library_books if book["read"]) 
            # {We also use this}
            total = len(library_books)
            percentage : float = count *100 / total
            print(f"\t\t📚 Total Books in Library: {total}")
            print(f"\t\t✅ Percentage Read: {percentage:.2f}% 📖")
        print("\n")


    elif Selected_Option == 6:
        print("\n\t\t📖 Mark a Book as Read ✅\n")
        user_title = input("🔎 Enter The Book Title : ")
        for i, book in enumerate(library_books, 1):
            if user_title.lower() == book["title"].lower():
                print("\n\t📚 Matching Book:")
                read = "Read" if book["read"] else "Unread"
                emoji = "✅" if book["read"] else "📖"
                print(f"\n\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read} {emoji}\n")
                if book["read"] :
                    print("\t⚡ You have already read this book!\n")
                    break
                else :
                    while True:
                        mark_read = input("📝 Mark as Read (yes/no) : ")
                        if mark_read.lower()=="yes":
                            book["read"]= True
                            save_book(library_books)
                            print(f"\n ✅ You mark this book as read\n")
                            break
                        elif mark_read.lower() == "no":
                            print("\n❌ Book was not marked as read.\n")
                            break
                        else:
                            print("\n⚠️ Invalid input! Please enter 'yes' or 'no'.\n")
                    break
        else:
            print("\n❌ Book not found! Please check the input and try again.\n")        
                

    elif Selected_Option == 7:
        print("\n\t\t📚 Library saved to file successfully! ✅")
        print("\t\t----------------------------------------")
        print("\t\t💡 Tip: Keep reading and exploring new books! 📖")
        print("\t\tThank you for using the Library System! 🙌")
        print("\t\t----------------------------------------")
        break