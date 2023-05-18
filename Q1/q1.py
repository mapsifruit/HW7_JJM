import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm

def main() :
    #q1
    arr = np.array([[1,2],[3,4]])
    eig_val,eig_vec = np.linalg.eig(arr)
    det = np.linalg.det(arr)
    print("Eigenvalues : \n",eig_val)
    print("Eigenvectors : \n",eig_vec)
    print("Determinanat : \n",det)
    

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    crs = np.cross(vec1,vec2)

    print("Cross product \n: ",crs)

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    B = np.array([[-15],[-21],[18]])
    C = np.linalg.solve(A,B)
    print("Solution  : \n",C)
    

if __name__ == "__main__" :
    main()
