import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    mr.emit_intermediate(record[1], record)


def initReducer(list):
    for order_records in list:
        if order_records[0] == 'order':
            for lines in list:
                if lines[0] == 'line_item':
                    mr.emit(order_records + lines)


def reducer(initList):
    initReducer(initList)


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
