# ShortestSubstring
HackerRank Shortest Substring problem

## Problem
Given a string comprised of lowercase letters in the range `ascii[a-z]`, determine the length of the smallest substring that contains all of the letters present in the string.

For example, given the string `s = dabbcabcd`, the list of all characters in the string is `[a, b, c, d]`. Two of the substrings that contain all the letters are `dabbc` and `abcd`. The shortest substring containing all the letters is 4 characters long, `abcd`.

## Solution
The solution involves using two pointers to create a sliding window in our string. Statring with both indices at position 0, we slide one of them (the right index) to the right and keep the other one (the left index) still. With each position advanced by the right index, we check if the substring between the left index (inclusive) and the right index (exclusive) is valid, i.e. contains all characters of the string. The naive way to do this is try all the possibilities, by iterating over all substrings all checking if they are valid. This runs in $O(nˆ2)$.

To make the code more efficient we can keep track of the frequency of the characters at each sliding window. Everytime we slide the right index, we increment the frequency for the character it reached. If every character has a frequency of one, we have found a possible substring. Now, we need to contract the substring by sliding the left index until it reaches the current position of the right index. But first, we already have a valid substring, so we get its length and compare to the previously stored minimum length. If it is lower, it is the new shortest substring. Everytime we slide the left index, the left character does not belong to the substring anymore. Now we check if the substring is still valid. If the ingored character on the left has now a frequency of 0, the substring is not valid anymore and we to slide the right index again. Thsi goes on until we reach the end of the string. The new solution runs in $O(n)$, where n is the length of the string.

### Code
The code is composed by a single method `shortest_substring()` tha runs all the algorithm.

### Dependencies
- Python 3.7+

### Usage
Just run `solution.py` with `$ python solution.py`. Only python 3.7 is supported!