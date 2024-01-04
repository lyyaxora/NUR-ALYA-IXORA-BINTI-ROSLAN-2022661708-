import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="order_data"
)

mycursor = mydb.cursor()

def place_order():
    Book_title = title_var.get()
    Quantity = int(quantity_entry.get())
    Price = Quantity * 10
    Name = name_entry.get()
    Customer_id = id_entry.get()

    # Insert order details into the database
    sql = "INSERT INTO orders (Book_title, Quantity, Price, Name, Customer_id) VALUES (%s, %s, %s, %s, %s)"
    val = (Book_title, Quantity, Price, Name, Customer_id)
    mycursor.execute(sql, val)
    mydb.commit()

    result_label.config(text = f"Thank you for ordering {Quantity} copies of ' {Book_title} ', {Name}. Total cost: RM{Price}")

root = tk.Tk()
root.title("Book Order")
root.geometry('600x500')
root.configure(bg='#ADD8E6')

label = tk.Label(root, text='ALIF BOOKSTORE', font=("Bahnschrift SemiBold",18, "bold"), bg='#ADD8E6')
label.pack(ipadx=10, ipady=10)

bt_text = tk.Text(root, height=10, width=50, bg='#E5E4E2')
bt_text.pack(pady=10)

bt_text.insert(tk.END, "AVAILABLE BOOKS (RM10 each):\n\n")
bt_text.insert(tk.END, "The Power of Now:\nIf you build the habit of focusing on the NOW, youwill find effortless joy and natural energy.\n\n")
bt_text.insert(tk.END, "The Brain That Changes Itself:\nThe erroneous ideas about the brain's inability toheal were believed to be true by brain experts anddoctors for decades.\n\n")
bt_text.insert(tk.END, "Wizards of Ice:\nWizards of Ice is a tale of adventure, friendship,and the enduring power of hope."f"Will Alaric and hiscompanions unlock the secrets of the prophecy in time to save Eldoria, or will they succumb to the icy grip of an ancient evil?\n\n")
bt_text.insert(tk.END, "A Potion For The Wise:\nA Potion For The Wise is a spellbinding tale that explores the timeless themes of courage, growth, and the enduring magic that lies within each individual.\n")
bt_text.configure(state='disabled')


# Predefined book titles
book_titles = ["The Power of Now", "The Brain That Changes Itself", "Wizards of Ice", "A Potion For The Wise"]

frame = tk.Frame(root, bg='#ADD8E6')
frame.pack()

# Frame 1
cust_frame =tk.LabelFrame(frame, text="Customer Details", bg='#95B9C7')
cust_frame.grid(row= 0, column=0, sticky="news", padx=20, pady=10)

name_label = tk.Label(cust_frame, text="Name:", bg='#95B9C7')
name_label.pack()
name_entry = tk.Entry(cust_frame)
name_entry.pack()


id_label = tk.Label(cust_frame, text="ID:", bg='#95B9C7')
id_entry = tk.Entry(cust_frame)
id_label.pack()
id_entry.pack()

for widget in cust_frame.winfo_children():
    widget.pack_configure(padx=15, pady=5)

#Frame2
book_order_frame = tk.LabelFrame(frame, text = "Order", bg='#95B9C7')
book_order_frame.grid(row= 0, column=2, padx=20, pady=10)

# Title input using dropdown menu
title_label = tk.Label(book_order_frame, text="Book Title:", bg='#95B9C7')
title_label.pack()

title_var = tk.StringVar(book_order_frame)
title_var.set(book_titles[0])  # Set the default book title

title_dropdown = tk.OptionMenu(book_order_frame, title_var, *book_titles)
title_dropdown.pack()

# Quantity input
quantity_label = tk.Label(book_order_frame, text = "Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(book_order_frame)
quantity_entry.pack()

for widget in book_order_frame.winfo_children():
    widget.pack_configure(padx=15, pady=5)

# Button to place order
order_button = tk.Button(root, text = "Place Order", command = place_order)
order_button.pack()

# Display result label
result_label = tk.Label(root, text = "", bg='#ADD8E6')
result_label.pack()

#Run
root.mainloop()