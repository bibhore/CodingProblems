

class Problem6:
    # solve the problem using map reduce
    @staticmethod
    def problem6():
        X = [1, 6, 3, 4, 8, 9, 4, 2, 5, 7, 60, 10]
        even = [x for x in X if x % 2 is 0]
        print(even)
        print(sorted(even, key=int))

# Problem6.problem6()
