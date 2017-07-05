class Py27elec:
	def __init__(self):
		print "py27elec init";
		pass

	# calculate r sequnece , 
	def r_seq( self, arr ):
		sum = 0.0
		for x in arr:
			sum += x 
		return sum   					# ohm  

	#calculate r parallel
	def r_para( self, arr ):
		sum = 0.0
		for x in arr:
			sum += 1/x 
		rev1 = 1/sum
		return rev1						# ohm  

	def i_by_vr(self, v ,r ):
		return v / r 					# Ampare

	def v_by_ir(self, i ,r ):
		return i *  r 					# Volt

if __name__ == "__main__" : 
	p27e = Py27elec()
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

	#V = p27e.v_by_ir( 2.0 / 1000, 4500.0 )
	V = p27e.v_by_ir(  i  ,  r4s )
	print "V = %f" % V 	

