names = ["John Smith", "Arthur Morgan", "Carl Johnson", "Real Deal", "Captain Price", "Kelly Oubre"]

for name in names:
    # Split the name into first name and last name
    first_name, last_name = name.split()

    # Check if the last name is longer than 4 letters
    if len(last_name) > 4 or len(name) > 5:
        print(last_name)


# add_name = input("Add another name") # variantas su input
# name, surname = add_name.split()
# if len(surname) < 20:
#     names.append(add_name) 

add_names = ["Mariah Carey", "Jude Law", "Jan Andersensensensensensen"]

for full_name in add_names:
    name, surname = full_name.split()
    if len(surname) < 20:
        names.append(full_name)
        
print(names)
