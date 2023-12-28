#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]
input_num_list = [0, 1, 3, 5, 7, 8, 9]
result = return_evens(input_num_list)

print(result)

def make_exclamation(sentence_list):
   return[s + '!' for s in sentence_list ]
input_sentence_list = ["Hello", "I'm doing great", "Python is fun"]
result= make_exclamation(input_sentence_list)
print(result)