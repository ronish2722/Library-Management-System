import random
import datetime
'''Importing random and datetime fucntion'''


def display():
    """Displaying available books"""
    # Opening the txt file for reading only
    file = open("books.txt", "r")
    # Reading all the items present in file
    lines = file.read()
    # Displaying books
    print('-----------------------')
    print("Books: ")
    print()
    print(lines)
    print()
    # Closing the file
    file.close()


def borrow_bill(ran_id, cus_name, b_book, l_book, tot):
    """Creates bill for borrowing books"""
    print('Thank you!!!!!')
    # Opening new file for writing only to create bill
    file_receipt = open(f"{ran_id}bill.txt", "w")
    # Creating a bill layout
    file_receipt.write(f"-------LIBRARY-------\n")
    file_receipt.write(f"\n")
    file_receipt.write(f"Bill Number: {ran_id}\n")
    file_receipt.write(f'Date of Issue: {datetime.date.today()}  \n')
    file_receipt.write(f'Time of Issue: {datetime.datetime.now().time()} \n')
    file_receipt.write(f'Bill To: {cus_name}\n')
    file_receipt.close()
    file_receipt2 = open(f"{ran_id}bill.txt", "a")
    file_receipt2.write(f"-----------------------------\n")
    file_receipt2.write(f"Books Purchased\n")
    for i in range(len(b_book)):
        file_receipt2.write(f'{b_book[i]} --------> {l_book[i]} pieces\n')
    file_receipt2.write(f"-----------------------------\n")
    file_receipt2.write(f'Total Cost: ${tot}\n')


def return_bill_late(ran_id, cus_name, b_book, l_book, ask_time):
    """Creates bill for returning book late"""
    # Calculating fine for the customer
    days = ask_time - 10
    fine = days * 1.5
    # Opening new file for writing only to create bill
    file_receipt = open(f"{ran_id}bill.txt", "w")
    # Creating a bill layout
    file_receipt.write("-------LIBRARY-------\n")
    file_receipt.write("\n")
    file_receipt.write(f"Bill Number: {ran_id}\n")
    file_receipt.write(f'Date of Issue: {datetime.date.today()}  \n')
    file_receipt.write(f'Time of Issue: {datetime.datetime.now().time()} \n')
    file_receipt.write(f'Bill To: {cus_name}\n')
    file_receipt.close()
    file_receipt2 = open(f"{ran_id}bill.txt", "a")
    file_receipt2.write("-----------------------------\n")
    file_receipt2.write("Books Returned\n")
    for i in range(len(b_book)):
        file_receipt2.write(f'{b_book[i]} --------> {l_book[i]} pieces\n')
    file_receipt2.write(f'-----------------------------\n')
    file_receipt2.write(f'As you have not submitted your book on time\n')
    file_receipt2.write(f'Fine: ${fine}')


def return_bill(ran_id, cus_name, b_book, l_book):
    """Creates bill for returning book on time"""
    file_receipt = open(f"{ran_id}bill.txt", "w")
    file_receipt.write("-------LIBRARY-------\n")
    file_receipt.write("\n")
    file_receipt.write(f"Bill Number: {ran_id}\n")
    file_receipt.write(f'Date of Issue: {datetime.date.today()}  \n')
    file_receipt.write(f'Time of Issue: {datetime.datetime.now().time()} \n')
    file_receipt.write(f'Bill To: {cus_name}\n')
    file_receipt.close()
    file_receipt2 = open(f"{ran_id}bill.txt", "a")
    file_receipt2.write("-----------------------------\n")
    file_receipt2.write("Books Returned\n")
    for i in range(len(b_book)):
        file_receipt2.write(f'{b_book[i]} --------> {l_book[i]} pieces\n')
    file_receipt2.write(f'----------------------------\n')
    file_receipt2.write(f'Thank you!! \n')
    file_receipt2.write(f'Please Visit Again.')


