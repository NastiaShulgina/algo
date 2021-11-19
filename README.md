Farmer John built a new long cattle unit, with N (2 <= N <= 100,000) sections. The sections are located along a straight line in positions x1, ..., xN (0 <= x-i <= 1 000 000 000).

His C (2 <= C <= N) cows do not like the new building and become aggressive one to one when they are placed in adjacent stalls. To avoid a situation where cows can harm a friend, a farmer who wants to place aggressive cows in stalls so that the minimum distance between any of them is as large as possible. What is the largest minimum distance?

Inboxes are contained in a file where:
The first line contains two integers separated by a comma: N and C
The following lines 2..N + 1: line i + 1 contains an integer that means the number of free stall x-i
Input:

5 3
1
2
8
4
9

Output:
3
Explanation:
The farmer has 5 cows, 3 of which are aggressive. They can be rotated in stalls 1, 4 and 8 or 1,4, 9. Thus, the minimum value of the maximum distance is 3

Hint:
Since we have at least two cows, the best thing we can do is place them in the pen in the first free stall and at the end
