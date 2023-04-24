# Suppose you have an algorithm that has two steps. When do you multiply the runtimes and when do you add them?

# O(A+B)
def add_runtime(arrA, arrB):
    for (int a: arrA):
        print(a);
    for (int b: arrB):
        print(b)

# O(A*B)
def multiply_runtime(arrA, arrB):
    for (int a: arrA):
        for(int b: arrB):
            print(a + "," + b)


# Rate of increase 
# O(x!) > O(2^x) > O(x^2) > O(x log x) > O(x) > O(log x)

''' Amortized time
ArrayList offers flexibility in size, will grow as you add elements
    Adding a new element: will create a new array with double the capacity and copy all the elements over to the new array -> O(N) time when array is full      
    Majority of the time it will take O(1) time
    
    Worst case happens once in a while; however, we double the size of the array every time, and the complexity of reaching the end approaches 1
    Therefore, the amortized time for each adding comes to O(1)
'''

''' Log N runtimes
    where the number of elements in the problem space gets halved each time -> likely O(log N) runtime
        finding an element in a blanace binary search tree is O(log N); each comparison we go either left or right and cut the space in half each time
'''

''' Recursive Runtimes
    When a recursive function makes multiple calls, the runtime will often look like O(branches^depth), where the branch is the number of times each recursive call
    branches. i.e. O(2^n)
    Space complexity is O(n)
    Although we have O(2^n) nodes in the tree total, only O(N) exist at any given time
'''

'''
    Sorting each string is O(s log s)
    Sort each string for every string: O(a * s log s)
    each string comparison takes O(s) time, there are O(a log a) comparisons - for a list 
    Sort each string for all strings: O(s * a log a)
    Sort the list: O(a log a)
    O(a * s log s) + O(a * s log a) = O(a * s (log a + log s))
'''

def int f(n):
    if (n <= 1):
        return 1;
    return f(n-1) + f(n-1)
# each function call has 2 children


# Pattern with recursive calls O(branches ^ depth)
# branches = fib(n-1) + fib(n-2)
# depth = n because this will run n times, creating n depth
def fib(n):
    if n <= 0:
        return 0
    elif n == 1
        return 1
    return fib(n-1) + fib(n-2)

