import sys
from Tools import HeaderPreprocessor
from Tools import FunctionCollector
from Tools import IfCollector

fileName = "test1.cpp"

HeaderPreprocessor.HeaderPreprocessor(fileName)

FunctionCollector.FunctionCollector(fileName)

IfCollector.IfCollectorHelper()