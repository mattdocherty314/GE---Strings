# Genetic Evolution of Strings
## Overview
This is a simple Genetic Evolution Python3 script which applies a genetic evolution
program on a string to reach a target string. Included is a sample output of it
attempting to reach 'Matt' with a mutatation rate of 1%, 1000 species per generation
and 1000 generations total. It was made in response to hearing about how a genetic neural network works and wanting to attempt to recreate it.

## Dependencies
* Python3 (tested to v3.6.5)

## Debugging
This program has been tested on Python 3.6.5 without any issues. If you run into any
errors please make sure you are on this version because it is known to work. If you
still are having issues on the aforementioned version, just send me a message on my
[GitHub](https://github.com/mattdocherty314)

## Program Use
When asked to for the desired gene you have to enter the target string.
When asked for a mutation chance, enter the denominator of the fraction, e.g. 20% =
5, ideal is 1% (enter 100)
When asked for the number of species in each generation (more = longer on each
generation, higher success).
When asked for the number of generations (more = longer overall, higher success) 
The time estimated is the estimated time on mid-range gear. Expect it to take either,
faster or slower than the estimate compared to single core performance.

## Version History
### v1.0.0
* Added the base genetic evolution program

## TODO
* Allow the program to be run within the terminal
* More error catching
* Better comments in code
* Try to find a better fitness function
* Input validation
* Add verbose toggle
* Implement a faster sort algorithm
