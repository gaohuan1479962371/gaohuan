import os,sys

# pwd print working directory
path = os.getcwd()   # current working directory
print('path=',path)
print('系统路径：',sys.path)

sys.path.append(path)
print('系统路径：',sys.path)
