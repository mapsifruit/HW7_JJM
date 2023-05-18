import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm

def main() :
    df = pd.read_csv('gender2.csv', encoding='cp949')
    df2 = df.loc[:,['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']]
    df2.columns = ['Total','Male','Female']
    print(df2)
    


if __name__ == "__main__" :
    main()
