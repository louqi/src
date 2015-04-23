'''
Created on 2015-4-22

@author: Administrator
'''

import test2222
import test3333
import test1111
print dir(test2222)
print test2222.__doc__
print dir(test3333)
print test3333.__doc__
print dir(test1111)
print test1111.__doc__

A,B,ARRAY =  test2222.cal(11,22,33,4)
print A,B,ARRAY

temp = 20
D = test3333.sum(A,B,temp,ARRAY)
print D

temp2 = 30
temp3 = 8
E = test1111.multiplication(D,temp2,temp3)
print E
