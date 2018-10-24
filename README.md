# Hashing_RainbowTable

The file rainbowTable consists of a class and a variety of functions that create the table and compares tables and hash-values. 

The file "cracker" has default passwords and result's lists. 

The program then creates two hash tables or "rainbow" tables consisting of:
Key: generated hash values using the python hash function.
Values: a dictionary (hold passwords and be indexed by hashes)

There is a class object that stores: 
    - a filename 
    - a hash table
    - the number of similar passwords found
    - the number of similar hash values found. 
    
Using these objects, it goes through a series of 12 tests comparing the two hash tables to see if the generated hash values reveal similar passwords. 

This assignment should reveal that each test returns True. 
