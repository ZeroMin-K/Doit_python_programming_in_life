import re

sentence = 'I have a lovely dog, really. I am not telling a lie'

print(re.findall(r'\w+ly', sentence))