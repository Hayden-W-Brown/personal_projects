size_num = 10
for x in range(size_num):
    line = "*"*x
    line = line+" "*((size_num*2)-(x*2))
    line = line+"*"*x
    print(line)
