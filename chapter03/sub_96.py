import re

sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'

print(re.sub(r'dog', 'cat', sentence))
print(sentence)

words = 'I am home now. \n\n\nI am with my cat.\n\n'
print(words)
print(re.sub(r'\n', '', words))