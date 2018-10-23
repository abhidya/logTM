# logTM
A turing machine to solve logarithmic calcuations

# Constraints:

n >= 1
k is an integer equal to the log base 2 of a number. if the log base 2 of a number contains a fraction, then k is rounded up to the next whole number. 


# Input:
log(n)

# Output:

# Process:

1. base10-unary.txt

input: log(n), (n being a positive whole number greater than 0),  ie ("log(3)")

output: 0<sub>n</sub><sup>i</sup>X   (unary conversion, ie ("000X")


2. convert back to base 10
 input: Y<sup>i</sup>0<sup>j</sup>X0<sup>k</sup>
 output i
 delete everything but iteration markers  (Y<sup>i</sup>) > 
 convert iteration markers to base 10 (Accept/Halt)



3. compare right to left side. 

  add iteration marker to the left end; ie (000X) -> (Y<sup>i</sup>000X)
  if 
  left side =< right side -> delete everything but iteration markers -> convert iteration markers to base 10 (Accept/Halt)
 
  else
  right side * 2
  compare right to left side. 
  
  
  
