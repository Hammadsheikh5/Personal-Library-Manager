import os
import json

# File where the library data is stored
LIBRARY = "library.txt"

def load_library():
    """Loads the library data from the JSON file. If the file doesn't exist, returns an empty list."""
    if not os.path.exists(LIBRARY):
        return [] # Return an empty list if the file doesn't exist
    with open(LIBRARY , "r") as file:   # Open the file in read mode
        return json.load(file) # Load and return the JSON data

def save_book(book):
    """Saves the current library data to the JSON file.
        Functionality:
    - Opens the JSON file in write mode.
    - Dumps the book list into the file in JSON format.
    - Uses indentation for better readability.
    """
    with open(LIBRARY , "w")as file :           # Open the file in write mode  
        json.dump(book , file ,indent=4)        # Save the book list with indentation for readability

def add():
    """Prompts the user to enter book details and returns a dictionary with the book's information."""
    title = input("\nEnter the book title: ")
    author = input("Enter the author: ")
    # Validate year input (must be a valid integer)
    while True:
        try:
            year = int(input("Enter the publication year (e.g., 1992): "))
            break  # Exit loop if input is valid
        except ValueError:
            print("❌ Invalid input! Please enter a valid year as a number (e.g., 1992).")
    genre = input("Enter the genre: ")
    #  Validate read status (user must enter 'yes' or 'no')
    while True:
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        if read_input in ["yes", "no"]:
            read = True if read_input == "yes" else False  # Convert input to boolean
            break
        else:
            print("❌ Invalid input! Please enter 'yes' or 'no'.")

    # Store book details in a dictionary
    Added_Book = {
        "title": title,
        "author":  author,
        "year": year,
        "genre":genre,
        "read" : read
    }
    return Added_Book  # Return the new book data

def greeting():
    """Displays a welcome message for the library system."""
    print("\n\t\t===========================================")
    print("\t\t📚 Welcome to Your Personal Library Manager! 📖")
    print("\t\t===========================================")
    print("\t\t🔹 Manage your book collection with ease.")
    print("\t\t🔹 Add, remove, search, and track your books effortlessly.")
    print("\t\t🔹 Get reading statistics and keep your library organized!")
    print("\t\t-------------------------------------------")
    print("\t\t🚀 Let's get started! Happy reading! 🎉")
    print("\t\t-------------------------------------------\n")

# Display welcome message
greeting()
# Load library data at the start of the program
library_books = load_library()  # Load library once at the start

