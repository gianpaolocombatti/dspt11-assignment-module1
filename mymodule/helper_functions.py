import pandas as pd
import numpy as np

def null_count(df):
    print(df.isna().sum())

def train_test_split(df,frac):
    def train_test_split(df, frac):
        test_indexes = np.random.choice(
            df.index, int(df.shape[0] * frac), replace=False)
        train_indexes = [i for i in df.index if i not in test_indexes]
        test_df = df.iloc[test_indexes, :]
        train_df = df.iloc[train_indexes, :]
        print(
            f'Shape of original df = {df.shape}, test DF = {test_df.shape}, train DF = {train_df.shape}')
        return (test_df, train_df)

