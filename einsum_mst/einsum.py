import numpy as np
from collections import OrderedDict

# This is the combo function from class
def combo(n):
  r = [0] * len(n)
  while True:
    yield tuple(r)
    p = len(r) - 1
    r[p] += 1
    while r[p] == n[p]:
      r[p] = 0
      p -= 1
      if p == -1:
        return
      r[p] += 1

# This is our einsum function
def my_einsum(subscripts, *operands):
  # Splits the left and right sides of the subscript
  split_subscripts = subscripts.split('->')
  # Splits the left side for each matrix
  left_strings = split_subscripts[0].split(',')
  # Concatenates all the letters of the left side
  all_letters = split_subscripts[0].replace(',', '')

  # Matches each unique letter with the matrix dimension
  matched = match_letters(all_letters, *operands)
  # Runs the combo function for those dimensions
  g = combo(matched.values())
  # Instantiates a numpy array of the correct size
  output = np.zeros(shape=tuple([matched[x] for x in split_subscripts[1]]))

  # Gets the tuple index for the output matrix
  output_index = get_tuple_index(all_letters, split_subscripts[1])

  # Loops through combos
  for t in g:
    tmp = 1.
    for index, array in enumerate(operands):
      # Get the array value and multiply them together
      array_index = get_tuple_index(all_letters, left_strings[index])
      array_tuple_index = tuple([t[x] for x in array_index])
      tmp *= array[array_tuple_index]
    # Set the correct value for the output matrix
    output_tuple_index = tuple([t[x] for x in output_index])
    output[output_tuple_index] += tmp
  return output

# This method matches the subscripts with the matrix dimensions
def match_letters(input_str, *arrays):
  match = OrderedDict()
  counter = 0
  for j in arrays:
    for k in j.shape:
      match[input_str[counter]] = k
      counter += 1
  return match

# This method gets the tuple index for a matrix
def get_tuple_index(distinct_input_str, substring):
  distinct_letters = ''.join(OrderedDict.fromkeys(distinct_input_str).keys())
  tuple_index = [distinct_letters.index(x) for x in substring]
  return tuple(tuple_index)

###
# Tests #
###

a = np.arange(60.).reshape(3,4,5)
b = np.arange(24.).reshape(4,3,2)
print np.einsum('ijk,jil->kl', a, b)
print my_einsum('ijk,jil->kl', a, b)

a = np.arange(25).reshape(5,5)
b = np.arange(5)

print np.einsum('ij,j->i', a, b)
print my_einsum('ij,j->i', a, b)

print np.einsum('ii->i', a)
print my_einsum('ii->i', a)