'''
Author: Adam Simon
Date: 7/13/2018

App for insight code challenge:
https://github.com/InsightDataScience/pharmacy_counting

outside lib faker only used to build test data, challenge stipulated only
standard lib packages could be used
'''
import csv
import operator
import sys

from faker import Faker

faker = Faker()

def generate_results(in_file, out_file):
    # paramter should be input txt file as list
    # create dictionary
    with open(in_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        a_list = [row for row in reader]
    dict_drug_cnt = {}
    f_list = []
    for i in a_list:
        prov_dict = {
                'id': i[0],
                'prov_last': i[1],
                'prov_first': i[2],
                }
        if i[3] in dict_drug_cnt:
            dict_drug_cnt[i[3]]['count'] += 1
            dict_drug_cnt[i[3]]['total_cost'] += int(i[4] )
            dict_drug_cnt[i[3]]['prov_list'].append(prov_dict)
        else:
            prov_dict = {
                'id': i[0],
                'prov_last': i[1],
                'prov_first': i[2],
                }
            try:
                dict_drug_cnt[i[3]] = {
                    'count': 1,
                    'total_cost': int(i[4]),
                    'prov_list': list([prov_dict]),
                }
            except ValueError:
                pass
    for k, v in dict_drug_cnt.items():
        f_list.append([k, v['count'], v['total_cost']])
    s = sorted(f_list, key=operator.itemgetter(2,0), reverse=True)
    header = ['drug_name','num_prescriber','total_cost']
    with open(out_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        writer.writerows(s)
    return f_list

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('No arguments provided, please provide input/output')
    else:
        in_file = str(sys.argv[1])
        out_file = str(sys.argv[2])
        out = generate_results(in_file, out_file)


