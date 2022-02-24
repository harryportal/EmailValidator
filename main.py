import re

"""
MetaCharacters	Description
 \ Used to drop the special meaning of character following it
[]	Represent a character class
^	Matches the beginning
$	Matches the end
.	Matches any character except newline
|	Means OR (Matches with any of the characters separated by it.
?	Matches zero or one occurrence
*	Any number of occurrences (including 0 occurrences)
+	One or more occurrences
{}	Indicate the number of occurrences of a preceding regex to match.
()	Enclose a group of Regex"""

word = 'geeks for geeks: portal in the mud'
match = re.search(r'portal', word)  # this simply search for the specified word
print("Start Index:", match.start())
print("End Index:", match.end())

word = 'geeks.geeks'
match = re.search(r'\.', word)  # the \ is used to remove the meaning of the special character is preceeds
print(match)

match = re.search(r'[a-z]', word)  # matches the first letter in the range of character class
print(match)

match = re.search(r'[^a-g]', word)  # matches the first letter not in the character class
print(match)

match = re.search(r'ge*', word)  # matches  zero or multiple occurrences of the string before it
print(match)

match = re.search(r'fa+', word)  # matches one or multiple occurrence of the preceding string
print(match)

string = "Hello my Number is 123456789 and my friend's number is 98765432"
match = re.findall(r'[0-9]+', string)    # to find every string that matches the pattern
print(match)

pattern = re.compile('[0-9]+')
print(pattern.findall(string))


