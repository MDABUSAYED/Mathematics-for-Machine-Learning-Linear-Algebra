# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:50:19 2018

@author: SAYED
"""


import numpy as np

A = [[1, 1, 3],
     [1, 2, 4],
     [1, 1, 2]]
Ainv = np.linalg.inv(A)
print Ainv



# In[ ]:


import numpy as np
A = [[4, 6, 2],
     [3, 4, 1],
     [2, 8, 13]]

s = [9, 7, 2]

r = np.linalg.solve(A, s)
print r

# In[ ]:
import numpy as np
A = [[1.0, 0.0, 1/3.0],
     [0.0, 1.0, -1/4.0]]

B=[[5.0,-1.0,-3.0,7.0],
   [4.0,-4.0,1.0,-2.0],
   [9.0,3.0,0.0,12.0]]

print np.dot(A,B)

Rp = [[8,  0,  -3,  11],
      [7/4,  -19/4,  1,  -5]]
      
# In[ ]:
T = [[1,0],
    [2,-1]]     
C = [[1,0],
     [1,1]]

print np.dot(np.dot(np.linalg.inv(C),T),C)

# In[ ]:

T = [[2,7],
    [0,-1]]     
C = [[1,0],
     [1,1]]

print np.dot(np.dot(T,T),T)