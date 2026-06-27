a = 1
print(f"a:2 is |{a:2}|")#a:2 means that we want to print the value of "a" with a width of 2 characters.
a = 1
print(f"a:4 is |{a:4}|")
a = 12
print(f"a:4 if |{a:4}|")#a:4 means that we want to print the value of "a" with a width of 4 characters. 
#If the value of "a" is less than 4 characters, it will be padded with spaces on the left.
a = 123
print(f"a:4 is |{a:4}|")
a = 1234
print(f"a:4 is |{a:4}|")
a = 12345
print(f"a:4 is |{a:4}|")#a:4 means that we want to print the value of "a" with a width of 4 characters.
#If the value of "a" is greater than 4 characters, it will be printed normally without any padding.
a = 12345
print(f"|{a: .3e}|")#a:0.3e means that we want to print the value of "a" in scientific notation 
#with 3 decimal places.
a = -12345
print(f"|{a:.3e}|")#a:0.3e means that we want to print the value of "a" in scientific notation 
a = 459.9999999 #number is rounded to 460.000 
b = 46.95238945 #rounding doesnt happen here
print(f"|{a:.3f}| \n|{b:.3f}|")#a:8.2f means that we want to print the value of "a" as a floating-point number
#with a width of 8 characters and 2 decimal places.

