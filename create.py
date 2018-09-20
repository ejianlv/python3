import random

for k in range(0,200):
    i = random.randint(1,99)
    j = random.randint(1,99)
    #print("{0}".format(i).rjust(2))
    print("{0}".format(i).rjust(2),"+".rjust(1),"{0}".format(j).rjust(2),"= (    )   ".rjust(2),end=" ")    
    if i > j:
        print("{0}".format(i).rjust(2),"-".rjust(1),"{0}".format(j).rjust(2),"= (    )".rjust(2))
    else:
        print("{0}".format(j).rjust(2),"-".rjust(1),"{0}".format(i).rjust(2),"= (    )".rjust(2))
    print("")

