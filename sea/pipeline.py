"""Pipeline for cleaning raw dataset."""
import pandas as pd
import numpy as np
from typing import Any

from dretch import io, config

RAW_DATA = 'data/seafloor_lith_data_all_features.csv'


def main() -> Any:
    # load raw data
    raw_data = pd.read_csv(RAW_DATA)

    # convert special missing notation to nan
    data = raw_data.replace(to_replace='nan', value=np.nan)
    training_bool = pd.notnull(data['lithology'])
    query_bool = ~training_bool

    data_train = data[training_bool].copy()
    data_train['lithology'] = data_train['lithology'].astype(int).astype(str)
    data_query = data[query_bool].copy()

    io.save_csv(data_train, config.train_data, index=False)
    io.save_csv(data_query, config.query_data, index=False)

    return data


if __name__ == '__main__':
    main()
