import pandas as pd

data = {'name' : ['Mark', 'Jane', 'CHris', 'Ryan'],
        'age' :[33, 32, 44, 42],
        'score' :[91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)

# print(df)

# print(df.sum())

# print(df.mean())

print(df.age)
print(df['age'])
