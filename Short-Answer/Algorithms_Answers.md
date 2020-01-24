#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) it has O(logn) cause a is increaseing faster than hight the number n is


b) its o(n) cause the while loop isnt increasing exponentially if it was a double for loop both in range(n) then it would be O(n^2)


c) its O(n) cause it doesnt matter what bunnies is and the 2 is a constant so it gets dropped

## Exercise II

Its going to be a function that takes two arguements, one for the number of storys and one for the floor that the eggs break on.  in order to find what floor the eggs break on you can take the storys and divide it by two.  you could then check to see if the floor is higher or lower than the storys/2.  Whatever the answer is you run the same funtion on the storys and keep checking if it is higher or lower until you are able to narrow it down to one number which is the floor that the eggs break on.  I think this i a binary search approach.  I guess you do a linear and loop through all the number of storys until you find the floor, but that would take longer.
