# Bank-Management-System-in-Python

# Objective

The project is a console-based Bank Management System built using Python and Object-Oriented Programming (OOP) concepts.
It simulates basic banking operations such as creating accounts, depositing/withdrawing money, transferring funds, and displaying account details.

# Features Implemented

# 1.Account Creation

Generates a random account number using randint.

Stores customer’s name, phone number, and balance.

# 2.View Account Details

Displays account number, full name, phone number, and balance.

# 3.Deposit Money

Allows users to add money into their account.

# 4.Withdraw Money

Validates balance before allowing withdrawal.

# 5.Money Transfer

Transfer funds between two valid accounts.

Checks for sufficient balance before transfer.

# 6.Exit

Ends the program safely.

# Technical Implementation

Language: Python

Concepts Used:

OOP → Bank class for encapsulating account behavior.

Data Structures → List (banks) to store multiple account objects.

Functions → check_account_exists() to search accounts by number.


# Example Workflow

Create two accounts → Alice & Bob.

Deposit money into Alice’s account.

Transfer part of Alice’s balance to Bob’s account.

Show both accounts → balances updated accordingly.

# Scope for Improvements

1.Save account data permanently using SQLite/MySQL instead of memory.

2.Add authentication (PIN/password) for security.

3.Provide transaction history for each account.

4.Create a GUI (Tkinter) or Web App (Flask/Django) for better usability.
