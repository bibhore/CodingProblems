import io
from functools import reduce


class Problem3:
    # solve the problem using map reduce
    @staticmethod
    def problem3():
        dict = {}
        with io.open('..\\resources\\problem3.txt') as input:
            content = input.readlines()
            content = [c.strip() for c in content]
            for line in content:
                try:
                    dict[line] = dict[line] + 1
                except:
                    dict[line] = 1
        for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
            print("%s %s" % (value, key))

# Problem3.problem3()
