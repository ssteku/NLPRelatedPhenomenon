import numpy as np
import transaction

from src.Testing.ChartsDrawer import ChartsDrawer


class Tester(object):
    def __init__(self, test_config, database):
        self.__test_config = test_config
        self.__databse = database
        self.__charts_drawer = ChartsDrawer()

    def perform_tests(self, feature_analizer):
        # current_configuration = self.__get
        tests = self.__test_config['test_plan']
        self.__create_old_charts()
        for test in tests.keys():
            print("Performing test : " + test)
            tests[test] = self.__execute_test(feature_analizer, tests[test])
    def __create_old_charts(self):

        for result in self.__databse.dbroot['test_results'].keys():
            testcase_conf = self.__databse.dbroot['test_results'][result]
            values_range = np.arange(
                testcase_conf['min_value'], testcase_conf['max_value'], testcase_conf['step'])
            self.__charts_drawer.create_charts(testcase_conf, values_range)

    def __execute_test(self, feature_analizer, testcase_conf):
        values_range = np.arange(
            testcase_conf['min_value'], testcase_conf['max_value'], testcase_conf['step'])
        print("Range : " + str(values_range))
        for value in values_range:
            configuration = self.__get_configuration(
                testcase_conf['config'].get_configuration_map(), testcase_conf['param_name'], value)
            conf_with_classifiers = self.__get_configuration(
                configuration, ['classifiers'], testcase_conf['classifiers'])
            value_results = feature_analizer.prepare_model(conf_with_classifiers)
            current_results = testcase_conf['results']
            testcase_conf['results'] =  self.__accumulate_results(current_results, value_results)
        self.__databse.dbroot['test_results'][testcase_conf['title']] = testcase_conf
        transaction.commit()
        print("Results databse size: " + str(len(self.__databse.dbroot['test_results'].keys())))
        self.__charts_drawer.create_charts(testcase_conf, values_range)

        return testcase_conf

    def __get_configuration(self, default_configuration, param_name_list, value):
        if len(param_name_list) == 1:
            print("Setting to value: " + str(value) + " param: " + param_name_list[0])
            default_configuration[param_name_list[0]] = value
            return default_configuration
        else:
            head_param = param_name_list[0]
            print("Going deeper, param: " + head_param)
            default_configuration[head_param] = self.__get_configuration(default_configuration[head_param], param_name_list[1:], value)
            return default_configuration

    def __accumulate_results(self, current_results, value_results):

        for level in  current_results['levels'].keys():
            for value_class in value_results[level].keys():
                if current_results['levels'][level].has_key(value_class):
                    current_results['levels'][level][value_class].append(value_results[level][value_class])
                else:
                    current_results['levels'][level][value_class] = []
                    current_results['levels'][level][value_class].append(value_results[level][value_class])

        return current_results

