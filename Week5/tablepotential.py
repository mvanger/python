import numpy as np

class TablePotential:
  def __init__(self, dim, table, index = None):
    if (index != None):
      self.table = np.zeros(table)
      self.table[index] = 1
    else:
      self.table = np.array(table)
    self.dim = dim

def doInference(potentials):
  dims = [i.dim for i in potentials]
  pots = [i.table for i in potentials]
  einsumFormat = ','.join(dims)
  vars = sorted(list(set(''.join(dims))))

  for v in vars:
    vMarginal = np.einsum(einsumFormat + '->' + v, *pots)
    vMarginal = vMarginal/np.sum(vMarginal)
    print("{} -> {}".format(v, vMarginal))

  varsString = ''.join(vars)
  joint = np.einsum(einsumFormat + '->' + varsString, *pots)
  # normalize
  joint = joint/np.sum(joint)
  # print
  print("{} -> {}".format(varsString, joint))

###
# Using example from blackboard