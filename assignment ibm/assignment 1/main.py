PM
Basic Python
1. Split this string
In [1]:
s = "Hi there Sam!"
In [2]:
print(s.split(""))

output : ['Hi', 'there', 'Sam!']

2. Use .format() to print the following string.
Output should be: The diameter of Earth is 12742 kilometers.
In [3]:
planet = "Earth"
diameter = 12742
In [4]:
print("The diameter of {} is {} kilometers.".format(planet,diameter))
'The diameter of Earth is 12742 kilometers'

output : 'The diameter of earth is 12742'


3. In this nest dictionary grab the word "hello"
In [5]:
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
In [6]:
sh=d['k1'][3]['tricky'][3]['target'][3]
print(sh)


Numpy
In [7]:
import numpy as np
4.1 Create an array of 10 zeros?
4.2 Create an array of 10 fives?
In [8]:
a0=[0]*10
In [9]:
print(a0)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
In [10]:
a5=[5]*10
In [11]:
print(a5)
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
5. Create an array of all the even integers from 20 to 35
In [12]:
arr=np.arange(20,35,2)
In [13]:
print(arr)
[20 22 24 26 28 30 32 34]
6. Create a 3x3 matrix with values ranging from 0 to 8
In [14]:
x =  np.arange(0,9).reshape((3,3))
In [15]:
print(x)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
7. Concatenate a and b
a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
In [16]:
a = np.array([[1, 2, 3]])
In [17]:
b = np.array([[4, 5, 6]])
In [18]:
np.concatenate((a,b),axis=0)
Out[18]:
array([[1, 2, 3],
       [4, 5, 6]])
Pandas
8. Create a dataframe with 3 rows and 2 columns
In [19]:
import pandas as pd
In [20]:
data = [['tom', 10], ['nick', 15], ['juli', 14]]
In [21]:
df = pd.DataFrame(data, columns=['Name', 'Age'])
In [22]:
df
Out[22]:
Name	Age
0	tom	10
1	nick	15
2	juli	14
9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023
In [23]:
date = pd.date_range(start ='1-1-2023',
         end ='02-10-2023')
In [24]:
for val in date:
  print(val)
2023-01-01 00:00:00
2023-01-02 00:00:00
2023-01-03 00:00:00
2023-01-04 00:00:00
2023-01-05 00:00:00
2023-01-06 00:00:00
2023-01-07 00:00:00
2023-01-08 00:00:00
2023-01-09 00:00:00
2023-01-10 00:00:00
2023-01-11 00:00:00
2023-01-12 00:00:00
2023-01-13 00:00:00
2023-01-14 00:00:00
2023-01-15 00:00:00
2023-01-16 00:00:00
2023-01-17 00:00:00
2023-01-18 00:00:00
2023-01-19 00:00:00
2023-01-20 00:00:00
2023-01-21 00:00:00
2023-01-22 00:00:00
2023-01-23 00:00:00
2023-01-24 00:00:00
2023-01-25 00:00:00
2023-01-26 00:00:00
2023-01-27 00:00:00
2023-01-28 00:00:00
2023-01-29 00:00:00
2023-01-30 00:00:00
2023-01-31 00:00:00
2023-02-01 00:00:00
2023-02-02 00:00:00
2023-02-03 00:00:00
2023-02-04 00:00:00
2023-02-05 00:00:00
2023-02-06 00:00:00
2023-02-07 00:00:00
2023-02-08 00:00:00
2023-02-09 00:00:00
2023-02-10 00:00:00
10. Create 2D list to DataFrame
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
In [25]:
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
In [26]:
df = pd.DataFrame(lists, columns =['Rollno','Name', 'Age'])
In [27]:
print(df)
   Rollno Name  Age
0       1  aaa   22
1       2  bbb   25
2       3  ccc   24
In [ ]:
