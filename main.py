import tkinter as tk
from tkinter import messagebox

user_database = {'admin': 'password123'}
petrol_prices = {'AI92': 1.6, 'AI 95': 1.6, 'Dizel': 1.6, 'Premium': 1.6}
food_prices = {'Hot Dog': 2.2, 'Col': 5, 'Gamburger': 3.7}

selected_items = {'petrol': None, 'food': None, 'liters': 0, 'food_quantity': 0}

def reset_password():
    messagebox.showinfo('Reset Password', 'Password reset functionality is not implemented yet.')

def register_page():
    def register_user():
        new_username = username.get()
        new_password = password.get()
        repeat_new_password = repeat_password.get()

        if new_password == repeat_new_password:
            user_database[new_username] = new_password
            print("Registration successful!")
            register_frame.pack_forget()  
            login_page()  
        else:
            print("Passwords do not match")

    register_frame = tk.Frame(root)

    username_lb = tk.Label(register_frame, text='Enter Username', font=('Bold', 12))
    username_lb.grid(row=0, column=0, padx=10, pady=10)

    username = tk.Entry(register_frame,
                        font=('Bold', 15),
                        bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.grid(row=0, column=1, padx=10, pady=10)

    password_lb = tk.Label(register_frame, text='Enter Password', font=('Bold', 12))
    password_lb.grid(row=1, column=0, padx=10, pady=10)

    password = tk.Entry(register_frame, font=('Bold', 15),
                        bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray',
                        show='*')
    password.grid(row=1, column=1, padx=10, pady=10)

    repeat_password_lb = tk.Label(register_frame, text='Repeat Password', font=('Bold', 12))
    repeat_password_lb.grid(row=2, column=0, padx=10, pady=10)

    repeat_password = tk.Entry(register_frame, font=('Bold', 15),
                               bd=0, highlightcolor='#158aff',
                               highlightthickness=2, highlightbackground='gray',
                               show='*')
    repeat_password.grid(row=2, column=1, padx=10, pady=10)

    register_btn = tk.Button(register_frame, text='Register', font=('Bold', 12),
                             bg='#158aff', fg='white', command=register_user)
    register_btn.grid(row=3, column=1, pady=10)

    register_frame.pack(pady=10)
    register_frame.pack_propagate(False)
    register_frame.configure(height=400, width=250)

def login_page():
    def authenticate_user():
        entered_username = username.get()
        entered_password = password.get()

        if entered_username in user_database and user_database[entered_username] == entered_password:
            print("Login successful!")
            login_frame.pack_forget()  
            if entered_username == 'admin':
                admin_page()
            else:
                user_page()
        else:
            print("Invalid username or password")

    login_frame = tk.Frame(root)

    username_lb = tk.Label(login_frame, text='Enter Username', font=('Bold', 12))
    username_lb.grid(row=0, column=0, padx=10, pady=10)

    username = tk.Entry(login_frame,
                        font=('Bold', 15),
                        bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.grid(row=0, column=1, padx=10, pady=10)

    password_lb = tk.Label(login_frame, text='Enter Password', font=('Bold', 12))
    password_lb.grid(row=1, column=0, padx=10, pady=10)

    password = tk.Entry(login_frame, font=('Bold', 15),
                        bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray',
                        show='*')
    password.grid(row=1, column=1, padx=10, pady=10)

    login_btn = tk.Button(login_frame, text='Login', font=('Bold', 12),
                          bg='#158aff', fg='white', command=authenticate_user)
    login_btn.grid(row=2, column=1, pady=10)

    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)
    login_frame.configure(height=400, width=250)

def user_page():
    def buy_petrol():
        selected_items['petrol'] = petrol_var.get()
        selected_items['liters'] = float(liters_entry.get())
        result_label.config(text=f"Petrol: {selected_items['petrol']}, Liters: {selected_items['liters']}")

    def buy_food():
        selected_items['food'] = food_var.get()
        selected_items['food_quantity'] = int(food_quantity_entry.get())
        result_label.config(text=f"Food: {selected_items['food']}, Quantity: {selected_items['food_quantity']}")

    def calculate_total():
        petrol_price = petrol_prices[selected_items['petrol']] * selected_items['liters']
        food_price = food_prices[selected_items['food']] * selected_items['food_quantity']
        total_price = petrol_price + food_price
        result_label.config(text=f"Total Price: {total_price:.2f}")

    user_frame = tk.Frame(root)

    petrol_var = tk.StringVar()

    petrol_label = tk.Label(user_frame, text='Select Petrol:')
    petrol_label.grid(row=0, column=0, padx=10, pady=10)

    petrol_options = list(petrol_prices.keys())
    petrol_menu = tk.OptionMenu(user_frame, petrol_var, *petrol_options)
    petrol_menu.grid(row=0, column=1, padx=10, pady=10)

    liters_label = tk.Label(user_frame, text='Enter Liters:')
    liters_label.grid(row=1, column=0, padx=10, pady=10)

    liters_entry = tk.Entry(user_frame)
    liters_entry.grid(row=1, column=1, padx=10, pady=10)

    buy_petrol_btn = tk.Button(user_frame, text='Buy Petrol', command=buy_petrol)
    buy_petrol_btn.grid(row=2, column=1, pady=10)

    food_var = tk.StringVar()
    food_label = tk.Label(user_frame, text='Select Food:')
    food_label.grid(row=3, column=0, padx=10, pady=10)

    food_options = list(food_prices.keys())
    food_menu = tk.OptionMenu(user_frame, food_var, *food_options)
    food_menu.grid(row=3, column=1, padx=10, pady=10)

    food_quantity_label = tk.Label(user_frame, text='Enter Quantity:')
    food_quantity_label.grid(row=4, column=0, padx=10, pady=10)

    food_quantity_entry = tk.Entry(user_frame)
    food_quantity_entry.grid(row=4, column=1, padx=10, pady=10)

    buy_food_btn = tk.Button(user_frame, text='Buy Food', command=buy_food)
    buy_food_btn.grid(row=5, column=1, pady=10)

    calculate_total_btn = tk.Button(user_frame, text='Order', command=calculate_total)
    calculate_total_btn.grid(row=6, column=1, pady=10)

    result_label = tk.Label(user_frame, text='')
    result_label.grid(row=7, column=0, columnspan=2, pady=10)

    user_frame.pack()
    user_frame.pack_propagate(False)
    user_frame.configure(height=400, width=250)

def admin_page():
    def show_petrol_prices():
        print("Petrol Prices:")
        for petrol, price in petrol_prices.items():
            print(f"{petrol}: {price}")

    def show_food_prices():
        print("Food Prices:")
        for food, price in food_prices.items():
            print(f"{food}: {price}")

    def delete_petrol():
        petrol_to_delete = delete_petrol_entry.get()
        if petrol_to_delete in petrol_prices:
            del petrol_prices[petrol_to_delete]
            print(f"{petrol_to_delete} deleted.")
        else:
            print(f"{petrol_to_delete} not found.")

    def delete_food():
        food_to_delete = delete_food_entry.get()
        if food_to_delete in food_prices:
            del food_prices[food_to_delete]
            print(f"{food_to_delete} deleted.")
        else:
            print(f"{food_to_delete} not found.")

    def add_petrol():
        new_petrol = new_petrol_entry.get()
        new_price = new_petrol_price_entry.get()

        try:
            new_price = float(new_price)
            petrol_prices[new_petrol] = new_price
            print(f"{new_petrol} added with price {new_price}.")
        except ValueError:
            print("Invalid price. Please enter a number.")

    def add_food():
        new_food = new_food_entry.get()
        new_price = new_food_price_entry.get()

        try:
            new_price = float(new_price)
            food_prices[new_food] = new_price
            print(f"{new_food} added with price {new_price}.")
        except ValueError:
            print("Invalid price. Please enter a number.")

    admin_frame = tk.Frame(root)

    show_petrol_prices_btn = tk.Button(admin_frame, text='Show Petrol Prices', command=show_petrol_prices)
    show_petrol_prices_btn.grid(row=0, column=0, pady=10)

    show_food_prices_btn = tk.Button(admin_frame, text='Show Food Prices', command=show_food_prices)
    show_food_prices_btn.grid(row=1, column=0, pady=10)

    delete_petrol_label = tk.Label(admin_frame, text='Delete Petrol:')
    delete_petrol_label.grid(row=2, column=0, padx=10, pady=10)

    delete_petrol_entry = tk.Entry(admin_frame)
    delete_petrol_entry.grid(row=2, column=1, padx=10, pady=10)

    delete_petrol_btn = tk.Button(admin_frame, text='Delete Petrol', command=delete_petrol)
    delete_petrol_btn.grid(row=3, column=0, pady=10)

    delete_food_label = tk.Label(admin_frame, text='Delete Food:')
    delete_food_label.grid(row=4, column=0, padx=10, pady=10)

    delete_food_entry = tk.Entry(admin_frame)
    delete_food_entry.grid(row=4, column=1, padx=10, pady=10)

    delete_food_btn = tk.Button(admin_frame, text='Delete Food', command=delete_food)
    delete_food_btn.grid(row=5, column=0, pady=10)

    add_petrol_label = tk.Label(admin_frame, text='Add Petrol:')
    add_petrol_label.grid(row=6, column=0, padx=10, pady=10)

    new_petrol_entry = tk.Entry(admin_frame)
    new_petrol_entry.grid(row=6, column=1, padx=10, pady=10)

    new_petrol_price_label = tk.Label(admin_frame, text='Price:')
    new_petrol_price_label.grid(row=7, column=0, padx=10, pady=10)

    new_petrol_price_entry = tk.Entry(admin_frame)
    new_petrol_price_entry.grid(row=7, column=1, padx=10, pady=10)

    add_petrol_btn = tk.Button(admin_frame, text='Add Petrol', command=add_petrol)
    add_petrol_btn.grid(row=8, column=0, pady=10)

    add_food_label = tk.Label(admin_frame, text='Add Food:')
    add_food_label.grid(row=9, column=0, padx=10, pady=10)

    new_food_entry = tk.Entry(admin_frame)
    new_food_entry.grid(row=9, column=1, padx=10, pady=10)

    new_food_price_label = tk.Label(admin_frame, text='Price:')
    new_food_price_label.grid(row=10, column=0, padx=10, pady=10)

    new_food_price_entry = tk.Entry(admin_frame)
    new_food_price_entry.grid(row=10, column=1, padx=10, pady=10)

    add_food_btn = tk.Button(admin_frame, text='Add Food', command=add_food)
    add_food_btn.grid(row=11, column=0, pady=10)

    admin_frame.pack()
    admin_frame.pack_propagate(False)
    admin_frame.configure(height=400, width=250)

root = tk.Tk()
root.title('Tkinter Hub')

register_page()
login_page()

root.mainloop()
