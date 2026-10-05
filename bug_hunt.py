count = 1
total = 0

# BUG: The while line was missing a colon at the end (SyntaxError). I added ":" after the condition.
# BUG: The condition was count < 5, so the loop stopped before adding 5 and gave 10 instead of 15 (no error shown). I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Using + to join a string and an integer causes a TypeError. I wrapped total in str() so it can be joined to the text.
print("Sum of 1 to 5 is: " + str(total))