
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.



# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.



# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.


def list_stats(numbers):
    if not numbers: return None

    total = 0
    count = 0
    largest = numbers[0]

    for number in numbers:
        total += number
        count += 1
        if number > largest:
            largest = number

    average = total / count
    print(f"The sum of the numbers is {total}")
    print(f"The average of the numbers is {average}")
    print(f"The largest number is {largest}")

    return total, average, largest

numbers = [2, 4, 6, 8, 10]
list_stats(numbers)



    

