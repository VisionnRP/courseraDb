import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(hash(record[0]) + hash(record[1]), record)


def reducer(list_of_values):
    if len(list_of_values) == 1:
        mr.emit((list_of_values[0][0], list_of_values[0][1]))
        mr.emit((list_of_values[0][1], list_of_values[0][0]))


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
