def fact_rec(n):
  if n == 0 or n == 1:
    return 1  # Fix the base cases: return 1 instead of 0 for factorial
  else:
    return n * fact_rec(n - 1)


number = 2
res = fact_rec(number)
print("the factorial of {} is {}".format(number, res))
