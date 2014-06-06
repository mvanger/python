from derivative import derivative

def fsolve(f, x0, g = None, eps = 1.e-8, max_iter = 100):
  for i in range(max_iter):
    y = f(x0)
    if not g:
      f_prime = derivative(f)
    else:
      f_prime = g(f)
    y_prime = f_prime(x0)
    if (abs(y_prime)) < eps:
      break
    x0 = x0 - y/y_prime
  return x0