from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.datasets import ClassificationDataSet
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer
from pybrain.utilities import percentError

class MLPClassifier(object):
    def __init__(self):
        print "MLP"

    def trainClasifier(self, training_set):
        dataSet = self.__createDataset(training_set)

        hiddenNodesArg = 55
        learningRateArg = 0.004
        momentumArg = 0.99
        biasArg = True
        recurrentArg = True
        hiddenclassArg = SoftmaxLayer
        outclassArg = SoftmaxLayer
        epochs = 11

        self.__net = buildNetwork(
            dataSet.indim, hiddenNodesArg, dataSet.outdim,
            bias = biasArg ,recurrent = recurrentArg ,
            hiddenclass = hiddenclassArg , outclass = outclassArg)
        self.__trainer = BackpropTrainer(self.__net, dataSet,learningrate = learningRateArg, momentum = momentumArg, verbose = False)
        self.__trainer.trainUntilConvergence(continueEpochs=12, maxEpochs = epochs)

    def testClasifier(self, test_set):
        classes = ['negative', 'positive']
        test_data = self.__createDataset(test_set)
        positive_matches = 0.0
        for sample in test_set:
            result =  self.__net.activate(sample[0].values())
            rresult_class = classes[result.tolist().index(max(result))]

            if rresult_class == sample[1]:
                positive_matches += 1.0

        print "testClasifier, accuracy:" +  str(positive_matches/len(test_set))

    def check_class(self, features_map):
        print "Todo check_class"

    def __createDataset(self, training_set):
        training_map = training_set[0]
        # TODO should have number  of sentiment values instead of 2
        classes = ['negative', 'positive']
        data = ClassificationDataSet(len(training_map[0].keys()), nb_classes=2, class_labels = classes)
        for sample in training_set:
            new_items = [1.0 if x == True else -1.0 for x in sample[0].values()]
            data.addSample(sample[0].values(), classes.index(sample[1]))
        data._convertToOneOfMany([0,1])
        return data
