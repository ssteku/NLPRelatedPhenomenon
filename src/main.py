from FeatureAnalisys import FeatureAnalisys
from Configuration.DefaultConf import DefaultConf
from Configuration.TestConfiguration import TestConfiguration
from Testing.Tester import Tester
from storage.DatabaseFacade import DatabaseFacade

test_conf = TestConfiguration().get_configuration_map()
database = DatabaseFacade(DefaultConf().get_configuration_map()['database_path'])

analizer = FeatureAnalisys(
    feature_name = "sentiment", feature_values=['negative', 'positive'], database=database)
tester = Tester(test_conf, database)
tester.perform_tests(analizer)
#connect to a URL
