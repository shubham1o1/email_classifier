import demjson
import csv

def jstopy():
    #convert js object's array to python dictionary's list
    emlist = [] #list of dictionaries
    with open ("emails.txt","r") as file : 
        emails = file.readlines()
    for email in emails:
        emailnew = str(email)[:-2] #remove comma and \n at end of line
        py = demjson.decode(emailnew) # convert js object to python dictionary
        emlist.append(py) # add new email to list
    return emlist

def extract_kw():
    # extracts the key words
    lis = jstopy()
    i = 0
    s = set() #list of keywords with no repetition 
    while i < len(lis):
        s.update(set((lis[i].keys()))) 
        #converts dictionaries into dictionary keys
        i += 1
    # print(type(s))
    return s


def make_csv():
    # makes 30*30 csv file of key words and their association
    s = extract_kw()
    with open('emaildf.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(list(s))
        for elem in s:
            l = []
            for nestelem in s:
                score = get_score(elem,nestelem)
                l.append(score)
                print(len(l))
            filewriter.writerow(l)

def get_score(elem,nestelem):
    # Scoring each pair one point for each of their occurrences together
    ld = jstopy()
    score = 0
    for i in range(26):
        s = set(ld[i].keys())
        if elem in s and nestelem in s:
            score += 1
    print(score)

    return score



