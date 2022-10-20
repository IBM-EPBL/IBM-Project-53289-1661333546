Assignment 1

1. Split this string

s = "Hi there Sam!";

print(s.split())

output=['Hi', 'there', 'Sam']


2. Use .format() to print the following string.
Output should be: The diameter of Earth is 12742 kilometers.


planet = "Earth"
diameter = 12742


print('The diameter of {} is {} kilometers'.format(planet,diameter));

output:The diameter of Earth is 12742 kilometers.


3. In this nest dictionary grab the word "hello"

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])
Output='hello'


Numpy

import numpy as np

4.1 Create an array of 10 zeros?



a0=[0]*10

print(a0)

output=[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

4.2 Create an array of 10 fives?
a5=[5]*10

print(a5)

output=[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

5. Create an array of all the even integers from 20 to 35

arr=np.arange(20,35,2)

print(arr)

output=[20 22 24 26 28 30 32 34]


6. Create a 3x3 matrix with values ranging from 0 to 8

x =  np.arange(0,9).reshape((3,3))

print(x)

output=[[0 1 2]
        [3 4 5]
        [6 7 8]]


7. Concatenate a and b

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

c=np.concatenate((a,b),1)

np.concatenate((a,b),axis=0)


output=[[1, 2, 3]
       [4, 5, 6]]


Pandas

8. Create a dataframe with 3 rows and 2 columns

import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]

df = pd.DataFrame(data, columns=['Name', 'Age'])

df

Output=
    Name	Age
0	tom	    10
1	nick	15
2	juli	14


9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

from datetime import timedelta,date
def daterange(date1,date2);

for n if in_range(int((date2-date).days)+1):

yield date1+timedelta(n)

start_dt=date(2023,1,1)

end_dt=date=date(2023,10,2)

for dt in daterange(start_dt,end_dt);

print9dt.strftime("yy-%m-%d")

output=1st jan 2023
        10th feb 2023


10. Create 2D list to DataFrame

import pandas as pd
import numpy as np

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df = pd.DataFrame(lists, columns =['Rollno','Name', 'Age'])

print(df)
   Rollno Name  Age
0       1  aaa   22
1       2  bbb   25
2       3  ccc   24