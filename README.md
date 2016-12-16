# Aiden

Aiden project includes two coding chanllenge programs(1A & 1B), both of which are command line tools that operate in terminals.

## Table of Contents
- [setup](#setup)
- [Solution1](#Solution1)
- [Solution2](#Solution2)
- [Improvement](#Improvement)

## setup

Clone/download the projects to local computer
open the terminal and cd to the directory that the projects are in 
set file permission by running "chmod a + x" + file name
eg.
```
chmod a + x tool.py
```
Call the program by running "./" + name of the coding file + parameters
(There are two coding files: 1A program is called "tool.py"; 1B program is called "tool2.py")
(correct way to format parameters will be discussed later)

eg.
```
cd /Users/emily/Desktop
chmod a + x tool.py
./tool.py 2 9 17
```

## Solution1

Coding file for solution1(1A) is called "tool.py". Given a value and an array with numbers, this program
returns a 1 or 0 indicating whether the numbers in the array can be used to reach the targeted value. 
('1' is yes;'0' is no; numbers in the array can be used more than once.)

### How to run the program

The program takes two parameters: a list of numbers & a value. When called from terminal, these two parameters must be inputted as a series of numbers without commas or brackets.
eg. [2,9] 17 --> 2 9 17
    [4, 6, 9] 35 --> 4 6 9 35
eg. find whether numbers in array A = [2,9] can be used to reach value 17
```
./tool.py 2 9 17
```

## Solution2

Coding file for solution2(1B) is called "tool2.py". Given a 10-20 digit number, the program returns a mix of 
numbers and letters which assist in remembering the original number. 

### Inspiration and thought process
My idea for this program is based on the keypad of phones in which every number except for 0 and 1 corresponds to 3-4 letters. 
In this program, I turned every digit of the given number except for 0 and 1 into their corresponding letters. I then implemented a text file of dictionary words to check whether there are any sequences of  digits of any length that can form a word with their corresponding letters. For those digits that cannot form a word I just leave them in their original position and combine them with words that are found. A single word or a  digit is considered an item; my criteria for best possible output is the one that has the least items.

In order to recall the original numbers, simply look at a keypad (such as on a mobile phone) and match the letter in the output with its corresponding number.

### How to run the program
The program takes one parameter, a 10-20 digit number. In order to call the program in terminal, directly write the number
eg.
```
./tool2.py 3462120646
```
## Improvement
The second program can be improved by speeding up the running time when the input doesn't have 0 and 1. The second program works well for phone numbers or other series of numbers that include 0 and 1 since 0 and 1 divide the number series into several parts to find possible words. However if the number contains consecutive 7 or more non-0-or-1 digits, the running time will be very slow.
Improvements can be made by turning current permutation function that returns all the permutations into a generator which only produce values when need, which saves a lot of time.

(Sorry, I wasn’t able to implement this improvement due to time constraints; I will look back into it if I have time.)
