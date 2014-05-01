# Bayesian Network
# Sari Nahmad, Anthony Tockar, Mike Vanger

import itertools
import json
import pdb

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

    # Method to add nodes
    def addNode(self, name, values, parents = []):
        node = Node()
        node.name = name
        node.values = values
        node.parents = parents
        node.bn = self
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

    '''
    jsonDefault takes care of the JSON encoding for a Bayesian Network, by turning it into a dict and
    setting the necessary values. The parameter "o" should be the Bayesian Network to be saved.
    '''
    def jsonDefault(self, o):
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

    '''
    This method is called on a BN with a filepath, and the BN is saved in JSON format.
    '''
    def saveJSON(self, filepath):
        with open(filepath, 'w') as outfile:
             json.dump(self.jsonDefault(self), outfile, indent = 4, sort_keys=True)

# Method to calculate each term in variable elimination algorithm
def sumProduct(factor, nodes):
    if len(nodes) == 1:
        return factor
    else:
        # First iteration - just want to sum term-probabilities over Gender
        for n in nodes:
            if n.evidence:
                post = []

                #Flatten probability matrix to access elements
                toFlatten = [x for x in n.prob]
                while True:
                    if not isinstance(toFlatten[0],list):
                        break
                    else:
                        toFlatten = list(itertools.chain(*toFlatten))
                print(toFlatten)

                for i in range(0,len(n.values)):
                    if n.evidence[i] != 0:
                        nValues = []
                        for p in n.parents:
                            nValues.append(len(p.values))
                        print('nValues = ' + str(nValues))
                        product = 1
                        for j in nValues:
                            product = product * j
                        for k in range(0,product):
                            print(k*int(len(toFlatten)/product) + i)
                            post.append(toFlatten[k*int(len(toFlatten)/product) + i])
                print('Post = ' + str(post))    # Debug
            else:
                cond = n.prob
                print('Cond = ' + str(cond))    # Debug

        sumProd = []
        for j in range(0,(int(len(post)/len(cond)))):
            sumTerm = 0
            for c in range(0,len(cond)):
                sumTerm = sumTerm + cond[c]*post[(c*2)+j]
            sumProd.append(sumTerm)

        print('SumProd = ' + str(sumProd))    # Debug
        print('Factor = ' + str(factor))      # Debug

        fXs = []
        for i in range(0,len(factor)):
            fXs.append(factor[i]*sumProd[i])

        return fXs

# def object_decoder(obj):
#     new_object = BayesNetwork()
#     new_object.name = obj['network']['name']
#     new_object.values = obj['values']
#     return new_object

