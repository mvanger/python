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

    def __init__(self):
        self.nodes = []
        self.evidence = {}

    ## Create nodes class
    class node():
        def __init__(self, name, values = [], prior = []):
            self.name = name
            self.values = values
            self.prior = prior
            self.parents = []
            self.children = []

        #  Option to add values and possibly prior probabilities separately
        def addValues(self, values, prior = []):
            self.values = values
            self.prior = prior

        # Observe node
        def observe(self):
            print('Name:\t' + self.name)
            print('Values:\t' + str(self.values))           # Maybe make this a bit prettier
            print('Prior distribution:\t' + str(self.prior))
            print('Parents:\t' + str(self.parents))         # Change to for loop with names
            print('Children:\t' + str(self.children))       # Change to for loop with names

    # Method to add nodes
    def addNode(self, node):
        ### CONSIDER ADDING SOME CHECKS - E.G. WHETHER NODE ALREADY EXISTS, WHETHER PROBABILITIES SUM TO 1
        self.nodes.append(node)
        print("New node \"" + node.name + "\" created")

    # Method to remove nodes
    def removeNode(self, node):
        self.nodes.remove(node)
        print("Node \"" + node.name + "\" removed")

    # Create links - parents and children
    def linkNodes(self, parent, child, joint = [], posterior = []):
        '''
        Specify joint or posterior probabilities
        '''
        parent.children.append(child)
        child.parents.append(parent)
        # Possibly create a new link object here which contains joint and posterior probabilities

    # Observe overall network structure
    def observeStructure(self):
        ### Will want to probably present this as a hierarchy - e.g. "level: nodeName"
        for node in self.nodes:
            print(node.name)

    # Clear all evidence
    def clearEvidence(self):
        self.evidence = {}

    # Set evidence
    def setEvidence(self, node, value):
        self.evidence[node.name] = value

### Test functionality

bn = BayesNetwork()

## Create, observe and remove a node
ageNode = bn.node('Age', ['young','old'], [0.8, 0.2])
bn.addNode(ageNode)

genderNode = bn.node('Gender')
bn.addNode(genderNode)
genderNode.addValues(['M','F'],[0.49,0.51])

smokerNode = bn.node('Smoker',{'No': 0.8, 'Light': 0.15, 'Heavy': 0.05})

bn.linkNodes(ageNode, smokerNode)
bn.linkNodes(genderNode, smokerNode)

#cancerPrior = [0.935, 0.046, 0.019]
cancerNode = bn.node('Cancer', ['None','Benign','Malignant'])
bn.addNode(cancerNode)

cancerGvnSmoker = [[0.96,0.88,0.6],[0.03,0.08,0.25],[0.01,0.04,0.15]]
bn.linkNodes(smokerNode, cancerNode, posterior = cancerGvnSmoker)

genderNode.observe()
cancerNode.observe()
smokerNode.observe()

tempNode = bn.node('Temp', ['A','B','C'])
bn.addNode(tempNode)
bn.removeNode(tempNode)

bn.clearEvidence()
bn.setEvidence(ageNode,'young')
