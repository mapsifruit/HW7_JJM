import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm

def main() :
    df = pd.DataFrame(np.array([[1000,25],[280,120],[900,30]]),index=['store1','store2','store3'],columns=['unit price','number'])
    print(df)
    df['total price'] = df['unit price'] * df['number']
    print(df)
    df2 = df.sort_values(by='total price', ascending=False)
    df2 = df2.head(2)
    print(df2)
    

if __name__ == "__main__" :
    main()
