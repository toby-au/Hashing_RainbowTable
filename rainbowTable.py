"""
Toby Au
Hw 9: Hashing and Rainbow Tables
CSC1 141
"""

from rit_lib import *
import hashlib



class RainbowTable(struct):
    """
    (str, filename): stores name of the password file used to generate the rainbow table
    (dict, table): hold passwords and be indexed by hashes
    (int, numFound): used to keep track of how many hashes have been cracked
    (int, numHashes): stores the size of the hash table
    """
    _slots = ((str, "filename"), (dict, "table"), (int, "numFound"), (int, "numHashes"))



def buildTable(filename):
    """
    key = hash
    value = pw (word)
    :param filename:
    :return:
    """
    Rtable = RainbowTable(filename, {}, 0, 0)
    file = open(filename)
    for line in file:
        pw = line.strip()
        hash = hashlib.md5(pw.encode()).hexdigest()
        Rtable.table[hash] = pw
        Rtable.numHashes += 1
    return Rtable



def crackHash(Rtable, hash):
    """
    if pw is in rainbow table, return True and the pw
    if pw is not in rainbow table, return False and "Not Found"
    :param Rtable:
    :param hash:
    :return:
    """

    hashlst = Rtable.table.keys()
    for key in hashlst:
        if key == hash:
            Rtable.numFound += 1
            return True, Rtable.table[hash]
    return False, "Not Found"



def crackFile(Rtable, filename):
    """
    filename = hashlst
    if hash is in the dictionary, return dictionary of hashes found
    return list of hashes not found
    :param Rtable:
    :param filename:
    :return: dictionary of hashes found and list of hashes not found
    """
    file = open(filename)
    lst = []
    dict = {}
    for line in file:
        hash = line.strip()
        bool, password = crackHash(Rtable, hash)
        if bool == True:
            dict[hash] = password
        else:
            lst.append(hash)
    return dict, lst

def compareTables(Rtable1, Rtable2):
    """
    returns number of shared hashes between rainbow tables
    :param Rtable1:
    :param Rtable2:
    :return:
    """
    shared = 0
    for key1 in Rtable1.table.keys():
        for key2 in Rtable2.table.keys():
            if key1 == key2:
                shared += 1
    return shared