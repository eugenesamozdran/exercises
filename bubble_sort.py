from collections.abc import Iterable

def bubble_sort(iter_obj, key=None, reverse=False): # bubble sorting algorythm
    
    # first, we check if argument is iterable
    # if yes and if it is not 'list', we convert the argument to a list
    if isinstance(iter_obj, Iterable):

        iter_obj = list(iter_obj)
        key = key if key is not None else lambda x: x
        length = len(iter_obj)
        
        # this is the sorting loop itself
        for i in range(length):
            for y in range(length-i-1):
                if key(iter_obj[y]) > key(iter_obj[y+1]):
                    iter_obj[y], iter_obj[y+1] = iter_obj[y+1], iter_obj[y]
                    
        # here we check if the result should be reversed or not            
        if reverse:
            return iter_obj[::-1]
        return iter_obj

    else:
        raise TypeError("first position argument expected to be iterable object")

a = [{"value": 42}, {"value": 32}, {"value": 40}, {"value": 56}, {"value": 11}]
a = bubble_sort(a, lambda x: x["value"])
print(a)
