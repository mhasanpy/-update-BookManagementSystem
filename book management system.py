books = []

while True:
# create new book
    print("1. Create new book")
    print("2. List of books")
    print("3. Sell a book")
    print("4. Update book qty")
    print("0. Exit")

    user_input = int(input("Enter your choice: "))

    if(user_input == 0): 
        print("closing the dokan")
        break

    if(user_input == 1):
        print(f"{'*'*60}")
        print(f"{'-'*21} Create new book {'-'*21}")
        print(f"{'*'*60}")

        book_name = input("Enter Book Name: ")
        book_qty = int(input("Enter Initial Book Quantity: "))

        new_book = {
            "name": book_name,
            "qty": book_qty
        }

        books.append(new_book)

        print(f"Book Name: {book_name} Successfully Added")
        print("1. Back")
        print("0. Exit")
        
        user_input_add = int(input("Enter your choice: "))
        if(user_input_add == 0): 
            print("closing the dokan")
            break


    # list of books
    if(user_input == 2):
        print(f"{'*'*60}")
        print(f"{'-'*21} List of book {'-'*21}")
        print(f"{'*'*60}")

        # print(books)
        print(f"{'-'*45}")
        print(f"|{"Book Name":^20} | {"Quantity":^20}|")
        print(f"{'-'*45}")

        for book in books:
            print(f"|{book['name']:^20} | {book['qty']:^20}|")
            print(f"{'-'*45}")

        print("1. Back")
        print("0. Exit")
    
        user_input_add = int(input("Enter your choice: "))
        if(user_input_add == 0): 
            print("closing the dokan")
            break


    # sell a book
    if(user_input == 3):
        found = False
        print(f"{'*'*60}")
        print(f"{'-'*21} Sell a Book {'-'*21}")
        print(f"{'*'*60}")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            inventory_book_name = book["name"]
            if(search_book_name == inventory_book_name):
                found = True
                print("The requested book Found!")
                
                sell_qty = int(input("Enter Sell Quantity: "))
                inventory_qty = book["qty"]

                if(sell_qty <= inventory_qty):
                    book["qty"] = inventory_qty - sell_qty
                
                break
        if(found == False):
           print("The requested book was not found")

        
        print("1. Back")
        print("0. Exit")
    
        user_input_sell = int(input("Enter your choice: "))
        if(user_input_sell == 0): 
            print("closing the dokan")
            break

    # Update book quantity
    if(user_input == 4):
        found = False
        print(f"{'*'*60}")
        print(f"{'-'*21} Update a Book {'-'*21}")
        print(f"{'*'*60}")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            inventory_book_name = book["name"]
            if(search_book_name == inventory_book_name):
                found = True
                print("The requested book Found!")
                
                update_qty = int(input("Enter update Quantity: "))  # Fixed variable name (was sell_qty)
                inventory_qty = book["qty"]

                # Fixed the condition syntax
                if(update_qty > 0):  # Removed the incorrect comparison
                    book["qty"] = inventory_qty + update_qty
                    print(f"Book quantity updated! New quantity: {book['qty']}")
                else:
                    print("Update quantity must be greater than 0")
                
                break
        
        if(found == False):
            print("The requested book was not found")

        print("1. Back")
        print("0. Exit")

        user_input_sell = int(input("Enter your choice: "))
        if(user_input_sell == 0): 
            print("closing the dokan")






"""

# update book quantity
if(user_input == 4):
    found = False 
    print(f"{'*'*60}")
    print(f"{'-'*20} Update Book Quantity {'-'*20}")
    print(f"{'*'*60}")

    search_book_name = input("Enter Book Name to Update:")

    for book in books:
        if(search_book_name == book["name"]):
            found = True
            print(f"Current quantity of '{search_book_name}': {book['qty']}")
            additional_qty = int(input("enter additional quantity to add:"))
            book["qty"] = book["qty"] + additional_qty
            print(f"Updated! New quantity of '{search_book_name}': {book['qty']}")
            break

        if(found == False):
            print("The requested book was not found")

            print("1. Back")
            print("0. Exit")

            user_input_update = int(input("Enter your choice: "))
            if(user_input_update == 0):
                print("closing the dokan")

                break


"""

"""
# Update book quantity
if user_input == 4:  
        found = False
        print(f"{'*'*60}")
        print(f"{'-'*20} Update Book Quantity {'-'*20}")
        print(f"{'*'*60}")

        search_book_name = input("Enter Book Name to update: ")

        for book in books:
            if search_book_name == book["name"]:
                found = True
                print(f"Current quantity of '{search_book_name}': {book['qty']}")

                additional_qty = int(input("Enter additional quantity to add: "))
                book["qty"] = book["qty"] + additional_qty

                print(f"Updated! New quantity of '{search_book_name}': {book['qty']}")
                break

        if not found:
            print("The requested book was not found")

        print("1. Back")
        print("0. Exit")

        user_input_update = int(input("Enter your choice: "))
        if user_input_update == 0:
            print("Closing the dokan")

          

        else:
            print("Invalid choice! Please enter 0-4")

"""










