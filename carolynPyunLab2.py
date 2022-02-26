###
# CS 3C Advanced Data Structures and Algorithms in Python
# Lab 2: Timing and Big O
# Application: Translator Class
# Solution File: carolynPyunLab2.py
# Date:  1/18/22
#
class Translator:

    def __init__(self, phrase):
        self.latin_phrase = phrase
        self.latin_list = None

    def process_file(self, file_path):
        my_file = open(file_path, 'r')
        self.latin_list = {}    # dictionary of latin and english translations
        for next_line in my_file:
            (latin, english) = next_line.split(",")
            new_english = english.rstrip('\n')[1:]
            self.latin_list[latin] = new_english
        my_file.close()

    def translate(self):
        latin_words = self.latin_phrase.split(" ")
        for word in latin_words:
            try:
                print(self.latin_list[word], end=" ")
            except KeyError:    # If not found in dictionary, marked with *
                print("*", end=" ")
