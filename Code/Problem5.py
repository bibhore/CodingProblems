import sys
import json


class Problem5:
    # solve the problem using map reduce
    @staticmethod
    def problem5():
        if sys.argv.__len__() is 0:
            return
        else:
            if sys.argv.__len__() is not 3:
                print('Invalid arguments')
                return

        jsonfile = sys.argv[1]
        path = sys.argv[2]
        file = open(jsonfile, 'r')
        jsonstring = json.load(file)
        dictpath = 'jsonstring'
        # convert path to dictionary format
        for val in path.split('.'):
            if val.__contains__('[') and val.__contains__(']'):
                dictpath = dictpath + '["'+val[0:val.find('[')]+'"]'+val[val.find('['):]
            else:
                dictpath = dictpath+"['"+val+"']"
        # print(jsonstring['root']['user']['username'])
        print(eval(dictpath))
        file.close()



# Problem5.problem5()
