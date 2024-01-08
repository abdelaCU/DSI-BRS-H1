# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:59:05 2024

@author: abdel
"""

import argparse
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('config_file', type=str)
args = parser.parse_args()

print("******************************")
print (args)
print("***********************************")


with open(args.config_file, 'r') as f:
    this_config = yaml.safe_load(f)

print(this_config)
print(this_config['color'])
print(this_config['dataset_url'])
print(this_config['cols_to_plot'])