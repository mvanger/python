from derivative import derivative

# fmin computes the local minimum of a function f given an interval (bounds).
# It takes optional parameters g and eps
# g is a function that returns the derivative of f.
# If g is not supplied, fmin defaults to the derivative function defined earlier
# eps is the error bound. The default is 1.e-8
# fmin returns a number x such that f(x) is a local minimum
# fmin sometimes demonstrates unexpected behavior and can be sensitive to the initial interval in Python 2.x
# Sometimes it exhibits long runtimes or returns an incorrect minimum
# If this seems to be the case, try subtly changing the initial interval or using Python 3.x
def fmin(f, bounds, g = None, eps = 1.e-8):
  # Compute f_prime
  if not g:
    f_prime = derivative(f)
  else:
    f_prime = g(f)
  # Set the width of the interval
  width = abs(bounds[0]-bounds[1])/max(1,abs(bounds[0]))
  # Loop the algorithm
  while width > eps:
    # Calculate a split
    split = bounds[0] + width/2
    # Check the slope at the split and compute the new interval
    if f_prime(split) == 0:
      return split
    elif f_prime(split) > 0:
      bounds = (bounds[0], split)
    else:
      bounds = (split, bounds[1])
    # Set the resulting width
    width = abs(bounds[0]-bounds[1])/max(1,abs(bounds[0]))
  return split

###
# Some test functions
# def first(x):
#   return x**2

# def second(x):
#   return -(x**(1/x))

# # Unexpected behavior based on the starting bounds in Python 2.x...
# test = fmin(second,(1,3))
# print(test) # returns 2 (incorrect)
# test = fmin(second,(1,3.1))
# print(test) # returns 2.71828161379 (correct)

