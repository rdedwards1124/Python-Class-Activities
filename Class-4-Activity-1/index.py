# result = lambda parameters: expression

# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.

the_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = sorted(the_list, key=lambda number: number[1])

print(sorted_list)


# Write a lambda function to cube every element of a list.

Original_list = [3,6,9,2]
cubed_list = [num*num*num for num in Original_list]

print(cubed_list)


# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.

alist = [3, 6, 9, 2]
fact = [num % 2 == 0 for num in alist]

print(fact)


# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100)

ranger = [num for num in range(1, 101)]

print(ranger)


# Use a dictionary comprehension to count the length of each word in a sentence.

sentence = "The quick brown fox jumped over the fence."
word_lengths = {word: len(word) for word in sentence.split()}

print(word_lengths)