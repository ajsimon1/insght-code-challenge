# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:09:34 2018

@author: Adam
"""
import csv
import itertools
import random
import sys

from faker import Faker


fda_drug_info = 'product.csv'
# in_file = 'insight_input_100.txt'
# out_file = 'output.txt'
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
    headers = ['id','prescriber_last_name','prescriber_first_name','drug_name','drug_cost']
    bad_chars = ['[', ']', "'"]
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        drug_name_list = [row for row in reader]
    drug_name_list = [str(x) for x in drug_name_list]
    for ch in bad_chars:
        drug_name_list = [x.replace(ch, '') for x in drug_name_list]
    drug_name_list = [x for x in drug_name_list if len(x) < 15]
    drug_name_set = set(drug_name_list)
    drug_final = list(itertools.islice(drug_name_set, 75))
    # build npi list
    npi_list = list(range(100000001,100000045))
    # build provder name list
    providers= []
    prov_list = [faker.name() for x in range(1, 33)]
    prov_list = [x.split() for x in prov_list]
    for i in prov_list:
        r= random.choice(npi_list)
        providers.append([r, i[1], i[0]])
        npi_list.remove(r)
    # build cost list
    cost_list = list(range(5, 1000, 25))
    # build final list
    test_input = []
    test_input.append(headers)
    for a in range(1,101):
        row = []
        a, b, c = random.choice(providers)
        row.append(a)
        row.append(b)
        row.append(c)
        row.append(random.choice(drug_final).upper())
        row.append(random.choice(cost_list))        
        test_input.append(row)
    return test_input


def output_csv(filename, out_list):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(out_list)
        
if __name__ == '__main__':
    out_file = str(sys.argv[1])
    inp = build_dummy_data(fda_drug_info)
    output_csv(out_file, inp)