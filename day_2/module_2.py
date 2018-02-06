'''
Created on Feb 6, 2018

@author: Maggy
'''
import utils


if __name__ == '__main__':
    
    while True:
        valor = input('Introduza um valor inteiro: ')
        valor = utils.is_number(valor)
        if valor !=None: break
        
    if (valor % 2 == 0): print('even')
    else: print('odd')