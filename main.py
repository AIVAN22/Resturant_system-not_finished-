import tkinter
from tkinter import NW, NO, RIGHT, LEFT, CENTER, TOP, ttk, NE
from PIL import Image, ImageTk
import mysql.connector


con = mysql.connector.connect(host="localhost", user="root", password=" ", database=" ")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS orders (table_id TEXT,bill TEXT)")
con.commit()


menu = {
    "salad": [
        ["Caesar Salad", 8.99],
        ["Spinach Salad", 7.99],
        ["Greek Salad", 9.99],
    ],
    "meal": [
        ["Cheeseburger", 10.99],
        ["Grilled Chicken Sandwich", 9.99],
        ["Fish and Chips", 12.99],
    ],
    "soda": [
        ["Coke", 1.99],
        ["Sprite", 1.99],
        ["Lemonade", 2.99],
    ],
    "drinks": [
        ["Cabernet Sauvignon", 5.99],
        ["Chardonnay", 5.99],
        ["Merlot", 5.99],
    ],
    "dessert": [
        ["Cheesecake", 4.99],
        ["Chocolate Cake", 5.99],
        ["Ice Cream Sundae", 3.99],
    ],
}


root = tkinter.Tk()
root.title("Order System")
root.geometry("960x500")
root.resizable(False, False)
root.config(background="#088a88")


orders = []


def Table():

    frame_mid_2.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()


def Menu():
    frame_mid.grid(row=1, column=1, sticky="WENS")
    frame_mid_2.grid_forget()
    frame_salad.grid_forget()
    frame_soda.grid_forget()
    frame_drinks.grid_forget()
    frame_dessert.grid_forget()
    frame_meal.grid_forget()


def salad():
    frame_salad.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()
    frame_mid_2.grid_forget()


def meal():

    frame_meal.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()
    frame_mid_2.grid_forget()
    frame_salad.grid_forget()


def soda():
    frame_soda.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()
    frame_mid_2.grid_forget()
    frame_salad.grid_forget()


def drink():
    frame_drinks.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()
    frame_mid_2.grid_forget()
    frame_salad.grid_forget()


def dessert():
    frame_dessert.grid(row=1, column=1, sticky="WENS")
    frame_mid.grid_forget()
    frame_mid_2.grid_forget()
    frame_salad.grid_forget()


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)
root.rowconfigure(2, weight=1)


# icon images
photo_salad = Image.open("./salad.png")
photo_meal = Image.open("./meal.png")
photo_soda = Image.open("./soda.png")
photo_drinks = Image.open("./drinks.png")
photo_dessert = Image.open("./dessert.png")


photo_salad = photo_salad.resize((105, 85))
photo_meal = photo_meal.resize((105, 85))
photo_soda = photo_soda.resize((105, 85))
photo_drinks = photo_drinks.resize((105, 85))
photo_dessert = photo_dessert.resize((105, 85))


photo_salad = ImageTk.PhotoImage(photo_salad)
photo_meal = ImageTk.PhotoImage(photo_meal)
photo_soda = ImageTk.PhotoImage(photo_soda)
photo_drinks = ImageTk.PhotoImage(photo_drinks)
photo_dessert = ImageTk.PhotoImage(photo_dessert)


frame_top = tkinter.Frame(root, background="red")
frame_mid = tkinter.Frame(root, background="red")
frame_bottom = tkinter.Frame(root, background="red")
frame_left = tkinter.Frame(root, background="lightblue")
frame_right = tkinter.Frame(root, background="pink")
#   GRID


frame_top.grid(row=0, column=1, sticky="WENS")
frame_mid.grid(row=1, column=1, sticky="WENS")
frame_bottom.grid(row=2, column=1, sticky="WENS")
frame_left.grid(row=0, column=0, rowspan=3, sticky="WENS")
frame_right.grid(row=0, column=2, rowspan=3, sticky="WENS")


frame_mid.columnconfigure(0, weight=1)
frame_mid.columnconfigure(1, weight=1)
frame_mid.columnconfigure(2, weight=1)
frame_mid.columnconfigure(3, weight=1)


frame_mid.rowconfigure(0, weight=1)
frame_mid.rowconfigure(1, weight=1)
frame_mid.rowconfigure(2, weight=1)


frame_left.columnconfigure(0, weight=1)


frame_left.rowconfigure(0, weight=1)
frame_left.rowconfigure(1, weight=1)
frame_left.rowconfigure(2, weight=1)
frame_left.rowconfigure(3, weight=1)
frame_left.rowconfigure(4, weight=1)
frame_left.rowconfigure(5, weight=4)


# MIDDLE DESSERT
frame_dessert = tkinter.Frame(root, background="red")
frame_dessert.columnconfigure(0, weight=1)
frame_dessert.columnconfigure(1, weight=1)
frame_dessert.columnconfigure(2, weight=1)
frame_dessert.columnconfigure(3, weight=1)

frame_dessert.rowconfigure(0, weight=1)
frame_dessert.rowconfigure(1, weight=1)
frame_dessert.rowconfigure(2, weight=1)

