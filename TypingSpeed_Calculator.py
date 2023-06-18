# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:29:21 2023

@author: Arsalan Dawalatabad
"""

import time

def calculate_typing_speed(text, elapsed_time):
    words = len(text.split())
    seconds = elapsed_time / 60
    speed = words / seconds
    return speed

def calculate_accuracy(prompt, user_input):
    prompt_words = prompt.split()
    user_words = user_input.split()
    correct_words = 0
    
    for prompt_word, user_word in zip(prompt_words, user_words):
        if prompt_word == user_word:
            correct_words += 1
    
    accuracy = (correct_words / len(prompt_words)) * 100
    return accuracy

def test_typing_speed():
    prompt = "\nThe quick brown fox jumps over the lazy dog\n"
    print("Type the following sentence:")
    print(prompt)
    print("Press Enter when you're ready to start.")
    input()
    print("START!...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    speed = calculate_typing_speed(user_input, elapsed_time)
    accuracy = calculate_accuracy(prompt, user_input)
    
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
    print("Your typing speed: {:.2f} words per minute".format(speed))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == '__main__':
    
    print("How many times you want to practice: ")
    practice_count = int(input())
    
    for x in range(0,practice_count):
        print(int(x+1),": out of ",practice_count)
        test_typing_speed()
