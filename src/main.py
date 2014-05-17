from FeatureAnalisys import FeatureAnalisys
from Configuration.DefaultConf import DefaultConf
from Configuration.TestConfiguration import TestConfiguration
from Testing.Tester import Tester


conf = DefaultConf().get_configuration_map()
test_conf = TestConfiguration().get_configuration_map()

analizer = FeatureAnalisys(
    feature_name = "sentiment", feature_values=['negative', 'positive'], configuration = conf)
# results = analizer.prepare_model(conf)
tester = Tester(test_conf)
tester.perform_tests(analizer, conf)
#connect to a URL