# DESSERT BUTT
def take_order_dessert(id_dessert):
    found = False
    for i, order_item in enumerate(orders):
        if order_item[0] == menu["dessert"][id_dessert][0]:
            found = True
            break

    if not found:
        orders.append(
            [menu["dessert"][id_dessert][0], menu["dessert"][id_dessert][1], 1]
        )
    else:
        orders[i][-1] += 1

    item_values = menu["dessert"][id_dessert]
    if orders:
        item_values.append(orders[-1][-1])
    else:
        item_values.append(1)
    bill.insert("", "end", values=item_values)


commands_desserts = menu["dessert"]
COLUMNS = 4
for i, item in enumerate(commands_desserts):
    id_dessert = i
    dessert_button = tkinter.Button(
        frame_dessert, bg="yellow", command=lambda id=id_dessert: take_order_dessert(id)
    )
    row, column = divmod(i, COLUMNS)
    dessert_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# MIDDLE DRINKS
frame_drinks = tkinter.Frame(root, background="red")
frame_drinks.columnconfigure(0, weight=1)
frame_drinks.columnconfigure(1, weight=1)
frame_drinks.columnconfigure(2, weight=1)
frame_drinks.columnconfigure(3, weight=1)

frame_drinks.rowconfigure(0, weight=1)
frame_drinks.rowconfigure(1, weight=1)
frame_drinks.rowconfigure(2, weight=1)


# DRINKS BUTT
commands_drinks = menu["drinks"]


def take_order_drinks(id_drinks):
    found = False
    for i, order_item in enumerate(orders):
        if order_item[0] == menu["drinks"][id_drinks][0]:
            found = True
            break

    if not found:
        orders.append([menu["drinks"][id_drinks][0], menu["drinks"][id_drinks][1], 1])
    else:
        orders[i][-1] += 1

    item_values = menu["drinks"][id_drinks]
    if orders:
        item_values.append(orders[-1][-1])
    else:
        item_values.append(1)
    bill.insert("", "end", values=item_values)


COLUMNS = 4
for i, item in enumerate(commands_drinks):
    id_drink = i
    drink_button = tkinter.Button(
        frame_drinks, bg="yellow", command=lambda id=id_drink: take_order_drinks(id)
    )
    row, column = divmod(i, COLUMNS)
    drink_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# MIDDLE SODA
frame_soda = tkinter.Frame(root, background="red")
frame_soda.columnconfigure(0, weight=1)
frame_soda.columnconfigure(1, weight=1)
frame_soda.columnconfigure(2, weight=1)
frame_soda.columnconfigure(3, weight=1)

frame_soda.rowconfigure(0, weight=1)
frame_soda.rowconfigure(1, weight=1)
frame_soda.rowconfigure(2, weight=1)
# SODA BUTT
def take_order_soda(id_soda):
    found = False
    for i, order_item in enumerate(orders):
        if order_item[0] == menu["soda"][id_soda][0]:
            found = True
            break

    if not found:
        orders.append([menu["soda"][id_soda][0], menu["soda"][id_soda][1], 1])
    else:
        orders[i][-1] += 1

    item_values = menu["soda"][id_soda]
    if orders:
        item_values.append(orders[-1][-1])
    else:
        item_values.append(1)
    bill.insert("", "end", values=item_values)


commandss_sodas = menu["soda"]
COLUMNS = 4
for i, item in enumerate(commandss_sodas):
    id_soda = i
    soda_button = tkinter.Button(
        frame_soda, bg="yellow", command=lambda id=id_soda: take_order_soda(id)
    )
    row, column = divmod(i, COLUMNS)
    soda_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# MIDDLE MEAL
frame_meal = tkinter.Frame(root, background="red")
frame_meal.columnconfigure(0, weight=1)
frame_meal.columnconfigure(1, weight=1)
frame_meal.columnconfigure(2, weight=1)
frame_meal.columnconfigure(3, weight=1)

frame_meal.rowconfigure(0, weight=1)
frame_meal.rowconfigure(1, weight=1)
frame_meal.rowconfigure(2, weight=1)

# MEAL BUTT
def take_order_meal(id_meal):
    found = False
    for i, order_item in enumerate(orders):
        if order_item[0] == menu["meal"][id_meal][0]:
            found = True
            break

    if not found:
        orders.append([menu["meal"][id_meal][0], menu["meal"][id_meal][1], 1])
    else:
        orders[i][-1] += 1

    item_values = menu["meal"][id_meal]
    if orders:
        item_values.append(orders[-1][-1])
    else:
        item_values.append(1)
    bill.insert("", "end", values=item_values)


commands_meals = menu["meal"]
COLUMNS = 4
for i, item in enumerate(commands_meals):
    id_meal = i
    meal_button = tkinter.Button(
        frame_meal, bg="yellow", command=lambda id=id_meal: take_order_meal(id)
    )
    row, column = divmod(i, COLUMNS)
    meal_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# MIDDLE SALAD
