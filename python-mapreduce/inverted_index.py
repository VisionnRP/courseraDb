import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    lst = []
    for v in list_of_values:
        if v not in lst:
            lst.append(v)
    mr.emit((key, lst))


inputdata = open(sys.argv[1])

mr.execute(inputdata, mapper, reducer)
