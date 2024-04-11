my_string = "Hello, World!"

first_space_index = my_string.index(' ')

first_word = my_string[:first_space_index].upper()

new_string = first_word + my_string[first_space_index:]

print(new_string) 