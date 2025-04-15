## What are the commonly used decoretors in python?

# classmethod example

class InstanceCounter:
    count = 0

    def __init__(self):
        # Each time an instance is crreated, increment the count
        InstanceCounter.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count
        

# Creating instance of the class

instance1 = InstanceCounter()
instance2 = InstanceCounter()
instance3 = InstanceCounter()
instance3 = InstanceCounter()
instance3 = InstanceCounter()

# Using the class method to get the instance count

total_instance = InstanceCounter.get_instance_count()

print(f"Total number of instances created: {total_instance}")