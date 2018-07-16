# Pharmacy Counting App

Approach to the problem was relatively simple, create a dictionary to organize
the data and create total_cost and count numbers; then export to as txt file.  

There is a second script, `create_dummy_data.py`, that builds out the input
file used during testing.  There is a depedency on the `products.csv`, which
can be downloaded as a zip file
[here](https://www.fda.gov/drugs/informationondrugs/ucm142438.htm). I modified
the file so that it only included the *PROPRIETARYNAME* column, then saved it
as a csv file.  

*Please note an ouside package. 'faker' was used to create the
dummy data.  No outside packages were used in the main script*

I did a time trial on the app using an input file of 1,000,001 records. The app
took 5.06022 seconds to run, with the bottleneck occurring during creation of
the `dict_drug_cnt` dict, taking 5.052717 s to finish.  This is the point where
the code could be refactored for optimization.   

## Application instructions

1. Run *create_dummy_data.py* file to build input file (if needed)
    - add filepath as cmd argument
2. Run *insight_drug_cost_sort.py* file to create sorted drug list
    - add input  and output filepath as cmd arguments
