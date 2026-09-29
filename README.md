# Retail Management System

This is a little console app I made in Python to run a shop from the terminal. It keeps track of what's in stock, makes bills for customers, and writes down all the money coming in and going out. I didn't use a database. Everything lives in plain text files, which turned out to be a great way to actually learn file handling.

The only thing you need to install is `tabulate`, which I use to print the tables.

---

## What it can do

There are three parts to it, and you get to all of them from one main menu.

**Inventory**
- Look at everything you have in stock
- Search for one particular item
- See which items are running low (anything under 10)
- Add a brand new item, or top up one you already have (every purchase also gets logged as a debit)

**Billing**
- Ask for the customer's name and mobile number
- Add as many items to the bill as you want
- Check the item is actually in stock, and take the sold quantity off the inventory
- Print a receipt with the total
- Log the sale as a credit

**Accounts**
- Credit log: the money customers have paid you
- Debit log: the money you've spent restocking
- Every entry has a timestamp

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

> Yes, I spelled `invetory.txt` wrong. The code looks for that exact name, so if you rename the file, you'll need to rename it inside the code too.

### `main.py`

This is the main program. All the menus live here.

### `timestamp.py`

It has one function that gives back the current local time, like `[21:40-28/9/2026]`. I use it every time a transaction gets logged.

```python
import time

def timestamp():
    b = time.localtime()
    return f"[{b.tm_hour}:{b.tm_min}-{b.tm_mday}/{b.tm_mon}/{b.tm_year}]"
```

### `tabuler.py`

This is a small wrapper around `tabulate`, so every table in the app looks the same. It can print either a dictionary or a list of rows.

```python
from tabulate import tabulate

def tabular(h, *b, **a):
    data = []

    for i, v in a.items():
        data.append([i, v])

    if a != {}:
        print(tabulate(tabular_data=data, headers=h, tablefmt="grid"))

    if b != ():
        print(tabulate(tabular_data=b, headers=h, tablefmt="grid"))
```

---

## How the data is saved

**`invetory.txt`** has one item per line, written as `Item,Quantity`:

```text
Mango,5
Rajma,50
Rice,25
Sugar,40
```

When the program starts, it reads this file into a dictionary, and after any change it writes the dictionary back to the file:

```python
{"Mango": "5", "Rajma": "50", "Rice": "25", "Sugar": "40"}
```

**`credits.txt`** is the money that comes in from customers, written as `Name,Amount,Timestamp`:

```text
Aayush,Rs.650,[22:7-28/9/2026]
Rahul,Rs.1200,[22:15-28/9/2026]
```

**`debits.txt`** is the money spent on stock, written as `Item,Quantity,Amount,Timestamp`:

```text
Mango,5,Rs.1125,[21:40-28/9/2026]
Rajma,50,Rs.2500,[21:49-28/9/2026]
```

---

## Getting it running

You'll need Python 3 and `tabulate`:

```bash
pip install tabulate
```

Keep all the files together in one folder, then run:

```bash
python main.py
```

The main menu will show up:

```text
WELCOME TO RETAIL MANAGEMNT SYSTEM

Enter 1 to access the inventory
Enter 2 to access the biling srvice
Enter 3 to access accounts log
```

(Yep, the typos in the menu are mine too. I'll fix them at some point.)

---

## How to use it

### Inventory (option 1)

```text
Enter 1 to access the whole inventory
Enter 2 to search for a specific item
Enter 3 to see items less in stock
Enter 4 to add an item to inventory
```

**1. See everything**

```text
+-------+----------+
| Item  | Quantity |
+-------+----------+
| Mango | 5        |
| Rice  | 25       |
| Rajma | 50       |
+-------+----------+
```

**2. Search for an item**

```text
Enter the item: Mango

5
```

If the item isn't in the inventory, it just tells you `Item not in inventory`.

**3. Low stock**

This shows anything with fewer than 10 units left. The whole filter is one line:

```python
x = {x:y for x,y in d.items() if int(y) < 10}
```

```text
+-------+----------+
| Item  | Quantity |
+-------+----------+
| Mango | 5        |
+-------+----------+
```

**4. Add stock**

Type in `item,quantity,price`, like this:

```text
Mango,5,225
```

If Mango already has 10 in stock, it goes up to 15 (so the file says `Mango,15`). The purchase also gets written into `debits.txt`.

### Billing (option 2)

It starts by asking for the customer's name and mobile number. After that, you enter each product as `item,quantity,price`:

```text
Mango,2,225
```

When you've added everything, type `1` to finish.

The stock comes off the inventory automatically. So if Mango was at 10 and the customer buys 3, it drops to 7, and that new number is saved back to `invetory.txt`.

Then it prints the receipt:

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

After that, the sale is saved to `credits.txt`.

### Accounts (option 3)

```text
Enter 1 to access credit logs
Enter 2 to access debits
```

**Credit log**

```text
+--------+--------+------------------+
| Name   | Amount | Date             |
+--------+--------+------------------+
| Aayush | Rs.650 | [22:7-28/9/2026] |
+--------+--------+------------------+
```

**Debit log**

```text
+-------+----------+---------+-------------------+
| Name  | Quantity | Amount  | Date              |
+-------+----------+---------+-------------------+
| Mango | 5        | Rs.1125 | [21:40-28/9/2026] |
+-------+----------+---------+-------------------+
```

---

## How it all connects

```text
                 ┌─────────────────────┐
                 │        START        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Main Menu      │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ┌───────────┐  ┌───────────┐  ┌───────────┐
       │ Inventory │  │  Billing  │  │ Accounts  │
       └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
             │              │              │
             ▼              ▼              ▼
       invetory.txt   invetory.txt    credits.txt
       debits.txt           │         debits.txt
                            ▼
                         Receipt
                            │
                            ▼
                       credits.txt
```

---

## What I learned while building it

- File handling: `open()`, `read()`, `write()`, `seek()`, `truncate()` and `close()`
- Using dictionaries to hold the inventory, and a comprehension to filter the low-stock items
- Breaking code up into functions and separate modules
- Formatting output with f-strings
- Using an external package (`tabulate`)

---

## What's still broken or missing

I know this isn't finished. Here are the main gaps:

1. **No input validation.** If you type letters where it expects a number, the program crashes with a `ValueError`.
2. **It needs the files to exist already.** `invetory.txt`, `credits.txt` and `debits.txt` have to be there before you pick certain options, or you'll get errors.
3. **Prices aren't saved in the inventory.** The price you type when adding stock only goes into the debit log, so the shop never remembers what an item sells for.
4. **Mobile numbers aren't saved.** They show up on the receipt, but they never make it into `credits.txt`.
5. **There's no login.** Anyone who can run the script can use everything.
6. **Text files don't scale well.** They're fine for learning, but once there's a lot of data, something like SQLite would be safer and much easier to search.

---

## What I want to do next

**Clean-up**
- Use `with open(...)` everywhere instead of opening and closing files by hand, so the file always closes even if something goes wrong
- Fix the `f.close` bug. It needs to be `f.close()`, otherwise the file never actually gets closed
- Rename `invetory.txt` to `inventory.txt` and `tabuler.py` to `tabular.py`
- Swap the one-letter variable names (`a`, `b`, `d`, `f`) for readable ones like `item_name` and `inventory`
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
- Move to SQLite, and maybe a GUI or barcode support later

---

## Built with

| Tool | What I used it for |
|---|---|
| Python | Everything |
| `time` | Timestamps |
| `tabulate` | Console tables |
| Text files | Storing the data |

---

## About me

I'm **Aayush**, a beginner learning Python by building things that actually work.

## License

This is for learning and personal use.