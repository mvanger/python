def remainder(a,b):
  q = a//b # // is truncating division
  r = a - q*b
  return r # return statement returns computed values
  # use a tuple to return multiple values

test = remainder(43,27)

print(test)

# You can give default values to parameters
def connect(hostname, port, timeout=300):
  # Function body
  return 0

# connect('www.python.org', 80) is equivalent to connect('www.python.org', 80, 300)
# You can call the parameters in any order
# connect(port=80, hostname='www.python.org')