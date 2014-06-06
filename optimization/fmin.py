from derivative import derivative

def fmin(f, bounds, g = None, eps = 1.e-8):
  if not g:
    f_prime = derivative(f)
  else:
    f_prime = g(f)
  width = abs(bounds[0]-bounds[1])/max(1,abs(bounds[0]))
  while width > eps:
    split = bounds[0] + width/2
    if f_prime(split) == 0:
      return split
    elif f_prime(split) > 0:
      bounds = (bounds[0], split)
    else:
      bounds = (split, bounds[1])
    width = abs(bounds[0]-bounds[1])/max(1,abs(bounds[0]))
  return split

def first(x):
  return x**2

def second(x):
  return -(x**(1/x))

# Unexpected behavior based on the starting bounds...
test = fmin(second,(1,3))
print(test)