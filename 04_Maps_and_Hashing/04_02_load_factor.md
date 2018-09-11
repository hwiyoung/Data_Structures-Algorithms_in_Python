# Load Factor
## Question
### 1 - What is the load factor?
* You have a hash fuction that divides a group of value by 100, and uses the remainder as a key
* The values are 100 numbers that are all multiples of 5.

### 2 - What number would you recommend his fuction to divide by rather than 100 to speed it up?
* (1) 87 | (2) 107 | (3) 125 | (4) 1001

## Answer
### 1 - What is the load factor?
* For the load factor, you should divide the number of values by the number of buckets.
* There are 100 values, as stated in the question, and 100 buckets (0 to 99).
* Thus, <u>**100/100 = 1**</u>

### 2 - What number would you recommend his fuction to divide by rather than 100 to speed it up?
* The answer to the second part is 107. The other values all had something wrong with them:
* 125 is also a multiple of 5. Dividing a bunch of multiples of 5 by another multiple of 5 will cause a lot of collisions.
* Here's an example, where 10 is used as the divisor:
  * 5 % 10 = 5
  * 10 % 10 = 0
  * 15 % 10 = 5
  * 20 % 10 = 0
* 87 is better than 125, but because it's less than 100 it'll still have collisions.
* 1001 is good, but it'll create a ton of leftover buckets and waste a lot of memory.