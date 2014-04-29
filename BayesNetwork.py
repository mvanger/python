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
    class Node:

        def __init__(self):
            self.prob = []
            self.evidence = []
            self.belief = []

        #  Option to add values and possibly distribution probabilities separately
        def setProbDist(self, probabilities = []):
            # Check each array adds to 1
            # Check input has the correct dimensions
            self.prob = probabilities

        # Observe node
        def observe(self):
            print('Name:\t' + self.name)
            print('Values:\t' + str(self.values))           # Maybe make this a bit prettier
            print('Distribution:\t' + str(self.prob))
            if self.evidence:
                print('Evidence:\t' + str(self.evidence))       # Only show if evidence exists
            if self.belief
                print('Belief:\t' + str(self.belief))       # Only show if belief exists
            print('Parents:\t' + str(self.parents))         # Change to for loop with names

        # Clear all evidence
        def clearEvidence(self):
            self.evidence = []
            print('Evidence cleared')

        # Set evidence
        def setEvidence(self, value):
            for i in range(0,len(self.values)):
                if self.values[i] == value:
                    self.evidence.append(1)
                else: self.evidence.append(0)

        # Get belief
        def getBelief(self, value):
            if self.belief:
                print('P(Some|shit) = ' + str(self.belief))
                return self.belief
            else:
                print('P(Some other shit) = ' + str(self.prob))
                return self.prob

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

    # Calculate belief - would be good if this can be executed along with setEvidence
    def calcBelief(self):
        # Calculate all beliefs in network given the evidence at hand

        # Find all nodes with evidence
        evidenceNodes = []
        for node in self.nodes:
            if node.evidence:
                evidenceNodes.append(node)

        # Do some hardcore formula to pull out the probabilities and evidence and infer the belief

### Test functionality

bn = BayesNetwork('BN1')

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

# cancerNode = bn.addNode('Cancer', ['None','Benign','Malignant'])
# cancerNode.setProbDist([[0.96,0.88,0.6],[0.03,0.08,0.25],[0.01,0.04,0.15]])
# cancerdistribution = [0.935, 0.046, 0.019]

ageNode.observe()
genderNode.observe()
smokerNode.observe()
# cancerNode.observe()

tempNode = bn.addNode('Temp', ['A','B','C'])
bn.removeNode(tempNode)

ageNode.setEvidence('young')
ageNode.observe()
ageNode.clearEvidence()
ageNode.observe()
ageNode.setEvidence('old')
ageNode.observe()
calcBelief()
