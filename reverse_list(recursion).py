#reversing the list using recursion:

def reverse_list(lst, start=0, stop=1):
    if start<stop-1: # (if at least 2 elements:) We can also write if start<stop-1: 
        #scenarios: When start == stop, the implicit range is empty, and when start == stop−1, 
        #the implicit range has only one element.
        
        lst[start],lst[stop]=lst[stop],lst[start]  # swap first and last
        reverse_list(lst,start+1,stop-1)  # recur on rest
       
print(lst)

#or

def rev(lst):
    if len(lst) == 0: return []
    return [lst[-1]] + rev(lst[:-1])


#reverse string
def rev_string(string):
    if len(string)==0:
        return string
    else:
        return rev_string(string[1:])+string[0]
        # string='akshay'
        # kshay+ a =kshaya
        # shaya+ k =shayak and so on