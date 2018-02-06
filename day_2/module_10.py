'''
Created on Feb 6, 2018

@author: Maggy
'''

if __name__ == '__main__':
    
    text = input('Some text: ')
    dict = {}
    for word in text.split(): ### other variant split(',') 
                                ##or split('\t') or split('space') -> by word
                                
        if word in dict: dict[word] += 1
        else: dict[word] = 1
    
    print(dict)
        
    