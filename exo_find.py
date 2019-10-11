# Software testing exercise: Hoare's FIND
#
# ** Requirements
#
# Debian/Ubuntu:
# $ sudo aptitude install python-hypothesis python-pytest python-pytest-cov
#
# You may also install the equivalent packages using pip or another
# package manager; the names will slightly vary.
#
# ** Reminder on how to run
#
# Running your program should NOT run tests:
# $ python ./find.py
#
# Tests should be executed using pytest:
# $ pytest find.py
# $ pytest --hypothesis-show-statistics find.py 
# $ pytest --cov=. find.py
#
# FYI here's how to obtain a coverage report for the
# normal execution of your file:
# $ python-coverage run find.py
# $ python-coverage html
#
# ** Instructions
#
# Implement the functions partition and sort below. Each one must
# be unit-tested, with at least one randomized test using hypothesis.
# The test coverage should be complete (all lines except __main__).
# Warning: do not roll your own testing system !
# Use pytest and hypothesis in a standard way, otherwise you'll likely
# violate one of the key ideas explained during the lecture...

import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists

# The function partition(a,mid) takes an array a and a mid-value mid
# and permutes the elements of a to put
#  * first the elements strictly smaller than mid,
#  * then the elements equal to it,
#  * and finally the strictly larger elements.
#
# This permutation can be operated in place, or a new array can be returned.
#
# The function should also return two indices indicating the boundaries
# of the three zones. The precise semantics of these indices is left up to
# you.
#
# The implementation should proceed in a single traversal of the array
# (a priori maintaining three indices during that traversal, and swapping
# elements of the array). An implementation using filter(), map() and
# array concatenation() is forbidden, as it would kill the exercise.
def partition(a,mid):
    """
    Rearrange l'ordre des elements de a et renvoie deux entier i, j tel que :
        Pour tout k < i-1 : a[k] < mid
        Pour tout k >= j : a[k] > mid
        Pour tout k E [i-1,j-1] : a[k] = mid
    """
    i = 0
    i0 = 0
    j = len(a)
    n = len(a)
    while (i0 < j) :
        if a[i0] < mid :
            a[i],a[i0] = a[i0],a[i]
            i = i + 1
            i0 = i0 + 1
        elif a[i0] > mid :
            a[j-1],a[i0] = a[i0],a[j-1]
            j = j - 1
        elif a[i0] == mid :
            i0 = i0 + 1
    i += 1
    return (i,j)
    assert False

# Implement sorting by recursively calling the above partition function.
# The choice of mid-value is not specified. A naive choice (e.g. the
# first element of the array) is accepted.
def sort(a):
    """ 
    Renvoie une liste triee ayant les memes elements que a
    """
    n = len(a)
    if (n == 1 or n == 0) :
        return a
    valeur = a[0]
    (i,j) = partition(a,valeur)
    l1 = sort(a[0:i])
    l3 = sort(a[j:n])
    l2 = []
    for k in range (0, j-i) :
        l2.append(valeur)
    return l1 + l2 + l3
    assert False

if __name__ == "__main__":
    print ("Hello, and goodbye.")


#On ecrit les fonctions de test
        

def test_unique () :
    a = [9,0,5,7,3,6,10,7,9,8]
    b = [0,3,5,6,7,7,8,9,9,10]
    a = sort(a)
    assert (a == b)
    
@given(lists(elements=integers()),integers())
def test_partition(l,k) :
    (i,j) = partition(l,k)
    boolean = True
    for q in range (0,len(l)) :
        if (q < i-1) and (l[q] >= k) :
            boolean = False
        elif (q >= j) and l[q] <= k :
            boolean = False
        elif (q >= i-1 and q < j and l[q] != k) :
            boolean = False
    assert boolean
    
@given(lists(elements=integers()))
def test_tri(l) :
     boolean = True
     tri_l = sort(l)
     for i in range (0,len(l)-1) :
         if tri_l[i] > tri_l[i+1] :
             boolean = False
     assert boolean
     

