from example import *
import json
import pdb

# Make a new object
test = Example()
# Add nodes and values
test.add_nodes(1)
test.add_nodes(2)
test.add_nodes(3)
test.add_values(10)
test.add_values(20)
test.add_values(30)

print(test)
print(test.nodes)
print(test.values)

# Save to json
# test.__dict__ makes it a dict to save as json
with open('data.json', 'w') as outfile:
  json.dump(test.__dict__, outfile, indent = 4, sort_keys=True)

# Define a method to take JSON data and turn it into an Example object
def object_decoder(obj):
  new_object = Example()
  new_object.nodes = obj['nodes']
  new_object.values = obj['values']
  pdb.set_trace()
  return new_object

# Opens json file
json_data = open('data.json').read()
# Takes open file and turns it into a new Example object
new_test = json.loads(json_data, object_hook = object_decoder)

print(new_test)
print(new_test.nodes)
print(new_test.values)