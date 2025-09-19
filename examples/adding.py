from jam import run_jam_code

#Example: add two numbers

code = """"
set x = 7
set y = 8
add x and y into total
print total
"""

print(run_jam_code(code))