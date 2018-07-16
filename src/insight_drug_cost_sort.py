'''
Author: Adam Simon
Date: 7/13/2018

App for insight code challenge:
https://github.com/InsightDataScience/pharmacy_counting
'''
import csv
import operator
import sys

def generate_results(in_file, out_file):
    '''
    function accepts the input file and produces output file.
    Input file expected to be formatted as below, there are no validations built
    in to check formatting
    ###
    id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
    1000000001,Smith,James,AMBIEN,100
    ###
    Output file should be created prior to running application. File can be
    or contain text, the application will overwrite any information that
    existed in the file prior to running the app.  formatting of output file is:
    ###
    drug_name,num_prescriber,total_cost
    CHLORPROMAZINE,2,3000
    ###
    parameters:
        in_file --> input file as csv or txt, formatting expected described above
        out_file --> name of output file, this is expected to be created
                    prior to running application
    returns:
        f_list --> result data mirroring out_file as list
        out_file --> output file as txt, formatted as described above

    function was tested for performance against 1,000,000 line input set,
    bottleneck is creation of dict which took 5.05 seconds to complete. could
    look to optimize this during refactoring
    '''
    # create dictionary used to format results prior to
    dict_drug_cnt = {}
    final_list = [] # create list to write to csv
    # open input file using 'with' context as per standard, add file contents
    # to list
    # iterate over input file contents, and add to dict creating 'count' of
    # providers that prescribed drug as well as 'total_cost' of drug
    # dict data type used to better organize results data
    with open(in_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            prov_dict = {
                    'id': row[0],
                    'prov_last': row[1],
                    'prov_first': row[2],
                    }
            if row[3] in dict_drug_cnt:
                dict_drug_cnt[row[3]]['count'] += 1
                dict_drug_cnt[row[3]]['total_cost'] += int(row[4] )
                dict_drug_cnt[row[3]]['prov_list'].append(prov_dict)
            else:
                prov_dict = {
                    'id': row[0],
                    'prov_last': row[1],
                    'prov_first': row[2],
                    }
                try:
                    dict_drug_cnt[row[3]] = {
                        'count': 1,
                        'total_cost': int(row[4]),
                        'prov_list': list([prov_dict]),
                    }
                except ValueError:
                    pass
    # iterate over dict, add to f_list in desired format
    for key, val in dict_drug_cnt.items():
        f_list.append([key, val['count'], val['total_cost']])
    # sort list by total_cost then by drug name, reverse=True indicates descending
    sorted_list = sorted(final_list, key=operator.itemgetter(2,0), reverse=True)
    # create header rows for file
    header = ['drug_name','num_prescriber','total_cost']
    with open(out_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        writer.writerows(sorted_list)
    return final_list

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ALERT: No arguments provided, please provide input/output filenames')
    else:
        in_file = str(sys.argv[1])
        out_file = str(sys.argv[2])
        out = generate_results(in_file, out_file)
