"""Pipeline for cleaning raw dataset."""
import pandas as pd
import numpy as np

from dretch import io


def main():
    # load raw data
    raw_data = pd.read_csv("seafloor_lith_data_all_features.csv")

    # convert special missing notation to nan
    data = raw_data.replace(to_replace='nan', value=np.nan) 
    training_bool = pd.notnull(data['lithology'])
    query_bool = ~training_bool

    data_train = data[training_bool].copy()
    data_train['lithology'] = data_train['lithology'].astype(int).astype(str)
    data_query = data[query_bool].copy()    

    io.save_csv(data_train, 'train_clean.csv', index=False)
    io.save_csv(data_query, 'test_clean.csv', index=False)

    return data


if __name__ == '__main__':
    main()
