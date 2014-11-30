"""Find users who have edited more than 2 pages.

This program will take a CSV data file and output tab-seperated lines of

    user -> number of page edits

To run:

    python top_users.py page_users.txt
    
Output:

"108"	3
"11292982"	3
"372693"	10
"8889502"	5
    
"""

from mrjob.job import MRJob
import sys
 
 
class TopUsers(MRJob):

    def mapper(self, line_no, line):
        """Extracts the users from the lines"""
        cells = line.split('\t')
        yield ### FILL IN    
              # What  Key, Value  do we want to output?

    def reducer(self, user, counts):
        """Sumarizes the user counts by adding them together. """       
        total = ### FILL IN
                # How do we calculate the total users from the counts?
        if total > 2:
            yield ### FILL IN
                # What  Key, Value  do we want to output?

        
if __name__ == '__main__':
    TopUsers.run()
