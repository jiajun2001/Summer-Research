from Tools.util import HeaderPreprocessor
from Tools.collector import SubRoutineCollector
from Tools.detector import Rule1Detector

fileName = "test1.cpp"

HeaderPreprocessor.HeaderPreprocessor(fileName)

SubRoutineCollector.FunctionCollector(fileName)

Rule1Detector.Rule1Detector()

