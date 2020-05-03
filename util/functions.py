import calendar
import time
from models.Order import *

# Some Dummy orders to test some of the functions
order1 = Order("Birthday1", (3, 21, 2020), (7, 20, 2020), 2, "red", "started", 1000)
order2 = Order("Birthday2", (1, 11, 2020), (7, 20, 2020), 1, "yellow", "started", 1000)
order3 = Order("Birthday3", (7, 30, 2020), (7, 20, 2020), 2, "red", "started", 20000)
order4 = Order("party1", (2, 1, 2020), (7, 20, 2020), 2, "red", "started", 32000)
order5 = Order("Wedding1", (5, 12, 2020), (7, 20, 2020), 1, "green", "started", 25000)
order6 = Order("Wedding2", (6, 17, 2020), (7, 20, 2020), 1, "yellow", "started", 15000)

daisy_orders = {order1.id: order1, order2.id: order2, order3.id: order3,
                order4.id: order4, order5.id: order5, order6.id: order6}


# General Program Function
# Function that keeps the program running depending on the users choice
def user_status_type():
    user_status = input("Do you want to continue? Y/N\n").lower()
    if user_status == 'n' or user_status == 'no':
        exit()
    return user_status


# Function that presents menu and deals with menu option
def user_main_menu():
    print("=====Welcome to Daisy's Planner=====")
    print("========= Menu Options =============")
    print("1. Enter Order\n" +
          "2. View Orders\n" +
          "3. Delete Orders\n" +
          "4. Update Orders\n"
          "5. Clear Orders\n")
    userOption = int(input("Enter a number corresponding to the option you want:"))
    if userOption == 1:
        enter_order()
        user_status_type()
    elif userOption == 2:
        view_orders()
        user_status_type()
    elif userOption == 3:
        delete_order()
        user_status_type()
    elif userOption == 4:
        update_order()
        user_status_type()
    elif userOption == 2:
        clear_order()
        user_status_type()
    else:
        print("The option you chose is invalid.")


# Function to collect instant variables and creates order instance
def enter_order():
    result = time.localtime()
    order_title = input("Enter the title: \n")
    order_due_date = pick_date()
    order_time_stamp = (result.tm_mday, result.tm_mon, result.tm_year)
    order_labour = int(input("How many people are assigned to this task?(enter a number) \n"))
    order_code = input("Enter order code(Red, Yellow, Green):\n")
    order_status = input("Enter order status: \n")
    order_price = int(input("Enter the price of this order:\n"))
    new_order = Order(order_title, order_due_date, order_time_stamp, order_labour, order_code, order_status,
                      order_price)
    daisy_orders[new_order.id] = new_order


# Function that displays the orders
def view_orders():
    index = 1
    for order in daisy_orders:
        print(str(index) + ". " + order)
        index += 1


# delete function that deletes orders from Daisy's scheduler in case a customer
def delete_order():
    view_orders()
    delete = input("Which order do you want to delete?\n")
    for order in daisy_orders:
        if delete == order:
            print(daisy_orders[order].title + " has been removed.")
            daisy_orders.pop(order)
            break


# update function that enables Daisy to make edits to the details of the order
def update_order():
    pass


# mark_as_done function that moves all completed orders to the paid list
def clear_order():
    pass


# Function that gets the date from the user
def pick_date():
    result = time.localtime()
    # Give the user the option if it is towards the end of the month to place their order to the next month
    if 25 < result.tm_mday < 31:
        user_input = input("Is the order due next month?(Yes/No)")
        # Display next month and get user input
        if user_input == "yes" or user_input == "Yes":
            print(calendar.month(result.tm_year, result.tm_mon + 1))
            day = int(input("Enter the order's due day(1-7): "))
            date = int(input("Enter the order's due date(1-31): "))
            return day, date, result.tm_year
        # Display current month and get user input
        elif user_input == "no" or user_input == "No":
            print(calendar.month(result.tm_year, result.tm_mon))
            day = int(input("Enter the order's due day(1-7): "))
            date = int(input("Enter the order's due date(1-31): "))
            return day, date, result.tm_year
        else:
            return "The option you entered is invalid"

    else:
        print(calendar.month(result.tm_year, result.tm_mon))
        day = int(input("Enter the order's due day(1-7): "))
        date = int(input("Enter the order's due date(1-31): "))
        return day, date, result.tm_year
