import random
import string

lis = []
x = 0
valid = 1
newset = ""


#Function that Generates the new password
def pas():
    length = int(input("How many charictors do you want? "))
    for x in range(length):
        if random.randint(0,1) == 1:
            lis.append(random.randint(0,9))
        else: 
            lis.append(random.choice(string.ascii_letters))
    
pas()

#Function that Prints the password
def passw():
    str_join = "".join(str(x) for x in lis)
    print ("Your New Password Is:","\n",str_join)
    input("Press Enter to close!")

passw()
