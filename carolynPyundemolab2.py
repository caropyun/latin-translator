###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program is a driver demo for the Translator class.
# Solution File: carolynPyundemolab2.py
# Date:  1/18/22
# Benchmarking: Trial 1: 0.0000300290 secs,
# Trial 2: 0.0000283440 secs, Trial 3: 0.0000292470 secs,
# Trial 4: 0.0000355630 secs, Trial 5: 0.0000272540 secs
# Complexity: O(n)
#

# Import the Translator class from the carolynPyunLab2 module
from carolynPyunLab2 import Translator
import timeit

phrase = input("Enter a latin phrase: ")
word = Translator(phrase)
t1 = timeit.Timer("word.translate()", "from __main__ import main, word; "
                                      "from carolynPyunLab2 import Translator; "
                                      "word.process_file('latin.txt')")


def main():
    times = t1.repeat(1, 1)
    t = times[0]
    print()
    print("%.10f secs" % t)


if __name__ == '__main__':
    main()

# Program run
'''
Enter a latin phrase: post hoc ergo propter hoc
after this therefore because of this 
0.0000300290 secs

Enter a latin phrase: carpe diem
* * 
0.0000283440 secs

Enter a latin phrase: alea iacta est
* * is 
0.0000292470 secs

Enter a latin phrase: in vino veritas
in * truth 
0.0000355630 secs

Enter a latin phrase: affectus forte ferrum
influenced by iron 
0.0000272540 secs
'''
