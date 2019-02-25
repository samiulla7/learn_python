'''
^a...s$      ---- any five letter string starting with a and ending with s.
Expression	String	    Matched?
^a...s$	    abs	        No match
            alias	    Match
            abyss	    Match
            Alias	    No match
            An abacus	No match
'''
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
'''
Here, we used re.match() function to search pattern within the test_string. 
The method returns a match object if the search is successful. If not, it returns None.
'''

#### MetaCharacters  ###
'''
[] . ^ $ * + ? {} () \ |

[] - Square brackets
Square brackets specifies a set of characters you wish to match.
Expression	    String	    Matched?
[abc]	        a	        1 match
                ac	        2 matches
                Hey Jude	No match
                abc de ca	5 matches    

You can also specify a range of characters using - inside square brackets.
[a-e] is the same as [abcde].
[1-4] is the same as [1234].
[0-39] is the same as [01239].

You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.
[^abc] means any character except a or b or c.
[^0-9] means any non-digit character.


. - Period
A period matches any single character (except newline '\n').
Expression	String	Matched?
..	        a	    No match
            ac	    1 match
            acd	    1 match
            acde	2 matches (contains 4 characters)
            
'''

# Example 1: re.findall()

# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'  # Matches any decimal digit. Equivalent to [0-9] 

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']

# Example 2: re.split()

import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


import re
string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'
# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)
# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']


# Example 3: re.sub()
# Program to remove all whitespaces
import re
# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'   #Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].
# empty string
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)
# Output: abc12de23f456


# Example 5: re.search()
import re
string = "Python is fun"
# check if 'Python' is at the beginning
match = re.search('\APython', string)   # /A Matches if the specified characters are at the start of a string. 
if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  
# Output: pattern found inside the string


# match.group()
# The group() method returns the part of the string where there is a match.
# Example 6: Match object
import re
string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
# match variable contains a Match object.
match = re.search(pattern, string) 
if match:
  print(match.group())
else:
  print("pattern not found")
# Output: 801 35

# match.start(), match.end() and match.span()
# The start() function returns the index of the start of the matched substring. Similarly, end() returns the end index of the matched substring.
# >>> match.start()
# 2
# >>> match.end()
# 8
# The span() function returns a tuple containing start and end index of the matched part.
# >>> match.span()
# (2, 8)