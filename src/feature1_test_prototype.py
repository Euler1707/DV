'''
Created on Sep 17, 2018

This module will outline what 
the test of the first feature will do 


@author: edgarcolin
'''

from dvtool_functions import error_message, range_check, var_samples


def feature1_test():
    
    error = 0
    
    feat1_variable1 = 'var1';
    feat1_variable2 = 'var2';
    feat1_variable3 = 'var3';
    feat1_variable4 = 'var4';
    feat1_variable5 = 1;
    feat1_variable6 = 1;
    
    range_check(feat1_variable1)
    error_message()
    error += 1
    
    range_check(feat1_variable2)
    error_message()
    error += 1
    
    range_check(feat1_variable3)
    error_message()
    error += 1
    
    
    range_check(feat1_variable4)
    error_message()
    error += 1
    
    var_samples()
    error_message()
    error += 1
    
    
    if feat1_variable5 == 0:
        error_message()
        error += 1
        
    if feat1_variable6 == 0:
        error_message()
        error += 1
        
    print("\nFeature1 testing has now been completed")
    print("ERRORS in feature 1 test = " + str(error))
    


feature1_test()




    
    
    