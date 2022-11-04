from collections import Counter

# Arrays
## Found a missing element in array from 1 to 10 (using formula n*(n+1)/2)
def misNum (array):
    n = len(array) + 1
    total = n*(n+1)/2
    return total - sum(array)

## Create a uniq array from another array (two ways with set and other with function for - if)
def uniq(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    return unique

## Returns all non_uniq numbers
def non_uniq(numbers):
    numbers.sort()
    print(numbers)
    non_uniq = []
    i = 0
    for n in numbers:
        while i < len(numbers) - 1:
            if numbers[i] == numbers[i + 1]:
                non_uniq.append(n)  
            i += 1 
            break
    return non_uniq

## Min & max values of array
def min_max(numbers):
    max = numbers[0]
    min = numbers[0]
    for n in numbers:
        if n > max:
            max = n
        if n < min:
            min = n
    print("Max value is: ", max, "Min value is: ", min)
    
## How to Find all Pairs in Array of Integers Whose sum is Equal to a Given Number
def pairs_sum (pairs, sum):
    # учитывает каждый элемент, кроме последнего
    for i in range(len(pairs) - 1):
        # начинается с i-го элемента до последнего элемента
        for j in range(i + 1, len(pairs)):
             # если искомая сумма найдена, вывести ее
            if pairs[i] + pairs[j] == sum:
                print('Pair found', (pairs[i], pairs[j]))

## How to find all duplicate elements in an array and the number of repetitions
def duplicate (numbers):
    counter = {}

    for e in numbers:
        counter[e] = counter.get(e, 0) + 1
    dupl = {element: count for element, count in counter.items() if count > 1}
    print(dupl)

## How to delete the duplicated elements from array
def del_duplicated (numbers):
    temp = []
    for n in numbers:
        if n not in temp:
            temp.append(n)
    print(temp)

## How to sort array. the most speedest way (5 algoritms) 1:
## Bubble sort (the slowest method)  - other algoritms is too difficult for me yet
def bubble_sort(numbers):
    swapped = True # Flag for swapped
    while swapped:
        swapped = False
        for n in range(len(numbers) - 1):
            if numbers[n] > numbers[n + 1]:
                # Меняем элементы
                numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    print(numbers)

array = [1, 2, 3, 4, 5, 7, 8, 9, 10]
numbers = [-3, 1, 2 ,2 ,2 ,4, 4, 5, 6, -7, 7, 7, 7]
pairs = [1, 4, 2, 3, 1, 2, 2, 1, 3, 2]

#print('The missing number is', misNum(array))
#print('Unique elements of list', uniq(numbers))
#print('Non uniq elements of list', non_uniq(numbers))
#min_max(numbers)
#pairs_sum(pairs, 5)
#duplicate(numbers)
#del_duplicated(numbers)
#bubble_sort(pairs)

