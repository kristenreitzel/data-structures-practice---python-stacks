# Data Structures Practice – Python Stacks

This repository contains simple Python examples that demonstrate how a **stack** works using a regular Python list. A stack is a **Last In, First Out (LIFO)** data structure, where the most recently added item is the first one removed.

## What this project shows

- How to use a Python list as a stack
- How to **push** items onto the stack using `append`
- How to **pop** items from the stack using `pop`
- How the order of operations always follows **LIFO** (Last In, First Out)

## File overview

- `stack_push_pop.py`  
  A small, focused example that:
  - creates an empty stack
  - pushes three items onto it
  - pops two items and prints them
  - prints the final contents of the stack

## Why this matters

Even though this is a small example, it shows:

- Understanding of a core data structure (*stack*)
- Correct use of Python list methods (`append` and `pop`)
- Ability to reason about state changes and order of operations  
  (which is very relevant for QA and debugging)

## How to run

You can run the script with:

```bash
python stack_push_pop.py
