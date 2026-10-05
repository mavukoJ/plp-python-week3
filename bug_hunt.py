count = 1
total = 0

# BUG: The while statement was missing a colon (:).
# Added the colon so Python can recognize the while-loop block.
while count <= 5:
    total = total + count

    # BUG: The original program increased count after adding,
    # but its condition stopped at 4. Changed the condition to <= 5
    # so that 5 is also included in the calculation.
    count = count + 1

# BUG: total is an integer, so it cannot be joined directly
# to a string with +. Converted total to a string using str().
print("Sum of 1 to 5 is: " + str(total))