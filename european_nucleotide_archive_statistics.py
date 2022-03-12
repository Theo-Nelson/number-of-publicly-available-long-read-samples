#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Generate European Nucleotide Archive Usage Statistics for Long-Read Sequencing Samples

Author: Theo Nelson (tmn2126)
"""

import requests

def generate_general_run_statistics():
    
    dates = []
    values = []
    
    # i = years (default: 2011 - 2022)
    for i in range(11,23):
        
        # j = months (default: Jan, Mar, May, Jul, Sept, Nov)
        for j in range(1,13,2):
            
            # exclude May, 2022 - Nov, 2022
            if(i == 22 and j > 3):
                print("non-existant")
            else:
                # set up with parameters according to the European Nucleotide Archive's Advanced Search (https://www.ebi.ac.uk/ena/browser/advanced-search)
                r  = requests.get("https://www.ebi.ac.uk/ena/portal/api/count?dataPortal=ena&dccDataOnly=false&query=first_public%3C%3D20"+str(i)+"-"+str(j).zfill(2)+"-01 AND read_count>100000 AND (instrument_platform=\"OXFORD_NANOPORE\" OR instrument_platform=\"PACBIO_SMRT\")&result=read_run")
                data = r.text
                dates.append("20"+str(i)+"-"+str(j)+"-01")
                values.append(data)
     
    # regular console print - allows programmer to manually check successful retrieval            
    print(dates)
    print(values)
    
    # export results to a TXT file for further analysis
    with open('number_of_long_read_sequencing_values.txt', 'w') as my_file:
        my_file.write("Dates" + '\t' + "Number of Long-Read Sequencing Samples" + '\n')    
        for i in range(0,len(dates)):
            my_file.write(dates[i] + '\t' + values[i] + '\n')
        print('File created')
  
def main():
    generate_general_run_statistics()
   
main()

