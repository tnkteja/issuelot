from __future__ import division
import math

class Db(object):

	def __int__(self,db):
		self.db=db
		self.value = 10**(self.db/10)

class Channel(object):
	"""docstring for Channel"""
	
	def __init__(self, bw, sr, snr=Db(40)):
		super(Channel, self).__init__()
		self.bw,self.sr,self.snr=bw,sr or 2*bw,snr
		self.maxCapacity= (self.snr/2)*math.log(1+snr.value,2)

	def getMaxBitRate():
		"""Using shanons channel theorem"""
		return 
		
