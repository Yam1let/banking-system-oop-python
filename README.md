# 🏦 Banking System - Object-Oriented Programming in Python

## Project Overview

This project is a structured banking system built using Object-Oriented Programming (OOP) in Python.

It simulates real-world banking operations such as deposits, withdrawals, balance checks, and transfers between clients, while enforcing validation rules and clean code practices.

The main goal of this project was to design a small but well-structured system that demonstrates proper class modeling, object interaction, and error handling.

---

## Concepts Applied

- Object-Oriented Programming (OOP)
- Class composition and object relationships
- Input validation using `isinstance`
- Exception handling with `TypeError` and `ValueError`
- Business rule enforcement (e.g., insufficient funds prevention)
- Custom object representation using `__repr__`
- Proper script structure using `if __name__ == "__main__"`

---

## System Architecture

The system consists of two main classes:

### 1️ `BankAccount`
Represents a bank account and provides:

- Deposit functionality
- Withdrawal functionality
- Balance storage
- Validation for invalid transactions
- String representation of account state

### 2️ `Client`
Represents a bank client associated with a `BankAccount`.

- Balance checking
- Money transfers between clients
- Type validation for safe interactions

---

## Validation & Error Handling

The system includes:

- Type checking for inputs
- Prevention of negative transactions
- Insufficient funds protection
- Clear and explicit error handling using Python exceptions

This ensures logical consistency and system reliability.

---

## Example Usage

The script includes an execution example under:

```python
if __name__ == "__main__":
