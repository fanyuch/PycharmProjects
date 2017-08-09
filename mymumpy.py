import numpy as np

print(np.array([x for x in range(10)]), [x for x in range(10, 20)])

print(np.array([x for x in range(10)], dtype=np.int32))

print(np.arange(15).reshape(3,5))

print(np.arange(15).reshape(5,3))

print(np.linspace(1, 3, 7))

print(np.zeros((3, 4)))

print(np.ones((3, 4)))

print(np.ones((3, 4)).shape)

m_array = np.array(([1, 3, 4, 5],
         [3, 5, 6, 7, 9],
         [3, 5, 6, 8],
         [2, 4]))

# print(np.shape(m_array))
print(m_array)


# import random
# m_list = random.sample([x for x in range(0, 20000)], 10000)
# random.shuffle(m_list)
# new_list = sorted(m_list)
#
# x = input()
# j = 0
# for i in new_list:
#     if x == i:
#         break
#     else:
#         j += 1


import pickle
value1 = {'id':410103198558963321,
         'name':'zhagnsan',
         'sex':'male',
         'area':'nanyang'}

value2 = {'id':410103198658963321,
         'name':'zhagnsan',
         'sex':'male',
         'area':'nanng'}

m_list = list()
m_list.append(value1)
m_list.append(value2)

with open('in.txt', 'wb') as f:
    pickle.dump(m_list, f)

new_list = list()
with open('in.txt', 'rb') as f:
    new_list = pickle.load(f)

with open('henan', 'wb') as f:
    for l in new_list:
        if 'henan' in l['area']:
            pickle.dump(l, f)

with open('man', 'wb') as f:
    for l in new_list:
        if l['sex'] == 'male':
            pickle.dump(l, f)


pass