'''
Created on Sep 21, 2018

@author: edgarcolin
'''
from dv_raw_classes import Data, ProgramVar, Test1_Data
from dv_standard_classes import PYStruct


f_t_d = Test1_Data('This is for test1')

print(hasattr(f_t_d,'feed_back_a_curren'))
print(f_t_d.info)
f_t_d.collect()


print(f_t_d.feed_back_a_current.varname)

print(f_t_d.feed_back_a_current.val)

print(f_t_d.feed_back_a_current.samples)


 