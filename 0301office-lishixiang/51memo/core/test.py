# import os
# import sys

# abspath = os.path.abspath(__file__)
# print('abs', abspath)

# dirname = os.path.dirname(__file__)
# print('dir', dirname)

# basename = os.path.basename(__file__)
# print('base', basename)

# dirabs = os.path.dirname(os.path.abspath(__file__))
# print('dirabs', dirabs)

# boo = os.path.exists(r'C:\abc')
# print(boo)

# path = os.path.abspath(os.path.join(dirabs, "..", "db"))
# print(path)
# # with open(os.path.join(path, 'test.txt'), 'w') as f:
# #     f.write('test')

# a = os.path.abspath(os.path.dirname(dirabs))
# print('a', a)

# b = os.path.abspath(os.path.dirname(__file__))
# print('b', b)

# c = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print('c', c)

def test():
    print(__file__)
    print('rum in test.py')

# print(sys.path)