import re

pattern = r'is'
script = 'Life is so cool'

print(re.search(pattern, script).group())
print(re.search(r'Life', script).group())
print(re.search(r'cool', script).group())
