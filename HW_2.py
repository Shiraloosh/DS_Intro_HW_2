# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:34:23 2022

@author: shir_al
"""
#A
sentence = input("Enter sentence:-")

reverse_word = input("Enter the reversted word:-")

def reverse(sentence,reverse_word):
    if reverse_word.isalpha():   
        if reverse_word  not in sentence:
            return("The word was not found")
        else:
            newsub=reverse_word[::-1]
            return(sentence.replace(reverse_word, newsub,1))
    else:
        return("invalid input" )
    
print(reverse(sentence,reverse_word))
#B
#def compute_equation(equation) :
  #  oparator={"*","+","-","/","**"}
 #   for char in equation:
   #     if char in oparator: