# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 22:32:09 2014

@author: samuel
"""
import os
import sqlite3

# create a Connection object that represents the database
def create_database(dbname):
    conn = sqlite3.connect(dbname)
    return conn
### Create the relevant tables if they do not already exist     
def create_table(cur, tname,column1,column2):
    query='CREATE TABLE IF NOT EXISTS '+tname+'('+column1+','+column2+')'
    cur.execute(query)
    return cur
### Functuon to insrt data into a given database
def insert_data(cur,tname,data):
    query= 'INSERT INTO '+tname+' VALUES ("'+data[0]+'","'+data[1]+'")'
    cur.execute(query)
    return cur

def main():
    dbname='stubs.db'
    
    ### List that contains relevant name
    ### first element in each tuple is the name of the database
    ### second is the text file that has the information in it
    ### third and fourth element in ec tuple are the column names
    tables_files_columns=[]  
    tables_files_columns.append(('pages','pages.txt','page_id','page_title'))
    tables_files_columns.append(('users','users.txt','user_id','username'))
    tables_files_columns.append(('page_users','page_users.txt','page_id','user_id'))
    
    ### Connect to database and create the cursor
    conn=create_database(dbname)
    cur=conn.cursor()
    
    ### Delete the tables if they dont exist already, if we dont do this we will get bad answer
    cur.execute('DROP TABLE IF EXISTS '+tables_files_columns[0][0])
    cur.execute('DROP TABLE IF EXISTS '+tables_files_columns[1][0])
    cur.execute('DROP TABLE IF EXISTS '+tables_files_columns[2][0])
    
    ### Create the tables
    cur=create_table(cur,tables_files_columns[0][0],tables_files_columns[0][2],tables_files_columns[0][3])
    cur=create_table(cur,tables_files_columns[1][0],tables_files_columns[1][2],tables_files_columns[1][3])
    cur=create_table(cur,tables_files_columns[2][0],tables_files_columns[2][2],tables_files_columns[2][3])

    #### Inserts into each table
    for tup in tables_files_columns:
        with open(tup[1]) as fp:
            for line in fp:
                line=line.replace('\n','')
                data=line.split('\t')
                cur=insert_data(cur,tup[0],data)
                
    ## Now write a sql query on the database to find out which username has written maximum number of pages
    ### SQL Query (This could be done much easier than this but I wanted to practice my SQL)
    ### I essentially join the three tables and thn group by username and and page title
    ### This returns duplicates so we then group by userame again and then order the resulting table in descending order

    sql_statement='SELECT username, COUNT(*) as frequency'+\
    ' FROM'+\
    ' (SELECT page_users.page_id, page_users.user_id,pages.page_title, users.username'+\
    ' FROM page_users'+\
    ' LEFT JOIN pages'+\
    ' ON page_users.page_id=pages.page_id'+\
    ' INNER JOIN users'+\
    ' ON page_users.user_id=users.user_id'+\
    ' GROUP BY username,page_title'+\
    ' ORDER BY username)'+\
    ' GROUP BY username'+\
    ' ORDER BY frequency DESC'
    cur.execute(sql_statement)
    
    ### Get first line of query results
    user_max_pages=cur.fetchone()
    
    ### Print the results
    print 'The user '+str(user_max_pages[0])+' wrote ' +str(user_max_pages[1])+' pages. This is the maximum.'
    
    ### Commit and then close connection    
    conn.commit()
    conn.close()    
if __name__=='__main__':
    main()
    
    