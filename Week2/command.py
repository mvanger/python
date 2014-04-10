# Load the sys module
import sys

# sys.argv is a list containing command line arguments
# sys.argv[0] is the module name

if len(sys.argv) != 2:
  print("Please supply a filename")
  raise SystemExit(1)

# get filename from the command line
f = open(sys.argv[1])

# Convert each line (string) to a number
# Notice the list comprehension!
fvalues = [float(line) for line in f]
f.close()

# Print min and max values
print("The minimum value is", min(fvalues))
print("The maximum value is", max(fvalues))