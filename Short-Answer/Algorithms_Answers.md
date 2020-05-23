#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


b)


c)

## Exercise II
Assumptions: 
If an egg doesn’t break when dropped from some floor, then it will not break when dropped from any lower floors. (Less than f)

An egg that survives a fall can be used again.

A broken egg must be discarded.

The effect of a fall is the same for all eggs.

If an egg breaks when dropped, then it would break if dropped from a higher floor (Greater than f).


linear O(n) would be most reliable but not most efficient: drop an egg from each floor (lowest floor to highest floor). When the egg is finally broken, you know which floor = f. Worst case scenario would take n throws 

another approach would be to split the floors (1/nth) = drop your first egg from the say 1/2, halfway up the building. Whether it breaks or not, determines the next move: for example if n = 100 and you drop the egg from the 50th floor and it breaks, you now only have to check floors 1-50 instead of floors 1-100. - logarithmic (i think) 
