import py27elec as elec

pe = elec.Py27elec()\


V = 24 
i1 = pe.i_by_vr( V, 9.0 )
print "i1 = %f" % i1

i2 = pe.i_by_vr( V, 6.0 )
print "i2 = %f" % i2

i3 = pe.i_by_vr( V, 3.0 )
print "i3 = %f" % i3

i1to3 = i1+i2+i3 
print "i1to3 = %f" % i1to3

