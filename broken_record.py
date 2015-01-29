# "Broken Record" in Python 2.7

class Record():
    def __init__(self, the_truth):
        self.broken = the_truth

my_record = Record(True)

while my_record.broken:
    print "Hello, World!"
