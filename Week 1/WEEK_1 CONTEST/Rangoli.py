'''
ita is fond of designing a rangolies . On a day she stated designing a rangoli . she started designing rangoli such that an 'n' star rangoli will be consisting of stars in the pattern such that each line of stars first decresing starting from one less than 2 times of 'n' untill 1 after that it will be gain increasing to one less than 2 times of 'n' and each line of stars will be preceded by spaces such that last star in each line is on the same vertical line
Refer to Sample inpus and explanations for clear understanding
Input Format

An single integer value in between 1 and 100 inclusive
Constraints

1<=n<=100

Output Format

series of stars and spaces refer to sample input and output
Sample Input 0

3
Sample Output 0

*****
 ****
  ***
   **
    *
   **
  ***
 ****
*****

Explanation 0

given n value is 3 . so total number of stars for each line will be starting from 5 (ie 3*2-1=5) and total stars will go on decreasing for each line . once it reaches one from the next line it will again goes on incrasing to 5 . Maximum number of spaces will be found in the middle most line which are equal to 4 ( ie 5-1 =4 )

Sample Input 1

2
Sample Output 1

***
 **
  *
 **
***
Explanation 1

given n value is 2 . so total number of stars for each line will be starting from 3(ie (2*2)-1=3 ) and total stars will go on decreasing for each line . once it reaches one from the next line it will again goes on incrasing to 3

Sample Input 2

1
Sample Output 2

*
'''

n = int(input())

m = n * 2 - 1
for i in range(m):
    for k in range(i):
        print(" ", end='')
    for j in range(m - i):
        print('*', end='')
    print()

for i in range(m - 1):
    for k in range(m - i - 2):
        print(" ", end='')
    for j in range(i + 2):
        print('*', end='')
    print()
