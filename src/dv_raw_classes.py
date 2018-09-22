'''
Created on Sep 21, 2018

@author: edgarcolin
'''

import abc
from dv_standard_classes import PYStruct




class ProgramVar:
    
    def __init__(self, val = 0):
    
        self.val = val
        
        
        
class Data(metaclass=abc.ABCMeta):
    
    def __init__(self,info = ''):
        
        self.info = info
    
    @abc.abstractmethod
    def collect(self):
        pass
    
    

class Test1_Data(Data):
    
    def __init__(self, info = ''):
        Data.__init__(self, info)
        self.feed_back_a_current = PYStruct()
    
    def collect(self):
        
        self.feed_back_a_current = PYStruct(varname = 'feed_back_a_current', unit = 'A', val = 150, samples = [156,157,145])
        
    
    
    
    
    
            
    