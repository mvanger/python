from derivative import derivative

# fsolve computes the zero of a function
# fsolve takes a function f, an initial guess x0, and optional parameters g, eps, and max_iter
# g should be a function that computes the derivative. If none is supplied it uses the derivative created earlier
# eps is the error bound. The default is 1.e-8
# max_iter is the maximum number of iterations for the approximation. The default is 100
# fsolve returns a number x such that f(x) is approximately equal to 0
def fsolve(f, x0, g = None, eps = 1.e-8, max_iter = 100):
  for i in range(max_iter):
    # Compute y
    y = f(x0)
    # Compute f_prime
    if not g:
      f_prime = derivative(f)
    else:
      f_prime = g(f)
    # Compute f_prime(x0)
    y_prime = f_prime(x0)
    # Check error bound
    if (abs(y_prime)) < eps:
      break
    # Set x0 to new value
    x0 = x0 - y/y_prime
  return x0