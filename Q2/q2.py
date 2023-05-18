import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm

def main() :
    Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query = np.array([1,1,0,0,1,0])
    sim = dot(Docs,Query)/(norm(Docs)*norm(Query))
    print("doc1={0:.2f}\ndoc2={1:.2f}\ndoc3={2:.2f}".format(sim[0],sim[1],sim[2]))

if __name__ == "__main__" :
    main()
