import re

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script)

pattern = r'life'
script = 'Life is so cool'
refinder(pattern, script)

pattern = r'is'
script = 'Life is so cool'
refinder(pattern, script)
