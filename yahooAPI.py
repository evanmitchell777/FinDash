#This needs to write to a file. This file will then be read by the C++ program
def fetch(heapFile):
    with open(heapFile) as file:
        requests = file.readlines()
        