frame_salad = tkinter.Frame(root, background="red")
frame_salad.columnconfigure(0, weight=1)
frame_salad.columnconfigure(1, weight=1)
frame_salad.columnconfigure(2, weight=1)
frame_salad.columnconfigure(3, weight=1)

frame_salad.rowconfigure(0, weight=1)
frame_salad.rowconfigure(1, weight=1)
frame_salad.rowconfigure(2, weight=1)

# SALAD BUTT


def take_order_salad(id_salad):
    found = False
    for i, order_item in enumerate(orders):
        if order_item[0] == menu["salad"][id_salad][0]:
            found = True
            break

    if not found:
        orders.append([menu["salad"][id_salad][0], menu["salad"][id_salad][1], 1])
    else:
        orders[i][-1] += 1

    item_values = menu["salad"][id_salad]
    if orders:
        item_values.append(orders[-1][-1])
    else:
        item_values.append(1)
    bill.insert("", "end", values=item_values)


commands_salads = menu["salad"]
COLUMNS = 4
for i, item in enumerate(commands_salads):
    id_salad = i
    salad_button = tkinter.Button(
        frame_salad, bg="yellow", command=lambda id=id_salad: take_order_salad(id)
    )
    row, column = divmod(i, COLUMNS)
    salad_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# MIDDLE 2 TABLE
frame_mid_2 = tkinter.Frame(root, background="red")
frame_mid_2.columnconfigure(0, weight=1)
frame_mid_2.columnconfigure(1, weight=1)
frame_mid_2.columnconfigure(2, weight=1)
frame_mid_2.columnconfigure(3, weight=1)

frame_mid_2.rowconfigure(0, weight=1)
frame_mid_2.rowconfigure(1, weight=1)
frame_mid_2.rowconfigure(2, weight=1)

# TABLE BUTT

the_id = 0


def get_table_id(id_):
    global the_id
    the_id = id_
    return the_id


COLUMNS = 4
for i, item in enumerate(range(5)):
    table_id = i
    id = get_table_id(table_id)
    menu_button = tkinter.Button(
        frame_mid_2,
        bg="yellow",
        text="Table 0" + str(i),
        command=lambda id=id: get_table_id(id),
    )
    row, column = divmod(i, COLUMNS)
    menu_button.grid(row=row, column=column, sticky="NEWS", padx=10, pady=10)


# top
l1 = tkinter.Label(frame_top, text="Staff_Id", bg="red")
l1.grid(row=0, column=0, padx=5, pady=5)

# mid
item_photo_list = [photo_salad, photo_meal, photo_soda, photo_drinks, photo_dessert]
commands = {"0": salad, "1": meal, "2": soda, "3": drink, "4": dessert}

COLUMNS = 4
for i, item in enumerate(item_photo_list):
    menu_button = tkinter.Button(
        frame_mid, image=item, bg="yellow", command=commands[str(i)]
    )
    row, column = divmod(i, COLUMNS)
    menu_button.grid(row=row, column=column, sticky="news", padx=10, pady=10)

# left


Table_b = tkinter.Button(frame_left, text="TABLE", width=15, height=2, command=Table)
Table_b.grid(row=2, column=0)

Menu_b = tkinter.Button(frame_left, text="MENU", width=15, height=2, command=Menu)
Menu_b.grid(row=3, column=0)


label_frame_ = tkinter.Label(frame_left, text="Table")


def delete_selected():

    items = bill.get_children()
    selected = bill.selection()

    if selected:
        item = bill.item(selected, "values")[0]

        for i, order in enumerate(orders):
            if order[0] == item:
                index = i
                break

        quantity = int(order[2] - 1)
        order[2] = quantity

        if quantity == 0:
            bill.delete(selected)
            orders.pop(index)

        else:
            bill.delete(selected)


button = tkinter.Button(frame_left, text="Delete order", command=delete_selected)
button.grid(row=1, column=0)


def total():
    global the_id

    bil = []
    for i in orders:
        bil.append(float(i[1]) * int(i[-1]))
    sum_ = sum(bil)
    the_sum = "%.2f" % sum_

    l1 = tkinter.Label(frame_left, text="%.2f" % sum_, bg="lightblue")
    l1.grid(row=0, column=0, padx=5, pady=5)

    cursor.execute(
        "INSERT INTO orders (table_id, bill) VALUES (%s, %s)", (the_id, the_sum)
    )
    # Save the changes to the database
    con.commit()
    orders.clear()
    bill.delete(*bill.get_children())


# right
Menu_b = tkinter.Button(frame_right, text="Total Me", command=total)
Menu_b.pack(fill="both", expand=True)


# Orders

bill = ttk.Treeview(frame_left, selectmode="browse")
bill.grid(row=5, column=0, rowspan=3, sticky="WENS")

bill["columns"] = ("item", "price", "quantity")
bill["show"] = "headings"

bill.column("item", minwidth=50, width=10)
bill.column("price", minwidth=50, width=10)
bill.column("quantity", minwidth=50, width=10)
bill.heading("item", text="item")
bill.heading("price", text="price")
bill.heading("quantity", text="quantity")

for order in orders:
    bill.insert("", "end", values=order)

root.mainloop()