'''
This method loads a JSON file and turns the JSON into a new BN.
'''
def loadJSON(filepath):
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
    Hi
    '''

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
        if self.belief:
            print('Belief:\t' + str(self.belief))       # Only show if belief exists
        # print('Parents:\t',end='')
        print([p.name for p in self.parents])         # Change to for loop with names

    # Clear all evidence
    def clearEvidence(self):
        self.evidence = []
        self.belief = []
        print('Evidence cleared')

    # Set evidence
    def setEvidence(self, value):
        for i in range(0,len(self.values)):
            if self.values[i] == value:
                self.evidence.append(1)
            else: self.evidence.append(0)

    # Get belief
    def getBelief(self):
        # Calculate all beliefs in network given the evidence at hand

        # Find all nodes with evidence
        nodesRemaining = [x for x in self.bn.nodes]

        # Create array with nodes that have evidence
        evidenceNodes = []
        for node in self.bn.nodes:
            if node.evidence:
                evidenceNodes.append(node)
        # print('Evidence = ',end='')
        print([node.name for node in evidenceNodes])

        # Create array with nodes to eliminate
        eliminateNodes = []
        # print('Nodes Remaining = ',end='')
        print([node.name for node in nodesRemaining])
        for node in nodesRemaining:
            if node != self and node not in evidenceNodes:
                eliminateNodes.append(node)
        # print('Eliminate = ',end='')
        print([node.name for node in eliminateNodes])

        # Create factors iteratively
        factor = [dict()] * (len(eliminateNodes) + 1)
        factor[0] = {'Node': self.name, 'Prob': self.prob}
        for i in range(0,len(eliminateNodes)):
            termNodes = []
            for node in nodesRemaining:
                if eliminateNodes[i] == node or eliminateNodes[i] in node.parents:   # Get node and children
                    termNodes.append(node)
            factor[i+1]['Node'] = eliminateNodes[i].name
            ####### Debug
            # print('term names = ',end='')
            print([n.name for n in termNodes])
            # print('term probabilities = ',end='')
            print([n.prob for n in termNodes])
            # print('term evidence = ',end='')
            print([n.evidence for n in termNodes])
            #############
            factor[i+1]['Prob'] = sumProduct(factor[i]['Prob'],termNodes)

            nodesRemaining.remove(eliminateNodes[i])

        belief = factor[len(eliminateNodes)]['Prob']
        # Remember to normalise
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

net = BayesNetwork("Jorge's sample net")
A = net.addNode('A',['a1','a2'])
C = net.addNode('C',['c1','c2','c3','c4'])
B = net.addNode('B',['b1','b2','b3'],[A,C])

A.setProbDist([0.9,0.1])
C.setProbDist([0.1,0.2,0.3,0.4])
B.setProbDist([
           [ [0.2,0.4,0.4] , [0.33,0.33,0.34 ] ] ,
           [ [0.1,0.5,0.4] , [0.3,0.1,0.6 ] ] ,
           [ [0.01,0.01,0.98] , [0.2,0.7,0.1 ] ] ,
           [ [0.2,0.1,0.7] , [0.9,0.05,0.05 ] ]
         ])

B.setEvidence('b3')

B.observe()

# aAfterSettingB = A.getBelief()
# print("P(A|B=b3) =",aAfterSettingB)

C.setEvidence('c4')

# aAfterSettingBC = A.getBelief();
# print("P(A|B=b3,C=c4) =",aAfterSettingBC)

# >>> P(A|B=b3,C=c4) = [ 0.9921, 0.0079 ]
# This value is also correct!

# Finally. What if I clear the evidence on node B.
# What is the distribution of A now?

B.clearEvidence()

# aAfterSettingC = A.getBelief();
# print("P(A|C=c4) =",aAfterSettingC)

# net.saveJSON('test.json')
bn2 = loadJSON('test.json')
bn2.saveJSON('test2.json')
# pdb.set_trace()

# bn = BayesNetwork('BN1')

# ## Create, observe and remove a node
# ageNode = bn.addNode('Age', ['young','old'])
# genderNode = bn.addNode('Gender',['M','F'])
# smokerNode = bn.addNode('Smoker',['No','Light','Heavy'],[ageNode,genderNode])

# ageNode.setProbDist([0.8, 0.2])
# genderNode.setProbDist([0.49,0.51])
# smokerNode.setProbDist([
# [[0.8, 0.15, 0.05],[0.7,0.2,0.1]],
# [[0.5, 0.2, 0.3],[0.5,0.25,0.25]],
# ])

# cancerNode = bn.addNode('Cancer', ['None','Benign','Malignant'],[smokerNode])
# cancerNode.setProbDist([[0.96,0.88,0.6],[0.03,0.08,0.25],[0.01,0.04,0.15]])
# # cancerdistribution = [0.935, 0.046, 0.019]

# ageNode.observe()
# genderNode.observe()
# smokerNode.observe()
# cancerNode.observe()

# tempNode = bn.addNode('Temp', ['A','B','C'])
# bn.removeNode(tempNode)

# smokerNode.setEvidence('Light')
# print(ageNode.getBelief())

# smokerNode.clearEvidence()
# smokerNode.observe()
# ageNode.setEvidence('old')
# ageNode.observe()
