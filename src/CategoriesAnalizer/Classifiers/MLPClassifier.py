from pybrain3.datasets import ClassificationDataSet
from pybrain3.supervised import BackpropTrainer
from pybrain3.tools.shortcuts import buildNetwork

from src.CategoriesAnalizer.Classifiers.BaseClassifier import BaseClassifier


class MLPClassifier(BaseClassifier):
    def __init__(self, configuration_map):
        super(MLPClassifier, self).__init__(configuration_map)

    def trainClasifier(self, training_set):
        dataSet = self.__createDataset(training_set)
        mpl_conf = self.configuration_map['mlp_classifier_config']

        self.__net = buildNetwork(
            dataSet.indim, mpl_conf['hidden_nodes'], dataSet.outdim,
            bias = mpl_conf['biasArg'] ,recurrent = mpl_conf['recurrentArg'] ,
            hiddenclass = mpl_conf['hiddenclassArg'] , outclass = mpl_conf['outclassArg'])

        self.__trainer = BackpropTrainer(
            self.__net, dataSet, learningrate = mpl_conf['learningRateArg'],
            momentum = mpl_conf['momentumArg'],verbose = mpl_conf['verbose'])

        self.__trainer.trainUntilConvergence(continueEpochs=12, maxEpochs = mpl_conf['epochs'])

    def testClasifier(self, test_set):
        classes = ['negative', 'positive']
        test_data = self.__createDataset(test_set)
        positive_matches = 0.0
        for sample in test_set:
            result =  self.__net.activate(sample[0].values())
            rresult_class = classes[result.tolist().index(max(result))]

            if rresult_class == sample[1]:
                positive_matches += 1.0

        accuracy = positive_matches/len(test_set)
        print("testClasifier, accuracy:" + str(accuracy))
        return accuracy

    def check_class(self, features_map):
        print("Todo check_class")

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
