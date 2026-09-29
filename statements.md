# Project Statements
## Project title
**Retail Management System** 
---
## Project description
This is the console based Retail Management System that I have developed in Python. 
The aim was to simulate the normal working of a small shop ie. maintaining the inventory, making bills for customers and keeping track of the flow of money.
Instead of a database, I have made use of **plain text files** and so the data is always persistent even if the program is terminated. 
---
## Why I created this
I wanted to apply Python for solving a real life problem and instead of developing each concept on its own, I just linked them together. 
What I wanted to develop in this project:
- Manage inventory for the shop
- Keep track of the quantity of each item
- Search for particular items in the inventory
- Find out items that are low on stock
- Add new items to the inventory
- Make bills for customers
- Generate bills
- Update the inventory when a bill is generated
- Make debit and credit entries
- Timestamp all transactions
- Simulate tables with appropriate formatting for display
---
## Major components
The program has three major components.
### Inventory module
This module allows you 
- to view all items present in the shop 
- to search for any particular item
- to view items with low stock level
- Add new inventory
- Raise quantity of an item already present
- Log purchases to debit log
---
### Billing system
Inside the billing part you can:
- Enter the customer details
- Enter as many items as you want
- Check that each item is present
- Decrease purchased amount from inventory
- Calculation of individual items
- Calculation of total bill
- Print the bill
- Log the bill to the credit log
---
### Accounts system
Inside the accounts part you can review:
- Credit logs
- Debit logs
All of these logs get timestamped every time there is a transaction.
---
# How data is stored
The source code uses 3 files to store the data.
### `invetory.txt`
Here all the products names and quantities are stored.
Format:
```text
item,quantity
```
Example:
```text
Mango,5
Rajma,50
Rice,25
```
---
### `credits.txt`
Here all the sales that are done are logged.
Format:
```text
customer,amount,timestamp
```
Example:
```text
Aayush,Rs.650,[22:7-28/9/2026]
```
---
### `debits.txt`
Here all purchases that are done to restock inventory are logged.
Format:
```text
item,quantity,amount,timestamp
```
Example:
```text
Mango,5,Rs.1125,[21:40-28/9/2026]
```
---
# Python concepts used
The source code uses several/python concepts.
Variables and data types
The program extracts from and inserts into strings/integer/lists/dictionaries/tuples.
---
Control flow statements
The main menu and all operations are if/elif/else based to decide what next.
---
Loops
From the billing program I use a while loop to bill for multiple products at a time.
---
Functions
I perform a number of operations in functions. For instance:
```python
timestamp()
```
and:
```python
tabular()
```
---
Modules
I seperate common code into its own Python modules:
```text
timestamp.py
tabuler.py
```
To practice simple modular programming.
---
Dictionaries
Inventory is held in a dictionary.
For example:
```python
{
"Mango": "5",
"Rajma": "50"
}
```
I get very fast product lookup and simple quantity and details update.
---
Lists
Billing details/ transaction records are held in lists before printing on screen or writing to external files.
---
File handling
There are many file handling operations in this program. These are:
```python
open()
read()
write()
seek()
truncate()
```
So the information exists after the program has ended.
---
F-strings
I use F-strings to make my file records:
```python
The code to read/write to file is:

```python
with open("file.txt",".") as f:
    items,values = f.readline().split(",")
    
# ...
    
f.write(f"{items},{values}\n")
```
---
The list is created with a dictionary comprehension
```python
x = {x:y for x,y in d.items() if int(y) < 10}
```
so that it only contains items on stock level.
---
### External Library
The `tabulate` Python package is used to print tabulated.

inventory and billing details.
---
# Design Thinking
I am consciously avoiding object-oriented programming or databases.
I am trying to demonstrate that I understand the following:

```text
Python Basics
↓
Functions
↓
Modules
↓
Lists/Dicts
↓
File Handling
↓
Data Processing
↓
Application
```
It is faster, less complex and easier to read code.
Still I am able to have a functional system and not just a script.
---
# Current Capability
Now, it is an educational application, well suited for:
- Learning basic billing
- Learning basic inventory
- Data persistence using files
- Basic financials
- Functional module based Python programming
It is not a production retail management and accounting system.
---
# Current Limitation
I am being subtle about the shortcomings of the current application.
### Input Validation
The program does not check for input compliance and will work only if the user indicates correct input format, else Python exceptions may occur.
### Text Storage
Data is in plain text files not in a database.
User authentication and access control has not been implemented yet.
### Price 
It is entered when dealing with inventory and when billing a customer it is entered at sales time but not even stored with inventory quantity.
### Customer Records
You're customer’s phone number is entered at sales time but paypal will not be entered in to the credit log
---
# Future Improvements
Some changes and features which I might add:
- Validating input
- Appropriate exception handling
- Auto creating missing file
- Price of product
- Product categories
- Customer records
- User authentication
- Different user roles
- Account number
- Sales Report
- Profit
- Better transaction log
- Support for SQLite Database
- GUI
---
# My Statement
I am developing this project to practice and try what I have learned of Python.
I particularly wanted to know how all the concepts worked together to create one working application in which I can use them.
With the knowledge gained of more concepts, I can add more to this project.
---
## Developer
**Aayush**
### Project Category
Academic / Personal Python Project 
### Technology Stack
**Python**
### Data Storage
**Plain text files**
### User Interface
**Command Line / console