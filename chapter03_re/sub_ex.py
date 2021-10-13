import re

sentence = 'I have a lovely dog, I am not telling alie. What a pretty dog! I love this dog.'

print(re.sub(r'dog', 'cat', sentence))

words = 'I am home now. \n\n\nI am with my cat.\n\n'
print(re.sub(r'\n', '', words))
