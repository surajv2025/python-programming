# create attandance data of 20 student for 5 days using 0 AND 1
import numpy as np

attendance = np.array([
    [0,1,1,0,1],
    [1,1,1,0,1],
    [1,1,1,1,1],
    [0,1,1,0,1],
    [0,0,0,0,0],
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,0,0,1,1],
    [0,1,1,1,1],
    [0,0,0,0,0],
    [1,1,0,1,0],
    [1,1,0,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [1,0,0,1,0],
    [0,0,0,1,1],
    [1,0,0,1,1],
    [0,1,1,0,0],
    [1,1,1,0,1],
    [1,0,0,0,1]
])
print(attendance)
at=np.sum(attendance,axis=1)
print("total attandance of each student")
for i in range(20):
    print(f'Student:{i+1}:Present{at[i]}')
ap=(at/5)*100
print("total percentage of each student")
for i in range(20):
    print(f'Student:{i+1}:{ap[i]}%')
print("Student with below 60%")
for i in range(20):
    if ap[i]<60:
       print(f'Student:{i+1}:{ap[i]}%')
        
    