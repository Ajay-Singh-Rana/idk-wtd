# P versus NP
- P verus NP is a problem in computer science which seeks answer to the question that 
whether or not every problem whose solution can be quickly verified can also be quickly solved.

Here, **P** is defined as the existence of an algorithm solving the task in polynomial time and vaires
as a polynomial function on the size of the input to the algorithm.

**NP** problems are defined as problems to which the answers can be verified in polynomial time yet no algorithm
exists to find the solution/answer in polynomial time.

**P != NP** is widely believed even though it hasn't been proved so. People believe that there are problems in NP that are 
harder to compute then verify.

Example -> The solution to a sudoku is easily verified (P). Though to calculate/compute the solution is not easy(NP).

**NP Completeness -** NP complete problems are a set of problems to each of which any other NP problem can be reduced in 
polynomial time and whose solution may still be verified in polynomial time.
NP complete problem is an NP problem that is at least as tough as any other problem in NP.

**NP hard -** NP hard problems are all problems to which all NP problems can be reduced (in polynomial time). And NP 
hard problems need not be NP (i.e. they need not have solutions verifiable in polynomial time).
NP hard is atleast as hard as the hardest NP problem.

![P vs NP](notes/PvsNP.png)
