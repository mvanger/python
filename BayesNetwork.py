# Bayesian Network
# Sari Nahmad, Anthony Tockar, Mike Vanger

import itertools
import json
import pdb

class BayesNetwork:

    '''
    1. Create, observe and change discrete random variables, including their names, possible values and marginal and
    conditional distributions as appropriate
    2. Add, observe and remove nodes to a Bayesian network
    3. Allow ways to create, observe and alter the structure of the network
    4. Save and load a Bayesian network from JSON
    5. Set and remove hard evidence on multiple variables
    6. Do inference on the network using variable elimination after setting evidence.
    '''

    # Name network and initialize list holder for nodes
    def __init__(self, name = "NoName"):
        self.name = name
        self.nodes = []

    # Add nodes to Bayesian network
    def addNode(self, name, values, parents = []):
        ''' Usage: BayesNetwork.addNode(name, values, parents = [])
            Adds nodes to Bayesian network
            Input the name and possible states of the node, and the address of any parent nodes if they exist
            Example: smokerNode = bn.addNode('smoker', ['no','light','heavy'], [ageNode, genderNode])
        '''
        assert name not in self.nodes,  "%r is already the name of a node" % (name)  # make sure nodes have unique names
        if parents:
            for p in parents:
                assert p in self.nodes, "%r is not in network: add it first." % (p) # check if parents exist

        node = Node()
        node.name = name
        node.values = values
        node.parents = parents
        node.bn = self
        self.nodes.append(node)
        print("New node \"" + node.name + "\" created")
        return node

    # Get the node named
    def getNode(self, name):
        ''' Usage: BayesNetwork.getNode(name)
            Returns the node named
            Example: smokerNode2 = bn.getNode('smoker')
        '''
        nodeNames = [n.name for n in self.nodes]
        assert name in nodeNames, "%r is not an existing node." % (name) ##
        return self.nodes[nodeNames.index(name)]


    # Remove nodes from the Bayesian network
    def removeNode(self, node):
        ''' Usage: BayesNetwork.removeNode(node)
            Remove given node from the Bayesian network
            Example: bn.removeNode(smokerNode)
        '''
        assert node in self.nodes, "%r is not an existing node: can not be removed." % (node.name)
        self.nodes.remove(node)
        print("Node \"" + node.name + "\" removed")

    # Observe overall network structure
    def observeStructure(self):
        ''' Usage: BayesNetwork.observeStructure()
            Shows a text breakdown of the Bayesian Network structure
            Example: bn.observeStructure()
        '''
        print('Top level nodes:')
        for node in self.nodes:
            if not node.parents:
                print('Name: ' + node.name)
        print('')
        print('Child nodes:')
        for node in self.nodes:
            if node.parents:
                print('Name: ' + node.name + '\t\tParents = ' + str([p.name for p in node.parents]))
        print('')

    # Prepares a BayesNetwork object to be saved as JSON
    def jsonDefault(self, o):
        ''' Usage: BayesNetwork.saveJSON(filepath)
            jsonDefault takes care of the JSON encoding for a Bayesian Network, by turning it into a dict and
            setting the necessary values. The parameter "o" should be the Bayesian Network to be saved.
            It is called by the saveJSON method and does not need to be invoked by the user.
        '''
        t = o.__dict__.copy()
        temp = []
        # Gets the nodes ready for JSON
        # For some reason t['nodes'] does not work
        # So we are using t.keys()[0] as a workaround
        for x in t[t.keys()[0]]:
            temp.append(x.readyForJSON())
        t['nodes'] = temp
        jsonObject = {}
        jsonObject['network'] = t
        return jsonObject

    def saveJSON(self, filepath):
        ''' Usage: BayesNetwork.saveJSON(filepath)
            This method is called on a BN with a filepath, and the BN is saved in JSON format.
            Example: bn.saveJSON('bn.json')
        '''
        with open(filepath, 'w') as outfile:
             json.dump(self.jsonDefault(self), outfile, indent = 4, sort_keys=True)

# Method to calculate each term in variable elimination algorithm
def sumProduct(factor, nodes):
    ''' Usage: sumProduct(factor, nodes)
        Calculates each term in variable elimination algorithm
        See: http://www.youtube.com/watch?v=FDNB0A61PGE
        Example: factor[i+1] = sumProduct(factor[i],nodesInTerm)
    '''
    if len(nodes) == 1:
        return factor
    else:
        for n in nodes:
            if n.evidence:
                post = []

                # Flatten probability matrix to access elements
                toFlatten = [x for x in n.prob]
                while True:
                    if not isinstance(toFlatten[0],list):
                        break
                    else:
                        toFlatten = list(itertools.chain(*toFlatten))

                # Calculate posterior probability distribution given the evidence
                for i in range(0,len(n.values)):
                    if n.evidence[i] != 0:
                        nValues = []
                        for p in n.parents:
                            nValues.append(len(p.values))
                        product = 1
                        for j in nValues:
                            product = product * j
                        for k in range(0,product):
                            post.append(toFlatten[k*int(len(toFlatten)/product) + i])
            else:
                cond = n.prob

        # Sum dot product of (conditional and/or posterior) probabilities
        sumProd = []
        for j in range(0,(int(len(post)/len(cond)))):
            sumTerm = 0
            for c in range(0,len(cond)):
                sumTerm = sumTerm + cond[c]*post[(c*2)+j]
            sumProd.append(sumTerm)

        # Multiply each element of factor by corresponding element in above sum-product
        fXs = []
        for i in range(0,len(factor)):
            fXs.append(factor[i]*sumProd[i])
        return fXs

