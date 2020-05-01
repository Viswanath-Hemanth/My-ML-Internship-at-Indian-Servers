
'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be
of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format:

The first line contains an integer,n , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''





if __name__ == '__main__':
    N = int(input())

commands = []
cmds = []
final_arr = []

for _ in range(N):
    commands.append(input())

for _ in range(N):
    cmds.append(commands[_].split(" "))

for i in range(N):
    if (cmds[i][0] == 'insert'):
        final_arr.insert(int(cmds[i][1]),int(cmds[i][2]))
    if (cmds[i][0] == 'remove'):
        final_arr.remove(int(cmds[i][1]))
    if (cmds[i][0] == 'print'):
        print(final_arr)
    if (cmds[i][0] == 'sort'):
        final_arr.sort()
    if (cmds[i][0] == 'pop'):
        final_arr.pop()
    if (cmds[i][0] == 'reverse'):
        final_arr.reverse()
    if (cmds[i][0] == 'append'):
        final_arr.append(int(cmds[i][1]))

