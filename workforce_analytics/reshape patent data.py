import csv
import numpy as np

### STEP 0 A
with open('C:/Users/chanbaik/desktop/Spring Term/Workforce Analytics/Data/Data/D3 patent_data.csv', 'rb') as f:
    next(f) #skip header row
    reader = csv.reader(f,delimiter=',')
    pnum=[]; firm=[]; year=[]; perf=[]; invnum=[]; lastname=[]; cntries=[]
    for row in reader:
            pnum.append(row[0])
            firm.append(row[1])
            year.append(row[2])
            perf.append(int(row[3]))
            invnum.append(row[4])
            lastname.append(row[5])
            cntries.append(row[6])
    f.close()



### STEP 0B  read competitor file 

import pickle

pkl_file = open("C:/Users/chanbaik/desktop/Spring Term/Workforce Analytics/Data/Data/firm_competition_data.pkl","rb")
firm_competition=pickle.load(pkl_file)
pkl_file.close()

        
# Find the average compeition that a firm faces        

avg_comp=[]
comp_names=[]
for key in firm:
    if firm_competition.has_key(key):
        tup=firm_competition[key]
        comp_vals=[val for comp,val in tup] # return the list of competition measures in the tuple
        comp_firms=[comp for comp,val in tup if val>0.24] # Find highest competitors (i.e, firms with competing_values > 0.24)
        mn=np.mean(comp_vals)
        avg_comp.append(mn)
        comp_names.append(comp_firms)
    else:
        avg_comp.append("0")
        comp_names.append([])
                 
    
                                                  
 
# STEP 1 RESHAPE DATA 
inv_reshape=[]; pnum_reshape=[];

for  i in range(len(invnum)):
    these_invs=invnum[i].split(';') # split inventor list by semicolon
    inv_reshape=inv_reshape+these_invs
    for j in range(len(these_invs)):
        pnum_reshape.append(pnum[i])
  
    
unq_inventors= list(set(inv_reshape))
        
 
# STEP 3 DEFINE FUNCTION all_indices
def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices
           
           
# STEP 2 INVENTOR-PROJECT DICTIONARY
inv_proj={}
for inv in unq_inventors:
    inds=all_indices(inv, inv_reshape) 
    pat_list =[pnum_reshape[i] for i in inds] 
    pat_list = list(np.sort(pat_list))
    inv_proj[inv]=pat_list
      
# STEP 4 IDENTIFY INVENTORS WHO WORK ON MULTIPLE PROJECTS
 
multiproj_invs={}

for key in inv_proj:
    pat_list=inv_proj[key] 
    if len(pat_list)>1:
        multiproj_invs[key]=pat_list
        
        

# STEP 5 IDENTIFY MOBILE INVENTORS
mobile_invs={}
 
for key in multiproj_invs:
    pat_list = multiproj_invs[key]
    inds =  [pnum.index(pat) for pat in pat_list]
    firm_list = [firm[i] for i in inds] 
    if len(set(firm_list))>1:
        mobile_invs[key]=firm_list