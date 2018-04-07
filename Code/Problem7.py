import random
import time

class Problem7:

    def printrandom(self):
        for i in range(10):
            print(random.randint(1,100))
        time.sleep(random.randint(0,1))

    def problem7(self):
        starttime = time.time()
        self.printrandom()
        endtime = time.time()
        print('Total elapsed time : '+str(endtime - starttime))



# problem7 = Problem7 ()
# problem7.problem7()