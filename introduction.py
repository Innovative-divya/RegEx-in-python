# importing re module 
import re
#Python has a built-in module named “re” that is used for regular expressions in Python. We can import this module by using the import statement.
#This Python code uses regular expressions to search for the word “portal” in the given string and then prints the start and end indices of the matched word within the string.
import re 
s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'portal', s) 
print('Start Index:', match.start()) 
print('End Index:', match.end()) 
#Note: Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \ character for its own escaping purpose.
#Before starting with the Python regex module let’s see how to actually write regex using metacharacters or special sequences. 

