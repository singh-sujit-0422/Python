# 2. Unique Object Counter
# Problem:
# Design a class Tracker that counts how many times objects of that class are created.

# Hint: Use a class variable (not instance) to track object count.


class Tracker:

    object_count = 0


    def __init__(self):
        self.__class__.object_count = self.__class__.object_count + 1
    

    def current_object_count(self):
        return f'Total {self.__class__.object_count} objects have been created so far'


t1 = Tracker()
t2 = Tracker()
t3 = Tracker()
t4 = Tracker()

print(t4.current_object_count())

