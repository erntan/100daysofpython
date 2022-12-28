with open("C:\\Users\Ern\Desktop\my_file.txt") as file:   # Default mode = read only "r"
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="w") as file: # Overwritten
#     file.write("New text")
#
# with open("my_file.txt", mode="a") as file: # Appended
#     file.write("\nNew text appended")

with open("new_file.txt", mode="w") as file:
    file.write("New file created")