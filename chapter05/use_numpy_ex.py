import numpy as np

# a =np.array([[2,3], [5, 2]])
# print(a)

# d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])

# print(d)
# print(d[1][2])
# print(d[1, 2])
# print(d[1:, 3:])

# d = np.array([2, 3, 4, 5, 6])
# print(d)
# print(d.shape)

# e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
# print(e)
# print(e.shape)

# print(d.dtype)
# print(e.dtype)

# data = np.arange(1, 5)
# print(data.dtype)

# print(data.astype('float64'))
# print(data.astype('int32'))

# print(np.zeros((2, 10)))

# print(np.ones((2, 10)))

# print(np.arange(2, 10))

# a = np.ones((2, 3))
# print(a)
# b = np.transpose(a)
# print(b)

# arr1 = np.array([[2, 3, 4], [6, 7, 8]])
# arr2 = np.array([[12, 23, 14], [36, 47, 58]])

# print(arr1 + arr2)
# print(arr1 * arr2)
# print(arr1/arr2)

# arr1 = np.array([[2, 3, 4], [6, 7, 8]])
# arr3 = np.array([100, 200, 300])

# print(arr1.shape)
# print(arr3.shape)
# print(arr1 + arr3)

# arr1 = np.array([[2, 3, 4], [6, 7, 8]])
# arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(arr4.shape)
# print(arr1.shape)
# print(arr1 + arr4)

# arr1 = np.array([[2, 3, 4], [6, 7, 8]])
# arr5 = np.array([[9], [3]])
# print(arr5.shape)
# print(arr1)
# print(arr1 + arr5)

# d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
# d[:2] = 0
# print(d)

# d_list = [[1, 2, 3, 4, 5], 
#         [2, 4, 5, 6, 7], 
#         [5, 7, 8, 9, 9, ]]
# print(d_list)
# print(type(d_list))
# d_list[:2] = 0

arr4 = np.arange(10)
print(arr4)

print(arr4[:5])
print(arr4[-3:])

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
print(arr1)
print(arr1[1, 2])
print(arr1[:, 2])