# Main loop for user interaction
while True :
    # Define available options
    Options = [
        "Add a book 📖", 
        "Remove a book ❌", 
        "Search for a book 🔍", 
        "Display all books 📚", 
        "Display statistics 📊", 
        "Mark a book as read ✅", 
        "Exit 🚪"] 
    # Display menu options
    for i, Option in enumerate(Options ,1 ):
        print(f"{i}- {Option}")
    # Get user input safely
    while True:
        try:
            Selected_Option = int(input("Enter Your Choice: "))
            # Validate the selected option
            # Check if the input is within the valid range 
            if 1 <= Selected_Option <= len(Options):
                break  # Exit loop if input is valid
            else:
                print("❌ Invalid choice! Please select a number between 1 and 6.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
   
    # Option 1: Add a new book
    if Selected_Option == 1:
        # Call the add() function to get book details from the user
        Added_Book = add()
        # Display the added book's details
        print(f"{Added_Book['title']} by {Added_Book['author']} ({Added_Book['year']}) - {Added_Book['genre']} - {Added_Book["read"]}")
        library_books.append(Added_Book)   # Add book to the list
        save_book(library_books)    # Save updated list to file
        print("Book added Succesfully\n")


    # Option 2: Remove a book from the library
    elif Selected_Option == 2:   
        # Check if the library has any books before attempting removal   
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else:
             # Prompt user to enter the title of the book they want to remove
            remove_book_title = input("\nEnter the title of the book to remove: ")
            book_found = False  # Flag to check if the book exists
            # Iterate through the list of books to find a match
            for book in library_books:
                # Perform a case-insensitive match to find the book
                if remove_book_title.lower() == book["title"].lower():  # Case insensitive match
                    print("\n✅ Book found:")
                    # Display details of the book to be removed
                    print(f"{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]}")
                    library_books.remove(book)  # Remove the book from the list
                    save_book(library_books)    # Save updated list to file
                    print("\n📕 Book removed successfully\n")
                    book_found = True
                    break  # Exit loop after finding and removing the book
            # If no matching book is found, inform the user
            if not book_found:
                print("\n❌ Book not found! Please check the title and try again.\n")


    # Option 3: Search for a book
    elif Selected_Option == 3:
        options = ["🔤 Title", "🖊️ Author"]
        print("\n\t\t🔍 Search By : ")
        # Display search options
        for i, option in enumerate(options,1) :
            print(f"\t\t{i}. {option}")
        # Get user search preference
        while True:
            try:
                search_option = int(input("\nEnter Your Choices 1 or 2 : "))
                if 1 <= search_option <= len(options):
                    break
                else:
                    print("❌ Invalid choice! Please select a number 1 or 2 only.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        #  Determine search key (title or author) based on user selection
        search_key = "title" if search_option == 1 else "author"
         # Prompt user to enter search input
        user_input = input(f"Enter the {options[search_option - 1]}: ")
         # Search for the book in the library
        for i, book in enumerate(library_books, 1):
            # Convert both user input and book data to lowercase to ensure case-insensitive matching
            if user_input.lower() == book[search_key].lower():
                print("\n\t📚 Matching Book:")
                read = "Read" if book["read"] else "Unread"         # Determine if the book has been read or not
                emoji = "✅" if book["read"] else "📖"             # Assign emoji based on read status
                # Display book details with formatting
                print(f"\n\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read} {emoji}\n")
                break   # Exit loop after finding the first match
        else:
            print("\n❌ Book not found! Please check the input and try again.\n")


    # Option 4: Display all books in the library
    elif Selected_Option == 4:
        # Check if the library is empty
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else :
            print("\n\t\t📖 Your Books in Library 📚:\n")
            # Loop through the library and display each book's details
            for i, book in enumerate(library_books, 1):  
                read = "Read" if book["read"] else "Unread"     # If book["read"] is True, assign "Read", otherwise assign "Unread"
                emoji = "✅" if book["read"] else "📖"  # ✅ for read, 📖 for unread
                # Display book details with index number
                print(f"\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read}{emoji}")
            print("\n")


    # Option 5: Display statistics
    elif Selected_Option == 5:
        print("\n\t\t📊 Statistics 📊\n")   # Header for statistics section
        # Check if there are any books in the library
        if not library_books:
            print("\n\t\t📚 No books in the library yet! 📭\n")
        else:
            count = 0   # Initialize a counter for read books
            # Loop through the library and count books that have been read
            for book in library_books:
                if book["read"]:    # Check if the book is marked as read
                    count = count + 1       # Increment the counter

            # count = sum(1 for book in library_books if book["read"]) 
            # {We also use this}

            total = len(library_books)    # Get the total number of books in the library
            percentage : float = count *100 / total       # Calculate the percentage of books that have been read
            print(f"\t\t📚 Total Books in Library: {total}")    # Display the total number of books
            print(f"\t\t✅ Percentage Read: {percentage:.2f}% 📖")      # Display the percentage of books read with 2 decimal places
        print("\n")


    # Option 6: Mark a book as read
    elif Selected_Option == 6:
        # Prompt user to enter the title of the book they want to mark as read
        print("\n\t\t📖 Mark a Book as Read ✅\n")
        user_title = input("🔎 Enter The Book Title : ")
         # Iterate through the library to find the book
        for i, book in enumerate(library_books, 1):
            # Check if the book title matches (case insensitive)
            if user_title.lower() == book["title"].lower():
                print("\n\t📚 Matching Book:")
                 # Determine the reading status of the book
                read = "Read" if book["read"] else "Unread"
                emoji = "✅" if book["read"] else "📖"
                 # Display the book details
                print(f"\n\t{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read} {emoji}\n")
                if book["read"] :
                    # If the book is already marked as read, notify the user
                    print("\t⚡ You have already read this book!\n")
                    break   # Exit loop as no further action is needed
                else :
                    # Loop to validate user input for marking as read
                    while True:
                        mark_read = input("📝 Mark as Read (yes/no) : ")
                        # If user confirms, mark the book as read and save changes
                        if mark_read.lower()=="yes":  
                            book["read"]= True      # Update the book's read status
                            save_book(library_books)        # Save updated library data
                            print(f"\n ✅ Book marked as read!\n")
                            break       # Exit the validation loop
                        # If user chooses 'no', do not mark the book as read
                        elif mark_read.lower() == "no":
                            print("\n❌ Book was not marked as read.\n")
                            break       # Exit the validation loop
                        # Handle invalid inputs
                        else:
                            print("\n⚠️ Invalid input! Please enter 'yes' or 'no'.\n")
                    break  # Exit the main loop after processing the book
        # If the book is not found in the library, inform the user
        else:
            print("\n❌ Book not found! Please check the input and try again.\n")        


    # Option 7: Exit the program
    elif Selected_Option == 7:
        print("\n\t\t📚 Library saved to file successfully! ✅")
        print("\t\t----------------------------------------")
        print("\t\t💡 Tip: Keep reading and exploring new books! 📖")
        print("\t\tThank you for using the Library System! 🙌")
        print("\t\t----------------------------------------")
        break