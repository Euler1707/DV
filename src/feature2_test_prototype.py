'''
Created on Sep 17, 2018

@author: edgarcolin
'''


'''
Created on Sep 17, 2018

This module will outline what 
the test of the first feature will do 


@author: edgarcolin
'''

from dvtool_functions import error_message, range_check, var_samples
from dvtool_functions import only_feature2test

def feature2_test():
    
    error = 0
    
    feat2_variable1 = 'var1';
    feat2_variable4 = 'var4';
    feat2_variable5 = 1;
    

    # Performing only 2 range checks    
    range_check(feat2_variable1)
    error_message()
    error += 1
    
 
    range_check(feat2_variable4)
    error_message()
    error += 1
    
    var_samples()
    error_message()
    error += 1
    
    
    # Performing 1 Ground Check
    if feat2_variable5 == 0:
        error_message()
        error += 1
        
     
    only_feature2test()    
        
    
        
    print("\nFeature2 testing has now been completed")
    print("ERRORS in feature 2 test = " + str(error))
    


feature2_test()

