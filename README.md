# Restaurant-Kiosk-System
An interactive terminal-based restaurant kiosk system written in Python for ITN160. Features dynamic dictionary-based menu generation, input constraint validation, multi-item ordering loops, and automated receipt totalization calculations.
markdown# 🍔 Pirate-Themed Restaurant Kiosk System (ITN160)

A lightweight, terminal-based Point-of-Sale (POS) kiosk application written in Python. This project utilizes structured data collections, data validation loops, and dynamic math operations to simulate a self-service ordering kiosk environment.

---

## 🛠️ Technical Design & Engineering Highlights

*   **Dictionary Menu Mapping:** Leveraging a Python dictionary (`menu`) to store, index, and map menu numbering keys seamlessly to immutable tuples containing item descriptors and floating-point prices.
*   **Input Validation Constraints:** Features nested `while` boundary containment loops to enforce clean transaction scaling (rejecting invalid item arrays or transaction counts below 1 or above 100).
*   **Transactional Staging Array:** Employs a multi-dimensional array list (`orders`) to append, track, and retain transaction memory records across ongoing multi-selection ordering routines.
*   **Financial Totalization Engine:** Automatically parses the order queue, formats output string sub-totals using fixed precision formatting (`:.2f`), and aggregates the `grand_total` metrics dynamically upon closure.

---

## 🚀 How It Works

The program outputs an intuitive user terminal interface:
1. Displays the custom seafood/pirate menu dynamically.
2. Prompts the customer for numerical menu mappings (1-10) and quantity specifications.
3. Validates that incoming values exist within legal bounds.
4. Generates a cleanly aligned receipt layout totaling all purchased items.

### Sample Terminal Execution Output
```text
Welcome to the Restaurant Kiosk and Menu!!!

1)  Black Pearl Burger - \$8.50
2)  Kraken Bites - \$6.00
3)  Tortuga Punch Run (Non-Alcoholic) - \$3.50
...

Enter the item number you want to order (1-10): 1
You selected: Black Pearl Burger
How many would you like to order? 2
Would you like to order another item? (Y/N): n

-------RECEIPT --------

Black Pearl Burger  x2  \$8.50 = \$17.00

--------------------------
GRAND TOTAL: \$17.00
--------------------------
```
