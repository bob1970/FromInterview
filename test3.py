#!/usr/bin/python

print "From Interview:"
list = [[]] * 5
print list
list[0].append(10)
print list
list[1].append(20)
print list
list.append(30)
print list

print ""

print "my experiment:"
list = [[], [], [], [], []] #this is the only difference
print list
list[0].append(10)
print list
list[1].append(20)
print list
list.append(30)
print list

print ""
print "aha... [[]] * 5 produces a list of 5 references to the SAME list!!!"

