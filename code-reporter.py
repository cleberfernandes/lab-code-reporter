import sys
import glob

path_arg = sys.argv[1]
filemask_arg = sys.argv[2]
str_arg = sys.argv[3]
print("args:", path_arg, filemask_arg, str_arg)

for filename in glob.iglob(path_arg + '/**/' + filemask_arg, recursive=True):
    print(filename)

    f = open(filename)
    try:
        line_list = f.readlines()
    except:
        line_list = ['n/a']
    
    print(line_list[0])
