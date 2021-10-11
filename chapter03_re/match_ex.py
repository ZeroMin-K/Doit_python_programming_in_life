import re

pattern = r'life'
script = 'life'
print(re.match(pattern, script))
print(re.match(pattern, script).group())
