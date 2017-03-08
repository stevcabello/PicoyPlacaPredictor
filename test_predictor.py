from predictor import *
import unittest


class TestPicoyPlacaPredictor(unittest.TestCase):

	def testOne(self):
		self.assertTrue(predictor1.isRestricted())

	def testTwo(self):
		self.assertFalse(predictor2.isRestricted())



def main():
	unittest.main()


if __name__ == '__main__':

	#Set the lower and upper road time boundaries according to Pico y Placa regulation.
	from_time_am = Time('7:00am')
	to_time_am = Time('9:30am')
	from_time_pm = Time('4:00pm')
	to_time_pm = Time('7:30pm')

	#Set two different license plate numbers
	plate1 = Plate('GHZ-2334')
	plate2 = Plate('GHZ-2335')

	date = Date('07/03/2017')
	_time = Time('6:30pm')


	predictor1 = Predictor(plate1,date,_time,from_time_am,to_time_am,from_time_pm,to_time_pm)
	predictor2 = Predictor(plate2,date,_time,from_time_am,to_time_am,from_time_pm,to_time_pm)

	main()


