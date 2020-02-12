#
# generate data for numbers experiment
#
import os

# setup paths and filename
dirpath = os.getcwd()
datapath = dirpath + '\\data'
addh = datapath + '\\addh.csv'
addm = datapath + '\\addm.csv'
adds = datapath + '\\adds.csv'
numh = datapath + '\\numh.csv'
numm = datapath + '\\numm.csv'
nums = datapath + '\\nums.csv'
remain = datapath + '\\remain.csv'

# 1. Attributes for add hour relationship
# start with numh 0-23
# need variables 
# - addee - the base integer 
# - addor - the integer being added,
# - resnum - the result of the addition (integer),
# - remres - the result (integer) if a remainder is carried from a previous addition , 
# - resrem - the (boolean) of whether a remainder is left over from the addition, 
# - remrem - the (boolean) of whether a remainder is left over from the addition, where a remainder is carried from a previous addition
#
myline1 = 'addee, addor, resnum, remres, remnum, remrem'+'\n'
with open(addh,'a') as out_file:
        out_file.write(myline1)

num = 24

for i in range(num):
    addee = i
    for j in range(num):
        addor = j
        resnum = i+j
        remres = resnum + 1
        if (resnum >(num-1)):
            resnum = resnum - num
            resrem = 'true'
        else:
            resrem = 'false'

        if (remres >(num-1)):
            remres = remres - num
            remrem = 'true'
        else:
            remrem = 'false'
        #####
        # deal with single digits
        ########
        if(addee<10):
            addeet = '0' + str(addee)
        else:
            addeet = str(addee)

        if(addor<10):
            addort = '0' + str(addor)
        else:
            addort = str(addor)
        
        if(resnum<10):
            resnumt = '0' + str(resnum)
        else:
            resnumt = str(resnum)

        if(remres<10):
            remrest = '0' + str(remres)
        else:
            remrest = str(remres)
        
        myline2 = addeet + ', ' + addort + ', ' + resnumt + ', ' + remrest + ', ' + resrem + ', ' + remrem +'\n'
        with open(addh,'a') as out_file:
            out_file.write(myline2)



# 2. Attributes for add minute relationship
# start with numm 0-59
# need variables 
# - addee - the base integer 
# - addor - the integer being added,
# - resnum - the result of the addition (integer),
# - remres - the result (integer) if a remainder is carried from a previous addition , 
# - resrem - the (boolean) of whether a remainder is left over from the addition, 
# - remrem - the (boolean) of whether a remainder is left over from the addition, where a remainder is carried from a previous addition
#
myline1 = 'addee, addor, resnum, remres, remnum, remrem'+'\n'
with open(addm,'a') as out_file:
        out_file.write(myline1)

num = 60

for i in range(num):
    addee = i
    for j in range(num):
        addor = j
        resnum = i+j
        remres = resnum + 1
        if (resnum >(num-1)):
            resnum = resnum - num
            resrem = 'true'
        else:
            resrem = 'false'

        if (remres >(num-1)):
            remres = remres - num
            remrem = 'true'
        else:
            remrem = 'false'
        #####
        # deal with single digits
        ########
        if(addee<10):
            addeet = '0' + str(addee)
        else:
            addeet = str(addee)

        if(addor<10):
            addort = '0' + str(addor)
        else:
            addort = str(addor)
        
        if(resnum<10):
            resnumt = '0' + str(resnum)
        else:
            resnumt = str(resnum)

        if(remres<10):
            remrest = '0' + str(remres)
        else:
            remrest = str(remres)
        
        myline2 = addeet + ', ' + addort + ', ' + resnumt + ', ' + remrest + ', ' + resrem + ', ' + remrem +'\n'
        with open(addm,'a') as out_file:
            out_file.write(myline2)

# 3. Attributes for add seconds relationship
# start with nums 0-59
# need variables 
# - addee - the base integer 
# - addor - the integer being added,
# - resnum - the result of the addition (integer),
# - remres - the result (integer) if a remainder is carried from a previous addition , 
# - resrem - the (boolean) of whether a remainder is left over from the addition, 
# - remrem - the (boolean) of whether a remainder is left over from the addition, where a remainder is carried from a previous addition
#
myline1 = 'addee, addor, resnum, remres, remnum, remrem'+'\n'
with open(adds,'a') as out_file:
        out_file.write(myline1)

num = 60

for i in range(num):
    addee = i
    for j in range(num):
        addor = j
        resnum = i+j
        remres = resnum + 1
        if (resnum >(num-1)):
            resnum = resnum - num
            resrem = 'true'
        else:
            resrem = 'false'

        if (remres >(num-1)):
            remres = remres - num
            remrem = 'true'
        else:
            remrem = 'false'
        #####
        # deal with single digits
        ########
        if(addee<10):
            addeet = '0' + str(addee)
        else:
            addeet = str(addee)

        if(addor<10):
            addort = '0' + str(addor)
        else:
            addort = str(addor)
        
        if(resnum<10):
            resnumt = '0' + str(resnum)
        else:
            resnumt = str(resnum)

        if(remres<10):
            remrest = '0' + str(remres)
        else:
            remrest = str(remres)
        
        myline2 = addeet + ', ' + addort + ', ' + resnumt + ', ' + remrest + ', ' + resrem + ', ' + remrem +'\n'
        with open(adds,'a') as out_file:
            out_file.write(myline2)


# 4. Hour Attributes 
# numh 0-24, 
#
myline1 = 'num'+'\n'
with open(numh,'a') as out_file:
        out_file.write(myline1)

num = 24

for i in range(num):
    #####
    # deal with single digits
    ########
    if(i<10):
        it = '0' + str(i)
    else:
        it = str(i)

    myline2 = it + '\n'
    with open(numh,'a') as out_file:
            out_file.write(myline2)

# 5. Minute Attributes 
# numm 0-59, 
#
myline1 = 'num'+'\n'
with open(numm,'a') as out_file:
        out_file.write(myline1)

num = 60

for i in range(num):
    #####
    # deal with single digits
    ########
    if(i<10):
        it = '0' + str(i)
    else:
        it = str(i)

    myline2 = it + '\n'
    with open(numm,'a') as out_file:
            out_file.write(myline2)

# 5. Secods Attributes 
# nums 0-59, 
#
myline1 = 'num'+'\n'
with open(nums,'a') as out_file:
        out_file.write(myline1)

num = 24

for i in range(num):
    #####
    # deal with single digits
    ########
    if(i<10):
        it = '0' + str(i)
    else:
        it = str(i)

    myline2 = it + '\n'
    with open(nums,'a') as out_file:
            out_file.write(myline2)

# 6. Remainder Attributes 
# does the addition have a remainder
# # remrem true-false, 
#
myline1 = 'rem'+'\n'
with open(remain,'a') as out_file:
        out_file.write(myline1)

myline2 = 'true' + '\n'
with open(remain,'a') as out_file:
        out_file.write(myline2)

myline3 = 'false' + '\n'
with open(remain,'a') as out_file:
        out_file.write(myline3)

      
    