# Method to normalize the belief so it sums to 1
def normalize(beliefUnNorm):
    ''' Usage: normalize(beliefUnNorm)
        Normalizes belief probabilities so they sum to 1
        Example: belief = normalize(beliefUnNorm)
    '''
    sumBeliefs = 0
    for b in beliefUnNorm:
        sumBeliefs = sumBeliefs + b
    belief = [b/sumBeliefs for b in beliefUnNorm]
    return belief

def loadJSON(filepath):
    ''' Usage: loadJSON(filepath)
        This method loads a JSON file and turns the JSON data into a new BN with nodes.
        Example: net = loadJSON('bn.json')
    '''
    # Opens the json file and reads the data
    json_data = open(filepath).read()
    # Instantiates a new BN object
    new_object = BayesNetwork()
    t = json.loads(json_data)['network']
    # Sets the BN name, and makes it a str
    new_object.name = t['name'].encode('ascii')
    # This stores each node
    temp = []
    # Creates and adds the nodes
    for x in t['nodes']:
        A = new_object.addNode(x['name'], x['values'], parents = [])
        # Sets the node name as a str
        A.name = A.name.encode('ascii')
        # Sets the node's values as str
        for y in range(0, len(A.values)):
            A.values[y] = A.values[y].encode('ascii')
        # Since the JSON file only has the name of the parent nodes, we need to loop through our temp
        # list to find the correct parents.
        for z in temp:
            if z.name in x['parents']:
                A.parents.append(z)
        # Sets the CPT and the evidence
        A.setProbDist(x['prob'])
        A.setEvidence(x['evidence'])
        temp.append(A)
    return new_object

