# Step 1: Create a list of products. For example: ['Apple', 'Banana', 'Orange']
products = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

# Step 2: Create a dictionary to store the quantity of each product in the inventory. Key should be product name, value - quantity (can be any positive integer or 0)
inventory = {product: 0 for product in products}

# Step 3: Use a for loop to display the current inventory. Example output to terminal:
# Current inventory:
#Apple: 0
#Banana: 0
#Orange: 0

print("Current Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# Step 4: Allow the user to update the quantity of a specific product in the inventory
product_to_update = input("\nEnter the product to update: ")
if product_to_update in inventory:
    new_quantity = int(input(f"Enter the new quantity for {product_to_update}: "))
    inventory[product_to_update] = new_quantity
    print(f"\n{product_to_update} quantity updated successfully!")
else:
    print(f"\n{product_to_update} not found in inventory.")

# Step 5: Display the updated inventory the same way as in step 3
print("\nUpdated Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

