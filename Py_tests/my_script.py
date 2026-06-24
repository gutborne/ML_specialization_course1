
#Note that when we run this file directly(python copy_tests.py), the __name__ variable will be
#__main__ indicating that this file is the main one. However, when we import this file as a module in 
# another file, the __name__ variable will be set to the name of the module (my_script in this case). 

print("this is my_script.py being imported as a module in copy_tests.py")
def main():
      print(f"__name__ in my_script: {__name__}, so this indicates this file is being imported as a module and" +
      " it's not the main one.)") 

if __name__ == "__main__":
      main()
