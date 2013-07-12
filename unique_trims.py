import MapReduce
import sys

"""
DNA unique trimming using the Simple Python MapReduce Framework

Test Input: dna.json
Test Output: unique_trims.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: the trimmed DNA string
    # value: the sequence id, which we'll never use 
    key = record[1][:-10] 
    value = record[0]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # The point here is to group all sequence with the same trimmed strings, and by doing
    # so, we can just emit the key and don't have to worry about checking duplicates ;)
    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
