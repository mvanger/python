def derivative(f):
  def g(x):
    delta = max(abs(x),1)*1.e-9
    return (f(x+delta)-f(x-delta))/(2*delta)
  return g