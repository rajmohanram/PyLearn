# Anything after hash (#) symbol is a comment (single line comment)
"""
Anything between 3 quotes (single or double) is a multi line comment.
This is second line of a multi-line comment.
"""

# Simply print a string using print() built-in function (came pre-coded with standard python installation)
print( "Hello Ajanthan, Welcome to the world of Python Programming")

# Let us declare some variables here
# Variables will be looked at in the next section
name = 'Ajanthan'
language = 'Python'

# String formatting: options - 1
# Concatenation of string with the declared variables
print("Hello "+ name + ", Welcome to the world of " + language + " Programming")

# String formatting: options - 2
# Format method - Positional arguments [order of argument is important
print("Hello {}, Welcome to the world of {} Programming".format(name, language))

# String formatting: options - 3
# Format method - Named arguments
print("Hello {user}, Welcome to the world of {lang} Programming".format(lang=language, user=name))

# String formatting: options - 4 (recommended)
# String literal method
print(f'Hello {name}, Welcome to the world of {language} Programming')
