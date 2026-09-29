# Retail Management System

A small console app I built in Python to run a shop from the terminal. It keeps track of stock, makes bills for customers, and logs all the money coming in and going out. There's no database. Everything is saved in plain text files, which made it a good way for me to learn file handling.

The only outside package it needs is `tabulate`, which prints the tables.

---

## What it does

The app has three parts, all reachable from one main menu.

**Inventory**
- See everything in stock
- Search for a single item
- List items that are running low (under 10)
- Add new items or top up existing ones (every purchase is logged as a debit)

**Billing**
- Take the customer's name and mobile number
- Add as many items as you like to a bill
- Check that the item is actually in stock and reduce the stock when it's sold
- Print a receipt with the total
- Log the sale as a credit

**Accounts**
- Credit log: money received from customers
- Debit log: money spent on restocking
- Every entry carries a timestamp

---

## Files

```text
Retail Management System/
├── main.py
├── timestamp.py
├── tabuler.py
├── invetory.txt
├── credits.txt
└── debits.txt
```

> Yes, `invetory.txt` is misspelled. The code looks for that exact name, so if you rename it, rename it in the code too.

- **`main.py`**: the main program and all the menus.
- **`timestamp.py`**: one function, `timestamp()`, that returns the current local time like `[21:40-28/9/2026]`.
- **`tabuler.py`**: one function, `tabular()`, a small wrapper around `tabulate` so every table in the app looks the same.

---

## How data is stored

**`invetory.txt`**: one item per line, `Item,Quantity`

```text
Mango,5
Rajma,50
Rice,25
```

When the program starts it reads this into a dictionary (`{"Mango": "5", ...}`) and writes it back after any change.

**`credits.txt`**: money from customers, `Name,Amount,Timestamp`

```text
Aayush,Rs.650,[22:7-28/9/2026]
```

**`debits.txt`**: money spent on stock, `Item,Quantity,Amount,Timestamp`

```text
Mango,5,Rs.1125,[21:40-28/9/2026]
```

---

## Getting started

You'll need Python 3 and `tabulate`:

```bash
pip install tabulate
```

Put all the files in the same folder and run:

```bash
python main.py
```

You'll see the main menu:

```text
WELCOME TO RETAIL MANAGEMNT SYSTEM

Enter 1 to access the inventory
Enter 2 to access the biling srvice
Enter 3 to access accounts log
```

(The typos in the menu text are mine too. I'll fix them eventually.)

---

## Using it

### Inventory (option 1)

```text
Enter 1 to access the whole inventory
Enter 2 to search for a specific item
Enter 3 to see items less in stock
Enter 4 to add an item to inventory
```

- **1** shows the full stock in a table.
- **2** asks for an item name and shows its quantity, or says `Item not in inventory`.
- **3** shows anything with fewer than 10 units left.
- **4** takes input as `item,quantity,price`, for example `Mango,5,225`. If Mango already has 10 in stock, it becomes 15. The purchase also goes into `debits.txt`.

### Billing (option 2)

First it asks for the customer's name and mobile number. Then enter each product as `item,quantity,price`:

```text
Mango,2,225
```

When you're done adding items, type `1` to finish. The stock is reduced automatically (selling 3 Mangoes from a stock of 10 leaves 7), and a receipt is printed:

```text
RECEIT

Name: Aayush
mobile no: 9876543210

+-------+----------+-------+-------+
| item  | quantity | price | total |
+-------+----------+-------+-------+
| Mango | 2        | 225   | 450   |
| Rice  | 1        | 100   | 100   |
+-------+----------+-------+-------+

Total amount to pay: 550
```

The sale is then saved to `credits.txt`.

### Accounts (option 3)

Pick **1** for the credit log or **2** for the debit log. Both are shown as tables with the timestamps.

---

## How it fits together

```text
Main menu
├── Inventory ──> invetory.txt (and debits.txt when adding stock)
├── Billing   ──> invetory.txt, then receipt, then credits.txt
└── Accounts  ──> credits.txt / debits.txt
```

---

## What I practised

- File handling: `open()`, `read()`, `write()`, `seek()`, `truncate()`, `close()`
- Dictionaries for the inventory and comprehensions for the low-stock filter
- Splitting code into functions and separate modules
- f-strings for formatting
- Using an external package (`tabulate`)

---

## Known problems

I know this isn't finished. The main gaps:

1. **No input validation.** Typing letters where a number is expected will crash the program with a `ValueError`.
2. **Missing files cause errors.** `invetory.txt`, `credits.txt` and `debits.txt` need to exist already.
3. **Prices aren't saved in the inventory.** The price you type when adding stock only goes into the debit log, so the shop doesn't "remember" selling prices.
4. **Mobile numbers aren't saved.** They show up on the receipt but never reach `credits.txt`.
5. **No login.** Anyone who can run the script can use everything.
6. **Text files don't scale.** They're fine for learning, but something like SQLite would be safer and easier to search as data grows.

---

## Things I'd like to do next

**Clean-up**
- Use `with open(...)` everywhere instead of opening and closing files by hand
- Fix the `f.close` bug (it needs to be `f.close()`, otherwise the file never actually closes)
- Rename `invetory.txt` to `inventory.txt` and `tabuler.py` to `tabular.py`
- Replace one-letter variable names (`a`, `b`, `d`, `f`) with readable ones like `item_name` and `inventory`
- Fix the typos in the menus

**New features**
- Create missing files automatically
- Add input validation and error handling
- Store prices in the inventory
- Save mobile numbers with each sale
- Invoice numbers
- Editing and deleting products
- Daily and monthly sales reports, and profit calculation
- Login with admin and employee roles
- Export to CSV or Excel
- Move to SQLite, then maybe a GUI or barcode support

---

## Built with

| Tool | Used for |
|---|---|
| Python | Everything |
| `time` | Timestamps |
| `tabulate` | Console tables |
| Text files | Storing data |

---

## Author

**Aayush**: a beginner learning Python by building something that actually works.

## License

This is for learning and personal use.