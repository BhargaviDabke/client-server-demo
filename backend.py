# give me a file with two functions to print the list of items and add values to the list

# items = []
# def print_items():
#     """Prints the list of items."""
#     if items:
#         print("Items in the list:")
#         for item in items:
#             print(f"- {item}")
#     else:
#         print("The list is empty.")

# def add_item(item:str):
#     """Adds an item to the list."""
#     items.append(item)
#     print(f"Item '{item}' added to the list.")  

# Create a function to get sqrt of a number
import numpy as np

def get_sqrt(n):
    print("Calling square root function from backend...")
    return np.sqrt(n)
