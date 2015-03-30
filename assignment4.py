#!/usr/bin/env python

bowler = 'Kade'
average = 180
game1 = 83
game2 = 50
game3 = 66
newavg = (game1 + game2 + game3) / 3
age = 33
kilos = 70
def convert_weight (x):
	convert = 2.2
	pounds = x * convert
	return pounds
	
status = 'Legend'
bowling_status = 'Trash'
expo = 5**18

print "Our bowler's name is", bowler
print "Normally, his bowling average is", average, ", but tonight it was", newavg, "."
print "His scores tonight were %d, %d, and %d." % (game1, game2, game3)
print "(If you divide the total of those games by three, you will find the average)"
print "Did I mention that %s is a %s?" % (bowler, status)
print "He lost over %d kilograms!" % kilos
print "thats about", convert_weight(70), "pounds!!"
print "he may be a %s, but his bowling is still %s." % (status, bowling_status)
print "five to the eighteenth power is %d" % expo
