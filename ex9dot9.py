import py27elec as elec

p27e = elec.Py27elec()
r1s = p27e.r_seq([7.0 ,2.0])
r2 = 5.0
r1p2 = p27e.r_para( [ r2,r1s])
r3s =  p27e.r_seq( [ 3.0,r1p2,4.0])
print "r1s = %f" % r1s
print "r1p2 = %f" % r1p2
print "r3s = %f" % r3s

r3p =  p27e.r_para( [ 1,r3s])
print "r3p = %f" % r3p
r4s = p27e.r_seq( [0.6,6.0,r3p ])
print "r4s = %f" % r4s

i  = p27e.i_by_vr(5.0,r4s)
print "i = %f" % i 
