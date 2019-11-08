#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) It has O(n) so its linier which means that the runtime will be constant

b) it has O(n^2) since there is a loop inside a loop. Each loop has O(n) but since its nested you multiply the parent by the child and get n^2

c) it has O(2^n) since it is increasing exponentially based on how many times it going to have to run recursion

## Exercise II

first I think there is some missing information. Am I allowed to go back and pick up the egg if I drop below floor f? Also, am I guaranteed to drop eggs the higher floor number I get? If both those are true than I would have a function with a variable for amount of eggs, one for floor number, and one for probability of dropping an egg. I would have a while loop to see if youve reached the top of the building. Inside I would have an if statement to see if your higher than 'f'. If true, than you do not need to go back to pick up the eggs, but you would have to subtract lost eggs from amount. If you are lower than 'f' you can go back and pick up the egg without losing an amount. I would also have the entire thing nested in a is_at_main_floor while loop.
each while loop would have a variable that defaults to true, than is immediately set to false once the loop starts. You could then return the final amount of eggs once you reach the top. Since there is a while loop inside of a while loop that is already O(n^2). Each if statment has a constant big O so it would be 0(n+n) which is O(n). the function is still quadratic with a big O of O(n^2)
