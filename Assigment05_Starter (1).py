#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Kaiden Piggott
# Date:  March 3rd 2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <YOUR NAME HERE>, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "C:\_PythonClass\Todo.txt"
strData = ""

lstTable = []
file1 = open("C:\PythonClass\Todo.txt", "r")
# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"



todo = [file1.read(11), file1.read(4), file1.read(10), file1.read(5)]  #LOADING INTO LIST####################

dicRow = {todo[0]: todo[1], todo[2]: todo[3]}                          #LOADING INTO DICTIONARY!###############


file1 = open("C:\PythonClass\Todo.txt", "w")


# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()# adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == "1"):                            # DISPLAYING INFO TO USER############
        for task, priority in dicRow.items():
            print(task, ":", priority)
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == "2"):
        task = input("Describe the Task: ")
        if task not in dicRow:
            priority = input("Enter the priority: (high/low)")
            dicRow[task] = priority
        else:
            print("That task is already in your todo list.")
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == "3"):
        task = input("what is the task you wish to remove?")
        if task in dicRow:
            del(dicRow[task])
            print(task, "is now deleted...")
        else:
            print("That task is not in the todo list. please try again.")
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == "4"):                                                  # SAVING FILE, MUST EXIT AS WELL
        lstTable = list(dicRow.items())
        print(lstTable)
        file1.write(str(lstTable))
        print("File Saved...Please exit before viewing txt file")
    elif (strChoice == "5"):
        break #and Exit the program
    else:
        print("that is not a valid choice")
file1.close()

