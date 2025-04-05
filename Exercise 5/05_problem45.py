
#3 What is monkey patching?
'''
Monkey patching is replace a function object with a new function object, so that the function is now pointing to new function object. Mostly used when you want to replace a function for testing pourpose.
'''

class Test:
    def __init__(self, x):
        self.a = x
    def get_data(self):
        print("Send code to fetch data from database")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()

t1 = Test(4)
print("Before Monkey Fatching\n ")
t1.f1()
t1.f2()
def get_new_data(self):
    print("Some to code fatch data from test data")
Test.get_data = get_new_data
print("\nAfter Monkey Patching\n")
t1.f1()
t1.f2()