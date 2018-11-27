import pandas as pd

def task2_1():
    df = pd.read_csv('NYC_Jobs.csv', sep=',')
    print(df['Agency'].head(10))


def task2_2():
    df = pd.read_csv('NYC_Jobs.csv')
    names = ['Agency', 'Business Title','Work Location 1']
    print(df[names])


if __name__=="__main__":
    task2_1()
    task2_2()
