from src.Configuration.DefaultConf import DefaultConf
from src.Configuration.TestConfiguration import TestConfiguration
from src.FeatureAnalisys import FeatureAnalisys
from src.Testing.Tester import Tester
from src.storage.DatabaseFacade import DatabaseFacade

test_conf = TestConfiguration().get_configuration_map()
database = DatabaseFacade(DefaultConf().get_configuration_map()['database_path'])

analizer = FeatureAnalisys(
    feature_name = "sentiment", feature_values=['negative', 'positive'], database=database)
tester = Tester(test_conf, database)
tester.perform_tests(analizer)
#connect to a URL
