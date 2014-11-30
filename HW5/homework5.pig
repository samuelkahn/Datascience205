----- Samuel Kahn ------
----- Homework 5 ------


----- Loads the exite-small.log file into the relation raw_log_file
raw_log_file  = LOAD 'excite-small.log' USING PigStorage('\t') AS (user, time, query);

----- Select/Filter tuples in bag that do not have query field that is empty
non_empty_query= FILTER raw_log_file BY (query!='');

---- Tuples all go into single group call group
grouped = GROUP non_empty_query ALL;

---- Count the number of non_empty Queries. This is the answer to 1A
total_queries = FOREACH grouped GENERATE COUNT(non_empty_query);

---- Tokenize each query, making each query a bag of words
tuple_tokens = FOREACH non_empty_query GENERATE TOKENIZE(query) AS tokens;

----- Create new bag with the size of each bag of words from the previosu tokenization
size_of_tuples= FOREACH tuple_tokens GENERATE SIZE(tokens) AS size_of_tokens;

---- Tuple of query sizes all go into one group
count_group= GROUP size_of_tuples ALL;

---- get max from query sizes. This is answer to 1B
max = FOREACH count_group GENERATE MAX(size_of_tuples.size_of_tokens) ;

---- get average from query size. this is answer to 1C
average  = FOREACH count_group GENERATE AVG(size_of_tuples.size_of_tokens);

---- Generate new bag where each tuple is a user
users_group= FOREACH raw_log_file GENERATE TOTUPLE(user) AS user;

---- Generate new bag with only distinct users
distinct_users= DISTINCT users_group;

---- Put all users into single group
grouped_users= GROUP distinct_users ALL;

---- Count number distinct users
total_distinct_users= FOREACH grouped_users GENERATE COUNT(distinct_users);

---- Store homework parts into respective folders

STORE total_queries INTO 'Part1A';
STORE max INTO 'Part1B';
STORE average INTO 'Part1C';
STORE total_distinct_users INTO 'Part1D';
