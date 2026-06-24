tp1 = (2, 3, 4)
tp2 = 1, 2, 3
print(tp1, tp2)


#accessing tuple values
"Note/Notice that the values keep their position, that means, the first value is 2, second is 3 and so on."
print(f"tp1[0]: {tp1[0]} tp1[1]: {tp1[1]}")

#immutability of tuples(we cannot change its values once the tuple is created)
try: 
    tp1[0] = 10
except TypeError as e:
    print(f"Error: {e}")


#hashability of tuples
d = {(2,3):"point1", (4,5):"point2"}
print(d[(2,3)], d[(4,5)])

#single-element tuple
"note that we need the comma to represent a single-element tuple, not just the parentheses"
tp4 = (5)
print(type(tp4)) #this is an integer, not a tuple
tp5 = (6,)

#tuple packing and unpacking
tp6 = 1, 2, 3 #packing
x, y, z = tp6 #unpacking
print(f"x: {x}, y: {y}, z: {z}")

#tuples can contain mixed types
tp7 = (1, "mateus", 3.4, [3,4], True)
print(tp7)

#Important methods for tuples
"There are only two buit-in methods for tuples: couunt() and index()"
"count(): returns the number of times a value shows up in the tuple"
"index(): returns the index of a value in the tuple(course, if the value exists in the tuple)"
tp8 = (1, 2, 3, 3, 4)
print(f"the number 3 shows up {tp8.count(3)} times in tp8")

#concatenate two tuples
tp3 = tp1 + tp2
print(tp3)

