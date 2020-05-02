'''
You will be given 'n' positive integers find the . exclude the maximum and minimum entries of those n numbers and find the sum of remaining all numbers . if only two numbers are given then return 0 as output . if there are duplicates of smallest or largest number then removing only one entry among those duplicate values
Input Format

first line of input will be consisting of integer value n
second line of input will be consisting of n space seperated integer values
Constraints

2<= n <=100

Output Format

An integer value corresponding to sum of n-2 numbers
Sample Input 0

5
1 2 5 4 3
Sample Output 0

9
Explanation 0

here minimum value is 1 and maximum value is 5 so after removing those two values the values remaining are 2 , 3 , 4 . sum of these values is 9 . so output is 9
Sample Input 1

8
4 2 5 6 2 4 6 3
Sample Output 1

24
Explanation 1

among the given 8 values smalest number is 2 and largest number is 6 . as theere are multiple 2's and multiple 6's remove one instance of 2 and one instance of 6 then numbers remaining are 4 , 5 , 6 , 2, 4 , 3 sum of all these is 4+5+6+2+4+3 = 24

Sample Input 2

3
8 9 7
Sample Output 2

8
'''

n = int(input())
l = list(map(int,input().split()))
l.remove(max(l))
l.remove(min(l))
print(sum(l))