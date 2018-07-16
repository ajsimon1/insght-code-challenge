# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:09:34 2018

@author: Adam
"""
import csv
import itertools
import random
import sys
# only outside package
from faker import Faker

# pulled in for drug names to add
fda_drug_info = '.\src\product.csv'
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
    # drug names in list come with brackets, quotations and mixed case
    # these chars were removed and all names set to uppercase for consistency
    headers = ['id','prescriber_last_name','prescriber_first_name','drug_name','drug_cost']
    # chars to remove
    bad_chars = ['[', ']', "'"]
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        drug_name_list = [row for row in reader]
    # case to string to use replace() method
    drug_name_list = [str(x) for x in drug_name_list]
    # iterate over bad_chars list replacing each with '' to clean data
    for ch in bad_chars:
        drug_name_list = [x.replace(ch, '') for x in drug_name_list]
    # additional cleaning step, removed any drugs with long names
    drug_name_list = [x for x in drug_name_list if len(x) < 15]
    # create set to remove and duplicates
    drug_name_set = set(drug_name_list)
    # took a slide of 75 drugs from the 9,000 available, this was to ensure that
    # the dummy data had duplicates when adding to input data
    drug_final = list(itertools.islice(drug_name_set, 75))
    # build npi list, used 45 #s to ensure duplicates were in input data
    npi_list = list(range(100000001,100000045))
    # build provder name list
    providers= []
    # used faker module to create dummy names
    prov_list = [faker.name() for x in range(1, 33)]
    # split names into first and last, as per input formatting
    prov_list = [x.split() for x in prov_list]
    # iterate through fake names and assocaite with npi # created previously
    # this was to ensure that provider always had same npi #
    for i in prov_list:
        r = random.choice(npi_list)
        providers.append([r, i[1], i[0]])
        npi_list.remove(r) # necessary to ensure 1 npi == 1 provider
    # build cost list, incremented in 25
    cost_list = list(range(5, 1000, 25))
    # build final list
    test_input = []
    # add headers first
    test_input.append(headers)
    # edit save of input file here by adjusting '101' to however many records
    # are needed
    # random module used for selecting, no random seed was used so input data
    # is different every time, this was done intentionally
    for a in range(1,101):
        row = []
        # unpack providers line item
        a, b, c = random.choice(providers)
        row.append(a)
        row.append(b)
        row.append(c)
        row.append(random.choice(drug_final).upper())
        row.append(random.choice(cost_list))
        test_input.append(row)
    return test_input

# output_csv func takes input list created in build_dummy_data func and outputs
# to file specified as argument
def output_csv(filename, out_list):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(out_list)

if __name__ == '__main__':
    out_file = str(sys.argv[1])
    inp = build_dummy_data(fda_drug_info)
    output_csv(out_file, inp)
