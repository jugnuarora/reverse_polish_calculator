# reverse_polish_calculator #

In this repository, a calculator is created that operates with reverse polish notation. It should take the string of characters and computes the result of the coputation that the string of chracters gives. It takes stacking into account with LIFO principle. The user can keep using the calculator again and again. The old calculated value is put in stack unless User says that it is a new calculation. If at any time user wants to see the stack, they can enter `s`. If they want to clear the stack entirely, they can enter `c`. And if they want to quit the calculator they can enter `q`. The working solution looks like this:

```
Operation(s)/Value(s): 4 5 +
Operation(s)/Value(s): s
Stack: 4.0, 5.0, +
Operation(s)/Value(s):  
Stack: 9.0
Operation(s)/Value(s): 7 sqrt
Operation(s)/Value(s): s
Stack: 9.0, 7.0, sqrt
Operation(s)/Value(s): 
Operation(s)/Value(s): s
Stack: 9.0, 2.64575131106
Operation(s)/Value(s): c
Operation(s)/Value(s): s
Stack: empty
Operation(s)/Value(s): q
```
