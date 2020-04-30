'''
Complete the recursive function fibonacci() in the editor below. It must return the nth element in the Fibonacci sequence.

fibonacci has the following parameter(s):

n: the integer index of the sequence to return
Input Format

The input line contains a single integer, n.

Output Format

Locked stub code in the editor prints the integer value returned by the fibonacci() function.

Sample Input

3
Sample Output

2
'''


def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


n = int(input())
print(fibonacci(n))