def borrow():
    """This module handles the borrowing action"""
    # Opening the txt file for reading only
    file = open("books.txt", "r")
    # Reading the items from txt file and putting them in list
    lines = file.readlines()
    # Closing the file
    file.close()
    # Declaring necessary lists and variables
    data = []
    confirm = ''
    book_names = []
    list_borrowed_book = []
    list_number_book = []
    total_all = 0
    # Generating random number for bill
    random_id = str(int(random.random() * 100000))

    # Creating  a 2d list
    for line in lines:
        line = line.replace('$', '')
        data.append(line.replace('\n', '').split(','))

        # Changing the String variable in list to int and float
        for i in range(len(data)):
            data[i][2] = int(data[i][2])
            data[i][3] = float(data[i][3])

    # Adding all the available book names to a list
    for b in range(len(data)):
        book_names.append(data[b][0].lower())
         
    customer_name = input('Enter your name: ')
    # Until confirm = n the loop should continue
    while confirm.lower() != "n":
        confirm = input('Do you want to borrow books?(Y/N)')

        # When confirm = y
        if confirm.lower() == 'y':
            borrow_book = input('Which book do you want to borrow: ')
            
            # Check if the inputted book name by user matches the book name from list
            if borrow_book.lower() in book_names:
                # Add the inputted book name by user to a new list
                list_borrowed_book.append(borrow_book.lower())
                # Exception Handling
                while True:
                    try:
                        number_book = int(input('How many books do you want to borrow: '))

                        # If user gives negative value show error
                        if number_book <= 0:
                            print(f'Enter a valid value.')
                        else:
                            break
                    except:
                        # If user gives invalid input show error
                        print(f'Enter a valid value.')
                # Add number of books borrowed to list
                list_number_book.append(number_book)

                # Calculating total and updating the values after borrowing
                for i in range(len(data)):
                    if borrow_book.lower() == data[i][0].lower():
                        total_ = number_book * data[i][3]
                        total_all = total_all + total_
                        data[i][2] = data[i][2] - number_book
                        break

            else:
                print('Enter a valid book name')

        # When user inputs n as confirm
        elif confirm.lower() == 'n':
            if len(list_borrowed_book) != 0:
                # Calling function borrow_bill
                borrow_bill(random_id, customer_name, list_borrowed_book, list_number_book, total_all)
                print(f'The ID number for your bill is {random_id}')

        else:
            print('Enter valid value')
            
    # Updating txt file
    file_stockbooks = open('books.txt', 'w')
    file_stockbooks.write(f"Harry Potter,JK Rowling,{data[0][2]},$2\n")
    file_stockbooks.write(f"Start With Why,Simon Sinek,{data[1][2]},$1.5 \n")
    file_stockbooks.write(f"Programming With Python,John Smith,{data[2][2]},$1.5\n")
    file_stockbooks.write(f"In Search of Lost Time,Marcel Proust,{data[3][2]},$2\n")
    file_stockbooks.write(f"Ulysses,James Joyce,{data[4][2]},$1\n")
    file_stockbooks.write(f"Don Quixote,Miguel de Cervantes,{data[5][2]},$2\n")
    file_stockbooks.close()


def return_():
    """This module handles the returning action"""
    # Opening the txt file for reading only
    file = open("books.txt", "r")
    # Reading the items from txt file and putting them in list
    lines = file.readlines()
    # Closing the file
    file.close()
    # Declaring necessary lists and variables
    data = []
    confirm = ''
    book_names = []
    list_borrowed_book = []
    list_number_book = []
    # Generating random number for bill
    random_id = str(int(random.random() * 100000))
    
    # Creating  a 2d list
    for line in lines:
        line = line.replace('$', '')
        data.append(line.replace('\n', '').split(','))

        # Changing the String variable in list to int and float
        for i in range(len(data)):
            data[i][2] = int(data[i][2])
            data[i][3] = float(data[i][3])

    # Adding all the available book names to a list
    for b in range(len(data)):
        book_names.append(data[b][0].lower())

    customer_name = input('Enter your name: ')
    # Until confirm = n the loop should continue
    while confirm.lower() != "n":
        confirm = input('Do you want to return books?(Y/N)')

        # When confirm = y
        if confirm.lower() == 'y':
            return_book = input('Which book do you want to return: ')

            # Check if the inputted book name by user matches the book name from list
            if return_book.lower() in book_names:
                # Add the inputted book name by user to a new list
                list_borrowed_book.append(return_book.lower())
                # Exception Handling
                while True:
                    try:
                        number_book = int(input('How many books do you want to return: '))
                        # If user gives negative value show error
                        if number_book <= 0:
                            print(f'Enter a valid value.')
                        else:
                            break
                    except:
                        # If user gives invalid input show error
                        print(f'Enter a valid value.')
                # Add number of books borrowed to list
                list_number_book.append(number_book)

                # Updating the values after returning
                for i in range(len(data)):
                    if return_book.lower() == data[i][0].lower():
                        data[i][2] = data[i][2] + number_book
                        break

            else:
                print('Enter a valid book name')

        # When user inputs n as confirm
        elif confirm.lower() == 'n':
            while True:
                try:
                    # Asking the user for the days they have had the book
                    ask_time = int(input('For how long have you had this book?'))
                    break
                except:
                    print(f'Enter a valid value')
            # If user had book for more than 10 days calculating fine
            if ask_time > 10:
                days = ask_time - 10
                fine = days * 1.5
                # Calling the fucntion return_bill_late
                return_bill_late(random_id, customer_name, list_borrowed_book, list_number_book, ask_time)
                print(f'Your fine will be : $ {fine}\n')
                print(f'The bill number for your bill is {random_id}')

            else:
                # Else callinf the function return_bill
                return_bill(random_id, customer_name, list_borrowed_book, list_number_book)
                print(f'The bill number for your bill is {random_id}')

        else:
            print('Enter valid value')
            
    # Updating txt file
    file_stockbooks = open('books.txt', 'w')
    file_stockbooks.write(f'Harry Potter,JK Rowling,{data[0][2]},$2\n')
    file_stockbooks.write(f"Start With Why,Simon Sinek,{data[1][2]},$1.5 \n")
    file_stockbooks.write(f"Programming With Python,John Smith,{data[2][2]},$1.5\n")
    file_stockbooks.write(f"In Search of Lost Time,Marcel Proust,{data[3][2]},$2\n")
    file_stockbooks.write(f"Ulysses,James Joyce,{data[4][2]},$1\n")
    file_stockbooks.write(f"Don Quixote,Miguel de Cervantes,{data[5][2]},$2\n")
    file_stockbooks.close()
