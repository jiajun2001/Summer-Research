from Tools.collector import InnerNodesCollector

def Rule1Detector():
    InnerNodesCollector.InnerNodesCollectorHelper(
        "IfStmt", 
        "kind", 
        "temp/functionNodes.json", 
        "temp/ifNodes.json"
    )
    InnerNodesCollector.InnerNodesCollectorHelper(
        "BinaryOperator", 
        "kind", 
        "temp/ifNodes.json", 
        "temp/booleanOperatorNodes.json"
    )
    
    

