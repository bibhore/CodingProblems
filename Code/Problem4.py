import csv
import io
import operator

class Problem4:
    # solve the problem using map reduce
    @staticmethod
    def problem4(file):
        metadelimit = {}
        metaquote = {}
        linecount = 0
        #csvReader = csv.reader(io.open(file))
        with open(file, "r") as data:
            lines = data.readlines()
            for row in lines:
                if linecount < 5:
                    # sniff only first five lines if available
                    sniffer = csv.Sniffer()
                    dialect = sniffer.sniff(row)
                    if dialect.delimiter not in metadelimit.keys():
                        metadelimit[dialect.delimiter] = 1
                    else:
                        metadelimit[dialect.delimiter] = metadelimit[dialect.delimiter] + 1
                    if dialect.quotechar not in metaquote.keys():
                        metaquote[dialect.quotechar] = 1
                    else:
                        metaquote[dialect.quotechar] = metaquote[dialect.quotechar] + 1
                    linecount = linecount + 1

            delimiter = max(metadelimit.items(), key=operator.itemgetter(1))[0]
            quote = max(metaquote.items(), key=operator.itemgetter(1))[0]
            data.seek(0)
            csvReader = csv.reader(data, delimiter = delimiter,  quotechar = quote)
            rowcount = 0
            for row in csvReader:
                #assume first row has right number of columns
                if rowcount is 0:
                    colcount = len(row)
                    rowcount = rowcount+1
                    print('Valid : ' + "\t".join(row))
                else:
                    if colcount is not len(row):
                        print('Invalid : ' + "\t".join(row))
                    else:
                        print('Valid : ' + "\t".join(row))



# Problem4.problem4('..\\resources\\problem4.txt')
