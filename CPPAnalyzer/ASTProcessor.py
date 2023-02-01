from Tools.util import HeaderPreprocessor
from Tools.collector import SubRoutineCollector
from Tools.detector import Rule1Detector
from Tools.detector import Rule2Detector
from Tools.detector import Rule3Detector
from Tools.detector import Rule9Detector

fileName = "test_Rule9.cpp"

# Preprocess Stage
HeaderPreprocessor.HeaderPreprocessor(fileName)
SubRoutineCollector.FunctionCollector(fileName)

# Rule Detecting Stage
Rule1Detector.Rule1Detector(fileName)
Rule2Detector.Rule2Detector(fileName)
Rule3Detector.Rule3Detector(fileName)

Rule9Detector.Rule9Detector(fileName)