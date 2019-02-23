import dataPrep
import pandas as pd
import csv

ld = dataPrep.jstopy()
s = dataPrep.extract_kw()

def get_total_words ():
    # find total words we are dealing with
    total_words = 0
    for i in range(26):
        list_values = list(ld[i].values())
        for l in list_values:
            total_words += int(l)
        list_values.clear()
    return total_words #392

def total_keys(key):
    # find total number of occurence of each words
    total = 0
    for i in range(26):
        if key in ld[i].keys():
            total += int(ld[i][key])
    return total # google -> 21


def get_support ():
    # find support for each word
    support_dict = {}
    total_words = get_total_words()
    for elem in s:
        support_dict[elem] = total_keys(elem)/ total_words
    return support_dict

def regression ():
    # perform a regression-like operation to fit a keyword into a space
    # This space is defined by occurrence of each keywords
    support_dict = get_support()
    reg_dict = {}
    df = pd.read_csv('emaildf.csv')
    i = 0
    l = []
    l = df[:0] # first row elements
    # print(l)
    for elem in l:
        reg_dict[elem] = df.loc[i,elem]
        # items such as (facebook,facebook) denotes number of emails facebook has occurred in

        for nestelem in l:
            if (nestelem != elem):
                reg_dict[elem] += df.loc[i,nestelem]*support_dict[nestelem]
        i += 1
    return reg_dict


def pair_support_regression():
    # pair regression score and support for each keyword
    supp_dict = get_support()
    reg_dict = regression()
    sup_reg_dict = {}
    for elem in s:
        sup_reg_dict[elem] = [reg_dict[elem],supp_dict[elem]]
    return sup_reg_dict

def write_files():
    # write a csv file with columns: keywords, Regression, Support
    dataset = pair_support_regression()
    list_kw = list(dataset.keys())
    list_pair = list(dataset.values())
    l =[]
    with open('pair_reg_sup.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Keywords","Regression", "Support"])
        for i in range(len(list_kw)):
            l = [list_kw[i],list_pair[i][0],list_pair[i][1]]
            filewriter.writerow(l)