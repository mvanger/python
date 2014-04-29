# Bayesian Network
# Sari Nahmad, Anthony Tockar, Mike Vanger

import numpy as np

class BayesNetwork:

    '''
    1. Create, observe and change variables, including their names, possible values and marginal and
    conditional distributions as appropriate. For this assignment we will confine ourselves to discrete
    random variables exclusively.
    2. Add, observe and remove nodes to a Bayesian network
    3. Allow ways to create, observe and alter the structure of the network
    4. Save and load a Bayesian network from JSON
    5. Set and remove hard evidence on multiple variables
    6. Do inference on the network using variable elimination after setting evidence.
    '''

    def __init__(self, name = "NoName"):
        self.name = name
        self.nodes = []

    ## Create nodes class
    class Node():
        def __init__(self):
            self.probabilities = []
            self.evidence = {}

        #  Option to add values and possibly distribution probabilities separately
        def setProbDist(self, probabilities):
            self.probabilities = probabilities

        # Observe node
        def observe(self):
            print('Name:\t' + self.name)
            print('Values:\t' + str(self.values))           # Maybe make this a bit prettier
            print('Distribution:\t' + str(self.probabilities))
            print('Parents:\t' + str(self.parents))         # Change to for loop with names

        # Clear all evidence
        def clearEvidence(self):
            self.evidence = {}

        # Set evidence
        def setEvidence(self, value):
            self.evidence[self.name] = value

    # Method to add nodes
    def addNode(self, name, values, parents = []):
        node = self.Node()
        node.name = name
        node.values = values
        node.parents = parents
        ### CONSIDER ADDING SOME CHECKS - E.G. WHETHER NODE ALREADY EXISTS, WHETHER PROBABILITIES SUM TO 1
        self.nodes.append(node)
        print("New node \"" + node.name + "\" created")
        return node

    # Method to remove nodes
    def removeNode(self, node):
        self.nodes.remove(node)
        print("Node \"" + node.name + "\" removed")

    # Observe overall network structure
    def observeStructure(self):
        ### Will want to probably present this as a hierarchy - e.g. "level: nodeName"
        for node in self.nodes:
            print(node.name)

### Test functionality

bn = BayesNetwork()

## Create, observe and remove a node
ageNode = bn.addNode('Age', ['young','old'])
genderNode = bn.addNode('Gender',['M','F'])
smokerNode = bn.addNode('Smoker',['No','Light','Heavy'],[ageNode,genderNode])

ageNode.setProbDist([0.8, 0.2])
genderNode.setProbDist([0.49,0.51])
smokerNode.setProbDist([
[[0.8, 0.15, 0.05],[0.7,0.2,0.1]],
[[0.5, 0.2, 0.3],[0.5,0.25,0.25]],
])

#cancerNode = bn.addNode('Cancer', ['None','Benign','Malignant'])
#cancerNode.setProbDist([[0.96,0.88,0.6],[0.03,0.08,0.25],[0.01,0.04,0.15]])
#cancerdistribution = [0.935, 0.046, 0.019]

ageNode.observe()
genderNode.observe()
smokerNode.observe()
#cancerNode.observe()

tempNode = bn.addNode('Temp', ['A','B','C'])
bn.removeNode(tempNode)

ageNode.clearEvidence()
ageNode.setEvidence('young')