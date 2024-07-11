import os
import yaml
import pandas as pd
import numpy as np
import argparse
#from pkgutil import get_data
from get_data import get_data, read_params


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in df.columns]
    #print(new_cols)
    raw_data_path = config["load_data"]["raw_data"]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)
    return load_and_save



if __name__=="__main___":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)