## Create nodes class
class Node:
    '''
    A class with methods to define each node in a Bayesian Network
    Should be instantiated by the addNode method in the BayesNetwork class
    '''

    # Initialize node properties that will be added later
    def __init__(self):
        self.prob = []
        self.evidence = []

    #  Set conditional probability distribution for given node
    def setProbDist(self, probabilities):
        ''' Usage: node.setProbDist(probabilities)
            Sets the conditional (or prior, if there are no parents) probability
            distribution for the node. Also performs some checks to ensure
            probabilities are input correctly.
            Example: smokerNode.setProbDist([
                                            [[0.8, 0.15, 0.05],[0.7,0.2,0.1]],
                                            [[0.5, 0.2, 0.3],[0.5,0.25,0.25]],
                                            ])
        '''
        # Check array probabilities sum to 1 and that input has the correct dimensions
        if not self.parents:
            assert sum(probabilities) == 1, "Please ensure probabilities sum to 1"
            assert len(probabilities) == len(self.values), "Please include a probability for each possible state in the node"
        else:
            parentLengths = [len(p.values) for p in self.parents]
            product = 1
            for p in parentLengths:
                product = product * p

            #Flatten probability matrix to access elements
                toFlatten = [x for x in probabilities]
                while True:
                    if not isinstance(toFlatten[0],list):
                        break
                    else:
                        toFlatten = list(itertools.chain(*toFlatten))

            # Sum all probabilities, divide by product of number of values of parents
            sumProbs = 0
            for f in toFlatten:
                sumProbs = sumProbs + f
            epsilon = 0.00001
            assert (sumProbs / product) < 1 + epsilon, "Please ensure all conditional probability possibilities sum to 1"
            assert (sumProbs / product) > 1 - epsilon, "Please ensure all conditional probability possibilities sum to 1"

            # Check number of probabilities is equal to product * (number of node values)
            assert len(toFlatten) == (product * len(self.values)), "Please include a probability for each possible state in the node"

        self.prob = probabilities

    # Observe node
    def observe(self):
        ''' Usage: node.observe()
            Provides a full breakdown of a given node's properties
            Example: smokerNode.observe()
        '''
        print('Bayes Network:\t' + self.bn.name)
        print('Name:\t' + self.name)
        print('States:\t' + str(self.values))
        print('Distribution:\t' + str(self.prob))
        if self.evidence:   # Only show if evidence exists
            print('Evidence:\t' + str(self.evidence))
        print('Parents:\t',end='')
        print([p.name for p in self.parents])

    # Clear all evidence
    def clearEvidence(self):
        ''' Usage: node.clearEvidence()
            Clears all evidence previously attributed to the given node
            Does not affect the evidence set on other nodes
            Example: smokerNode.clearEvidence()
        '''
        self.evidence = []
        print('Evidence cleared for node ' + self.name)

    # Set evidence
    def setEvidence(self, value):
        ''' Usage: node.setEvidence(value)
            Sets hard evidence on given node. This can then be used to form a belief on the probability
            of another node occurring (see Node.getBelief())
            Example: smokerNode.setEvidence('Light')
        '''
        assert value in self.values, "%r is not a possible state for %r " % (value, self.name)
        for i in range(0,len(self.values)):
            if self.values[i] == value:
                self.evidence.append(1)
            else: self.evidence.append(0)
        print('Evidence set for ' + self.name)

    # Get belief
    def getBelief(self):
        ''' Usage: node.getBelief()
            Uses variable elimination algorithm to find the belief (i.e. posterior probability distribution)
            for a given node, given all available evidence in the Bayesian Network
            Example: ageNode.getBelief()
        '''

        # Find all nodes with evidence
        nodesRemaining = [x for x in self.bn.nodes]

        # Create array with nodes that have evidence
        evidenceNodes = []
        for node in self.bn.nodes:
            if node.evidence:
                evidenceNodes.append(node)

        # Create array with nodes to eliminate
        eliminateNodes = []
        for node in nodesRemaining:
            if node != self and node not in evidenceNodes:
                eliminateNodes.append(node)

        # Create factors iteratively
        factor = [dict()] * (len(eliminateNodes) + 1)
        factor[0] = {'Node': self.name, 'Prob': self.prob}
        for i in range(0,len(eliminateNodes)):
            termNodes = []
            for node in nodesRemaining:
                if eliminateNodes[i] == node or eliminateNodes[i] in node.parents:   # Get node and children
                    termNodes.append(node)
            factor[i+1]['Node'] = eliminateNodes[i].name
            factor[i+1]['Prob'] = sumProduct(factor[i]['Prob'],termNodes)

            nodesRemaining.remove(eliminateNodes[i])

        beliefUnNorm = factor[len(eliminateNodes)]['Prob']

        # Normalize belief
        belief = normalize(beliefUnNorm)

        return belief

    def readyForJSON(self):
        t = self.__dict__.copy()
        t['bn'] = t['bn'].name
        t['parents'] = [x.name for x in t['parents']]
        return t

    # def jsonDefault(self, obj):
    #     t = obj.__dict__.copy()
    #     t['bn'] = t['bn'].name
    #     return t

    # def saveJSON(self, filepath):
    #     with open(filepath, 'w') as outfile:
    #          json.dump(self, outfile, default=self.jsonDefault, indent = 4, sort_keys=True)


### Test functionality

# net = BayesNetwork("Jorge's sample net")
# A = net.addNode('A',['a1','a2'])
# C = net.addNode('C',['c1','c2','c3','c4'])
# B = net.addNode('B',['b1','b2','b3'],[A,C])

# # net.observeStructure()

# A.setProbDist([0.9,0.1])
# C.setProbDist([0.1,0.2,0.3,0.4])
# B.setProbDist([
#            [ [0.2,0.4,0.4] , [0.33,0.33,0.34 ] ] ,
#            [ [0.1,0.5,0.4] , [0.3,0.1,0.6 ] ] ,
#            [ [0.01,0.01,0.98] , [0.2,0.7,0.1 ] ] ,
#            [ [0.2,0.1,0.7] , [0.9,0.05,0.05 ] ]
#          ])

# B.setEvidence('b3')

# B.observe()

# aAfterSettingB = A.getBelief()
# print("P(A|B=b3) =",aAfterSettingB)

# C.setEvidence('c4')

# aAfterSettingBC = A.getBelief();
# print("P(A|B=b3,C=c4) =",aAfterSettingBC)

# B.clearEvidence()

# aAfterSettingC = A.getBelief();
# print("P(A|C=c4) =",aAfterSettingC)


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

# cancerNode = bn.addNode('Cancer', ['None','Benign','Malignant'],[smokerNode])
# cancerNode.setProbDist([[0.96,0.88,0.6],[0.03,0.08,0.25],[0.01,0.04,0.15]])

smokerNode.setEvidence('Light')
print("P(Age|Smoker = 'Light') = " + str(ageNode.getBelief()))

# ageNode.observe()
# genderNode.observe()
# smokerNode.observe()
# cancerNode.observe()

# tempNode = bn.addNode('Temp', ['A','B','C'])
# bn.removeNode(tempNode)

# smokerNode.clearEvidence()
# smokerNode.observe()
# ageNode.setEvidence('old')
# ageNode.observe()