str = "Good Luck"
new_str = ""

to_be_replaced_char = "o"
new_char = "u"

for char in str:
    if char == to_be_replaced_char:
        new_str += new_char
    else:
        new_str += char

print(new_str)