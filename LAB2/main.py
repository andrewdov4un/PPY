

"""8.
Extend the previous Python program to write the output to a file and perform operations on that file.

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. ...

  h. Write Output to File: Write all the results (original inputs, modified data structures, type conversion results) to a file.

  i. Perform Operations on File: Open the file, read its content, and perform some operations like counting the number of lines, finding specific data, etc.

  j. Modify File Content: Modify the content of the file by, for example, changing specific lines or adding new lines.
"""

## Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input to List
numbers_list = [int(num) for num in input_numbers.split()]

# Manipulate List
numbers_list.append(10)  # Append 10 to the list
numbers_list.insert(2, 20)  # Insert 20 at index 2
if 8 in numbers_list:
    numbers_list.remove(8)  # Remove the element 8 if it exists

# Attempt to Modify Tuple (this will raise an error)
numbers_tuple = tuple(numbers_list)
try:
    numbers_tuple.append(10)  # Attempt to append to tuple
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
numbers_set = set(numbers_list)
other_set = {10, 11, 12}
set_union = numbers_set.union(other_set)  # Union of sets
set_intersection = numbers_set.intersection(other_set)  # Intersection of sets
set_difference = numbers_set.difference(other_set)  # Difference of sets

# Dictionary Operations
numbers_dict = {num: num ** 2 for num in numbers_list}  # Creating dictionary

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = {num: num ** 2 for num in numbers_list}
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = {num: num ** 2 for num in numbers_tuple}
set_to_list = list(numbers_set)
set_to_tuple = tuple(numbers_set)
set_to_dict = {num: num ** 2 for num in numbers_set}
dict_to_list = list(numbers_dict.keys())
dict_to_tuple = tuple(numbers_dict.keys())
dict_to_set = set(numbers_dict.keys())

# Write Output to File
with open("output.txt", "w") as file:
    file.write("Original List: " + str(numbers_list) + "\n")
    file.write("Original Tuple: " + str(numbers_tuple) + "\n")
    file.write("Original Set: " + str(numbers_set) + "\n")
    file.write("Original Dictionary: " + str(numbers_dict) + "\n\n")

    file.write("Manipulated List: " + str(numbers_list) + "\n")
    file.write("Manipulated Tuple: " + str(numbers_tuple) + "\n")
    file.write("Union of Set: " + str(set_union) + "\n")
    file.write("Intersection of Set: " + str(set_intersection) + "\n")
    file.write("Difference of Set: " + str(set_difference) + "\n")
    file.write("Updated Dictionary: " + str(numbers_dict) + "\n\n")

    file.write("List to Tuple: " + str(list_to_tuple) + "\n")
    file.write("List to Set: " + str(list_to_set) + "\n")
    file.write("List to Dictionary: " + str(list_to_dict) + "\n")
    file.write("Tuple to List: " + str(tuple_to_list) + "\n")
    file.write("Tuple to Set: " + str(tuple_to_set) + "\n")
    file.write("Tuple to Dictionary: " + str(tuple_to_dict) + "\n")
    file.write("Set to List: " + str(set_to_list) + "\n")
    file.write("Set to Tuple: " + str(set_to_tuple) + "\n")
    file.write("Set to Dictionary: " + str(set_to_dict) + "\n")
    file.write("Dictionary to List: " + str(dict_to_list) + "\n")
    file.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
    file.write("Dictionary to Set: " + str(dict_to_set) + "\n")

# Perform Operations on File
with open("output.txt", "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
    num_integers = sum(line.count(" ") for line in lines)
    sum_integers = sum(int(num) for line in lines for num in line.split() if num.isdigit())

print("Number of lines in the file:", num_lines)
print("Number of integers in the file:", num_integers)
print("Sum of integers in the file:", sum_integers)

"""--------------------------------------------------------------------------------
**Control Statements:**
Control statements are used in programming to alter the flow of execution based on certain conditions or criteria. In Python, commonly used control statements include:

`if, elif, else:` These statements are used for conditional execution. They allow the program to execute different blocks of code based on specified conditions.

`for loop:` Used for iterating over a sequence (such as lists, tuples, strings, etc.) or any iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

`while loop:` Used for executing a block of code repeatedly as long as a specified condition is true. It keeps iterating until the condition becomes false.


**Loops:**
Loops are used for executing a block of code repeatedly. In Python, there are two main types of loops:

`for loop: `As mentioned earlier, the for loop iterates over a sequence or any iterable object.

`while loop:` This loop executes a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.

**Other Statements:**
This category typically includes other types of statements that don't fall directly under control statements or loops. It can include various types of statements used for different purposes in Python programming, such as:

`Assignment statements:` Assigning values to variables.

`Function calls:` Invoking functions to perform specific tasks.

`Import statements:` Importing modules or packages to use their functionality in the current script or program.

`Exception handling statements: `Statements used for handling exceptions (errors) that may occur during the execution of a program, such as try, except, finally, etc.

`With statements: `Used for resource management, especially for working with files, to ensure that certain resources are properly closed or released after use.

These are fundamental constructs in Python programming that enable you to control the flow of your program, repeat tasks efficiently, and execute various types of statements to achieve desired functionality.

-------------------------------------------------------------------------------

9.  Utilizing the Largest Integer from output.txt

  Task Description:

  Transform the previous task to utilize the largest integer from the output file 'output.txt' instead of asking the user for it.

  1. Read the largest integer from the 'output.txt' file.
  2. Generate a list of all prime numbers up to the largest integer.
  3. Print the list of prime numbers.
  4. Calculate the sum of all prime numbers in the list.
  5. Determine the largest and smallest prime numbers in the list.
  6. Check if the largest integer itself is prime and print the result.
  7. Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'.
  8. Handle the scenario where the largest integer cannot be found in the file.

  Example:

  If the 'output.txt' file contains:
  Largest prime number: 20

  The program will generate the list of prime numbers up to 20, perform calculations, and write the results to 'prime_numbers.txt'.
"""

# Read the largest integer from the 'output.txt' file
with open("output.txt", "r") as file:
    for line in file:
        if "Largest prime number" in line:
            largest_integer = int(line.split(":")[1].strip())
            break
    else:
        print("Error: Largest integer not found in the file.")
        exit()

# Generate a list of all prime numbers up to the largest integer
prime_numbers = []
for num in range(2, largest_integer + 1):
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        prime_numbers.append(num)

# Print the list of prime numbers
print("List of prime numbers:", prime_numbers)

# Calculate the sum of all prime numbers in the list
sum_primes = sum(prime_numbers)

# Determine the largest and smallest prime numbers in the list
largest_prime = max(prime_numbers)
smallest_prime = min(prime_numbers)

# Check if the largest integer itself is prime and print the result
if largest_integer in prime_numbers:
    print("The largest integer itself is prime.")
else:
    print("The largest integer itself is not prime.")

# Write the list of prime numbers along with the sum, largest, and smallest prime numbers to 'prime_numbers.txt'
with open("prime_numbers.txt", "w") as file:
    file.write(f"List of prime numbers: {prime_numbers}\n")
    file.write(f"Sum of prime numbers: {sum_primes}\n")
    file.write(f"Largest prime number: {largest_prime}\n")
    file.write(f"Smallest prime number: {smallest_prime}\n")


"""10.
In the final main.py file, leave the results from task 8 and 9, commit and push
"""
