# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:15:55 2014

@author: samuelkahn
"""
### Scikit-learn to run regression model
import pandas as pd
import os
from sklearn import linear_model
import numpy as np
#### Converts txt file from BLS to csv
### Input: BLS txt file with 1990-1999 population data by FIPS
### Output. CSV with 1990-1999 population data by FIPS that is CLEANED
def txt_to_csv(filename):
    ### Empty dataframe
    df = pd.DataFrame(columns=('year', 'fips', 'population'))
    
    with open(filename) as f:
        index=0
        for line in f:
            try:
                ### For each line return list with white-space removed
                one_row=[int(x) for x in line.split(' ') if x!='' and x!='\r\n']
                ### Add rows to dataframe, column 3 is sum of all populations
                df.loc[index]=[int(one_row[0]),one_row[1],sum(one_row[2:-1])]
                index+=1
                print index
            ### Catches header
            except ValueError:
                continue
    ### Writes tot CSV
    df.to_csv('1990_1999_population.csv',sep=',',index=False)


###  generate data for 2000-2014
### Input: Cleaned CSV of 1990-1999 population data by FIPS
### Output: CSV with 1990-2014 population data by FIPS
def run_regressions(filename):
    ### Reading in CSV
    df=pd.DataFrame.from_csv(filename,index_col=False)
    
    fips_list= list(set(df['fips'].tolist()))
    complete_dataframe=pd.DataFrame(columns=('year', 'fips', 'population'))
    ### 
    index=0
    df_index=len(df)
    prediction_years=np.array(range(2000,2015)).reshape(15,1)
    
    for code in fips_list:
        print 'Fitting regression: '+str(index)+'/'+str(len(fips_list))
        fips_df=df[df['fips']==code]
        ## Dependent and Independent variables        
        Y=np.array(fips_df['population'].tolist()).reshape(10,1)
        X=np.array(fips_df['year'].tolist()).reshape(10,1)
        ### Fit and 
        reg_fit = linear_model.LinearRegression().fit(X,Y)
        fitted_results=reg_fit.predict(prediction_years).tolist()
        
        for x in range(0,len(fitted_results)):
            df.loc[df_index]=[prediction_years[x][0],code,fitted_results[x][0]]
            df_index+=1
        index+=1
        
        complete_dataframe=complete_dataframe.append(df[df['fips']==code])
    complete_dataframe.to_csv('1990_2014_population.csv',sep=',',index=False)
        
def main():
    path='/Users/samuelkahn/Desktop/Berkeley/DS205/Final Project'
    os.chdir(path)
    ### Convert BLS provided txt file to csv for easier processing
    txt_to_csv('1990-1999_population.txt')
    run_regressions('1990_1999_population.csv')

    
if __name__=='__main__':
    main()