#!/usr/bin/python

def ExtendList1(val, list=[]):
    list.append(val)
    return list

def ExtendList2(val):
    list = []
    list.append(val)
    return list

print "From the interview:"
list1=ExtendList1(10)       #list is global
list2=ExtendList1(123,[])
list3=ExtendList1('a')      #list is global, not 100% sure why the default list=[] parameter 
                            #doesn't overwrite the global list making the global list an empty list again??? 
print list1
print list2
print list3

print ""
print "My experiment:"
list1=ExtendList2(10)
list2=ExtendList2(123)
list3=ExtendList2('a')
print list1
print list2
print list3

print "Interesting! If the list is created as a default parameter value it is global!! dangerous!!!"
print "I would have thought it would be local to the function. I won't forget this."
print ""
print "Thank you for the Interview!"
