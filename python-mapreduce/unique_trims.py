import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(record[1][:-10], None)


def reducer(key):
    mr.emit(key)


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
