import numpy as np
import collections

def test1():
    s1 = [0, 0, 0, 0]
    s2 = np.zeros(4)

    s3 = np.resize(s1, (2, 2))
    print(s3)
    print(type(s3))

    if(collections.Counter(s1) == collections.Counter(s2)):
        print('Они равны!')

    print('type(s1) = ', type(s1))
    print('type(s2) = ', type(s2))
    print(type(list(s2)))

    s1.append(0)
def test2():
    test_num = 0
    res = [int(i) for i in list('{0:0b}'.format(test_num))]
    print("The converted binary list is : " + str(res))

# test1()
test2()