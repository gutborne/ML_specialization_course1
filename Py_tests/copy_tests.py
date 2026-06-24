import copy
import my_script

def main():
    print(f"__name__ in copy_tests: {__name__}, so this indicates this file is the main one(ot the main module)")
    #Integers are immutable, so when we assign b = a, both a and b point to the same value (10).
    # However, when we change b to 230, it creates a new object for b, and the variable a still points 
    # to the original value (10). Therefore, the output will be:
    print("INTEGERS ARE IMMUTABLE")
    a = 10
    b = a
    print(f"a =  {a}, b = {b}")  # Output: 10 10
    b = 230
    print(f"a =  {a}, b = {b}")  # Output: 10 230
    print("INTEGERS ARE IMMUTABLE")

    print("case with mutable objects".capitalize())
    print("                                     copy by reference")
    my_list = [[1,3], [4, 5]]
    copy_list = my_list
    print(f"copy_list: {copy_list}")
    copy_list[0][0] = 10
    print(f"copy_list: {copy_list}")

    print("                                     shallow copy")
    my_list = [[1,3], [4, 5]]
    print(f"my_list: {my_list} is the original one.")
    copy_list = my_list.copy() #we could have declared copy_list = copy.copy(my_list)
    print(f"copy_list: {copy_list}")
    copy_list[0][1] = 45
    print(f"my_list: {my_list}")
    print(f"copy_list: {copy_list}")
    print(f"my_list id: {id(my_list)} copy_list id: {id(copy_list)}")
    print(f"my_list[0] id: {id(my_list[0])} copy_list[0] id: {id(copy_list[0])}")
    if id(my_list[0]) == id(copy_list[0]): print("equal ids!")
    else: print("not equal ids!")    

    print("                                     deep copy")
    my_list = [[1,3], [4, 5]]
    print(f"my_list: {my_list} is the original one.")
    copy_list = copy.deepcopy(my_list)
    print(f"copy_list: {copy_list}")
    copy_list[0][1] = 59
    print(f"my_list: {my_list}")
    print(f"copy_list: {copy_list}")
    print(f"my_list id: {id(my_list)} copy_list id: {id(copy_list)}")
    print(f"my_list[0] id: {id(my_list[0])} copy_list[0] id: {id(copy_list[0])}")
    if id(my_list[0]) == id(copy_list[0]): print("equal ids!")
    else: print("not equal ids!")

    print("case with mutable objects".capitalize())

if __name__ == "__main__":
    main()
