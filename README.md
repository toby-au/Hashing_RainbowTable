# Hashing_RainbowTable

The file rainbowTable consists of a class and a variety of functions that create the table and compares tables and hash-values. <br>

The file "cracker" has default passwords and result's lists. <br>

The program then creates two hash tables or "rainbow" tables consisting of: <br>
Key: generated hash values using the python hash function. <br>
Values: a dictionary (hold passwords and be indexed by hashes)<br>

There is a class object that stores: <br>
    - a filename <br>
    - a hash table <br>
    - the number of similar passwords found <br>
    - the number of similar hash values found <br>
    
Using these objects, it goes through a series of 12 tests comparing the two hash tables to see if the generated hash values reveal similar passwords. <br>

This assignment should reveal that each test returns True. 
