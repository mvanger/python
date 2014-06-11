# This function takes as argument f, a function.
# It computes the derivative and returns it as a function using closures.
# More precisely, parameter f of derivative is a function that takes a number x as its input and also returns a number.
# The function g that derivative returns has the same signature as f: It also takes a number x as its input, and also returns a number.
# The value that function g returns for a given input x is the derivative of f evaluated at x.
def derivative(f):
  def g(x):
    delta = max(abs(x),1)*1.e-9
    return (f(x+delta)-f(x-delta))/(2*delta)
  return g