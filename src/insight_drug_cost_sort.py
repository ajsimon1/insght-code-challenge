'''
Author: Adam Simon
Date: 7/13/2018

App for insight code challenge:
https://github.com/InsightDataScience/pharmacy_counting

outside lib faker only used to build test data, challenge stipulated only
standard lib packages could be used
'''
from faker import Faker
import csv

# TODO accept arg input from command line
# TODO write func to build dummy data to test

filename = 'unfinished_product.csv'
faker = Faker()


def build_dummy_data(filename):
    '''
    func builds out test input with dummy data using drug name list from fda
    and 'faker' package
    arguments:
        filename --> should be in same folder as app
    returns:
        txt file formatted for immediate use
    '''
    # clean fda drug list, create set to avoid dupes
    bad_chars = ['[', ']', "'"]
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        drug_name_list = [row for row in reader]
    drug_name_list = [str(x) for x in drug_name_list]
    for ch in bad_chars:
        drug_name_list = [x.replace(ch, '') for x in drug_name_list]
    drug_name_list = [x for x in drug_name_list if len(x) < 15]
    drug_name_set = set(drug_name_list)
    # build npi list
    npi_list = list(range(100000001,100000045))
    # build provder name list
    prov_list = [faker.name() for x in range(1, 33)]
    # build cost list
    cost_list = list(range(5, 1000, 25))
    return drug_name_set


build_dummy_data(filename)
