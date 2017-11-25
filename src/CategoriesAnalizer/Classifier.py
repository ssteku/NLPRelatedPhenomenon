import concurrent.futures
import math
import random

from src.CategoriesAnalizer.Classifiers.DecisionTreeClassifier import DecisionTreeClassifier
from src.CategoriesAnalizer.Classifiers.MLPClassifier import MLPClassifier
from src.CategoriesAnalizer.Classifiers.MaxentClassifier import MaxentClassifier
from src.CategoriesAnalizer.Classifiers.NaiveBayesClassifier import NaiveBayesClassifier
from src.CategoriesAnalizer.TrainingSetGenerator import TrainingSetGenerator


class Classifier(object):
    def __init__(self, feature_name, configuration_map):
        print("Classifier")
        self.__feature_name = feature_name
        self.__configuration_map = configuration_map

    def classify(self, article_db, most_frequent_words):
        results = {}
        executor = concurrent.futures.ProcessPoolExecutor(self.__configuration_map['repeat_test_count'])
        for level in self.__configuration_map['database_structure']['levels']:
            print("------ Classification for level : " + level + " ------")
            training_set_gen = TrainingSetGenerator(self.__feature_name, self.__configuration_map)
            training_set = training_set_gen.get_training_set(article_db, most_frequent_words, level)

            level_results = self.__perform_clasification(executor, training_set)
            results[level] = level_results
        return results

    def __perform_clasification(self, executor, training_set):
        if self.__is_training_set_proper(training_set):
            return self.__classify_with_all_classifiers(executor, training_set)
        else:
            print("Too less elements in training set")

    def __classify_with_all_classifiers(self, executor, training_set):
        classifiers = [
            MLPClassifier(self.__configuration_map),
            NaiveBayesClassifier(self.__configuration_map),
            DecisionTreeClassifier(self.__configuration_map),
            MaxentClassifier(self.__configuration_map)]
        minimal_training_set_size = self.__configuration_map['training_to_test_set_size_ratio']
        train_size = int(math.floor(len(training_set) * minimal_training_set_size))
        results = {}
        print("Data set size: " + str(len(training_set)))
        print("Train size: " + str(train_size))
        print("Test size: " + str(len(training_set) - train_size))
        for classifier in classifiers:

            if classifier.__class__.__name__ in self.__configuration_map['classifiers']:
                sum_result = 0.0
                print("------ ------ Classifier: " + classifier.__class__.__name__ + '------')
                results[classifier.__class__.__name__] = test_classifier(executor, classifier, self.__configuration_map['repeat_test_count'], training_set, train_size)
                print("Avarage accuracy : " + str(results[classifier.__class__.__name__]))
            else:
                print("Classifier rejected")
        return results



    def __is_training_set_proper(self, training_set):
        return len(training_set) > self.__configuration_map['minimal_training_set_size']

def test_classifier(executor, classifier, test_count, training_set, train_size):
    sum_result = 0.0
    print("------ ------ Classifier: " + classifier.__class__.__name__ + '------')

    futures_pool = [executor.submit(
        unit_test, classifier, training_set, train_size)
               for i in range(test_count)]
    concurrent.futures.wait(futures_pool)
    for fut in futures_pool:
        sum_result += fut.result()
    return sum_result/test_count

def unit_test(classifier, training_set, train_size):
    random.shuffle(training_set)
    classifier.trainClasifier(training_set[:train_size])
    return classifier.testClasifier(training_set[train_size:])