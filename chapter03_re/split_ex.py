import re

sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', sentence))

data = 'a:3; b:4; c:5'

for i in re.split(r';', data):
    print(re.split(r':', i))
