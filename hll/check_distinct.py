from HLL import HyperLogLog
from python_examples.pythoncookbook.section1.generate_rand import gen

hll = HyperLogLog(5) # use 2^5 registers

for i in gen():
    print(i)
hll.add('some data')

estimate = hll.cardinality()
