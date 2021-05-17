import pandas as pd
import numpy as np

class Helper:
    def __init__(self, df):
        self.df = df

    def null_count(self):
        return(self.df.isnull().sum().sum())

    def train_test_split(self, frac):
        test_indexes = np.random.choice(
            self.df.index, int(self.df.shape[0] * frac), replace=False)
        train_indexes = [i for i in self.df.index if i not in test_indexes]
        test_df = self.df.iloc[test_indexes, :]
        train_df = self.df.iloc[train_indexes, :]
        print(
            f'Shape of original df = {self.df.shape},'
            f' test DF = {test_df.shape}, '
            f'train DF = {train_df.shape}')
        return (test_df, train_df)

print("hello world")