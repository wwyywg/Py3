import pandas as pd
import numpy as np
import string

# pd1 = pd.Series([1,2,3,4,5])
# print(pd1)
# print(type(pd1))

# pd2 = pd.Series(np.arange(10), index=list(string.ascii_uppercase[:10]))
# print(pd2)

# pd3 = pd.Series([1,23,2,2,1],index=list("abcde"))
# print(pd3)

# temp_dict = {"name": "xiaohong", "age": 30, "tel": 10086}
# pd4 = pd.Series(temp_dict)
# print(pd4)

a = {string.ascii_uppercase[i]: i for i in range(10)}
print(a)

print(pd.Series(a))

b = pd.Series(a, index=list(string.ascii_uppercase[5:15]))
print(b)

print(a.dtype)