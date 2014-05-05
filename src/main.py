from FeatureAnalisys import FeatureAnalisys
from Configuration.DefaultConf import DefaultConf

conf = DefaultConf()
analizer = FeatureAnalisys(
    feature_name = "sentiment", feature_values=['negative', 'positive'], configuration = conf)
analizer.prepare_model()
#connect to a URL
