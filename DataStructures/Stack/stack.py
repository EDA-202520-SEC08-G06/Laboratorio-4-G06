# PILAS

from DataStrucutres import array_list.py as list 
from DataStrucutres import single_linked_list.py as list



def new_stack():
    
    my_stack = list.new_list()

    return my_stack



def push(my_stack): 
    
    return  list.add_first(my_stack)



def pop(my_stack):
    
    return list.remove_first(my_stack)



def is_empty(my_stack) -> bool: 
    
    return list.is_empty(my_stack) 



def top(my_stack): 
    
    return list.first_element(my_stack)



def size(my_stack) -> int: 
    
    return list.size(my_stack) 

