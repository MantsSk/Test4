# list_module.py

def sum_list(numbers):
    return sum(numbers)

def average_list(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return "List is empty"

# Additional list functions can be added as needed