# Project Statements

## Project Title

**Retail Management System**

---

## Project Overview

This is a console-based Retail Management System that I built in Python.

The idea was to recreate the day-to-day running of a small retail store: keeping track of inventory, billing customers, and logging money coming in and going out.

Instead of a database, everything is saved in **plain text files**, so the data sticks around even after the program closes.

---

## Why I Built It

I wanted to use Python to solve a practical, real-world problem. Rather than practising each concept in isolation, I brought them all together into one working system.

Here's what I set out to do:

- Manage the store's inventory
- Keep track of how much of each item is available
- Search for products
- Spot products that are running low on stock
- Add new products to the inventory
- Process customer purchases
- Calculate bills
- Update the inventory after every sale
- Keep credit and debit records
- Record the time of every transaction
- Show information in neat, formatted tables

---

## Main Components

The system is split into three main sections.

### Inventory Management

With the inventory section, you can:

- View the complete inventory
- Search for a particular item
- See which items have stock below 10
- Add brand-new inventory
- Increase the quantity of an item that already exists
- Record inventory purchases in the debit log

---

### Billing System

With the billing section, you can:

- Enter the customer's information
- Enter as many purchased items as needed
- Check whether each product is available
- Deduct the purchased quantities from inventory
- Work out the total for each item
- Calculate the final bill
- Display a receipt
- Record the transaction in the credit log

---

### Accounts System

The accounts section lets you look at:

- Credit transaction records
- Debit transaction records

Every transaction is saved with a timestamp.

---

# How Data Is Stored

The project relies on three text files to keep its data.

### `invetory.txt`

This file holds product names and how many of each we have.

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

This file holds sales made to customers.

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

This file holds purchases made to restock the inventory.

Format:

```text
item,quantity,amount,timestamp
```

Example:

```text
Mango,5,Rs.1125,[21:40-28/9/2026]
```

---

# Python Concepts I Used

This project puts a number of Python concepts into practice.

### Variables and Data Types

The program works with strings, integers, lists, dictionaries, and tuples.

---

### Conditional Statements

The main menu and each operation use `if`, `elif`, and `else` to decide what the program should do next.

---

### Loops

The billing system uses a `while` loop so that several products can be added to a single bill.

---

### Functions

I pulled reusable operations out into functions. Two examples are:

```python
timestamp()
```

and:

```python
tabular()
```

---

### Modules

Reusable functionality lives in its own Python files:

```text
timestamp.py
tabuler.py
```

This is my way of practising basic modular programming.

---

### Dictionaries

Inventory data is represented with dictionaries.

Example:

```python
{
    "Mango": "5",
    "Rajma": "50"
}
```

This makes it easy to look up products and update their quantities quickly.

---

### Lists

Lists hold the billing information and transaction records before they are shown on screen or written to files.

---

### File Handling

File handling is used heavily throughout the project. The operations involved include:

```python
open()
read()
write()
seek()
truncate()
```

Thanks to this, information is still there after the program ends.

---

### F-Strings

F-strings help me format output and build the records that get written to files.

Example:

```python
f.write(f"{items},{values}\n")
```

---

### Dictionary Comprehension

The low-stock list is built with a dictionary comprehension:

```python
x = {x:y for x,y in d.items() if int(y) < 10}
```

This filters the inventory down to items based on their quantity.

---

### External Library

To show inventory and billing details in clean, formatted tables, the project uses the `tabulate` Python package.

---

# Design Approach

I deliberately stuck to fundamental Python instead of reaching for object-oriented programming or databases.

The aim was to show that I understand the following progression:

```text
Python Fundamentals
       ↓
Functions
       ↓
Modules
       ↓
Lists & Dictionaries
       ↓
File Handling
       ↓
Data Processing
       ↓
Practical Application
```

Keeping things simple makes the code easier to follow, while still giving me a functional retail management system.

---

# Current Scope

Right now, this is mainly an educational console application.

It works well for demonstrating:

- Basic inventory management
- Basic billing
- Saving data in files so it persists
- Simple financial records
- Modular Python programming

It isn't meant to replace a production-level retail management or accounting system.

---

# Current Limitations

The current version has a few limitations worth being upfront about.

### Input Validation

The program assumes the user will enter data in the expected format. If they don't, Python exceptions may occur.

### Text-Based Storage

Data lives in plain text files instead of a proper database.

### Authentication

There's no user authentication or access control yet.

### Product Pricing

Prices are entered while billing and while adding inventory, but they aren't saved permanently alongside the inventory quantity.

### Customer Records

A customer's mobile number is shown during billing, but it isn't saved in the credit log.

---

# Future Development

Here are some improvements I could make down the line:

- Input validation
- Exception handling
- Automatic creation of missing files
- Storing product prices
- Product categories
- Customer records
- Authentication
- User roles
- Invoice numbers
- Sales reports
- Profit calculation
- A better transaction history
- SQLite database support
- A graphical user interface

---

# Development Statement

I built this project as a hands-on way to apply what I've learned in Python.

My focus was on understanding how individual programming concepts can be combined into one complete, working application.

As I learn more advanced Python concepts, I can keep expanding the project.

---

## Author

**Aayush**

### Project Type

Educational / Personal Python Project

### Technology

**Python**

### Storage

**Plain Text Files**

### Interface

**Console / Command Line**