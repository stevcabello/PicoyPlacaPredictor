import time


class Plate:
	""" A license plate number.

	Attributes:
		plate: A string representing the license plate number.
	"""

	def __init__(self, plate):
		"""Return a Plate object whose license plate number is *plate*."""
		self.plate = plate

	def lastDigit(self):
		"""Return the last digit of the license plate number."""
		return int(self.plate[-1])


class Date:
	""" A date.

	Attributes:
		date: A string representing a date in the format dd/mm/yyyy.
	"""

	def __init__(self,date):
		"""Return a Date object whose date is *date*."""
		self.date = date

	def weekDay(self):
		"""Return a number representing a day on a week according to date.
		0:Monday .... 6:Sunday."""
		return time.strptime(self.date,'%d/%m/%Y').tm_wday

	def lastDigits(self):
		"""Return a tuple with the possible license plate's last digits
		based on the weekday according to the pico y placa regulation."""
		d1 = self.weekDay()*2+1
		d2 = (self.weekDay()*2+2)%10
		return (d1,d2)


class Time:
	""" A time.

	Attributes:
		_time: A string representing a time in the format hh:mm(am or pm).
	"""
	def __init__(self,_time):
		"""Return a Time object whose time is *_time*."""
		self._time = time.strptime(_time,'%I:%M%p')

	def hour(self):
		"""Return a number representing the hour according to _time."""
		return self._time.tm_hour

	def min(self):
		"""Return a number representing the minute according to _time."""
		return self._time.tm_min



class Predictor:
	""" Support class to check if a vehicle is restricted to road according to 
	Pico y placa regulation.

	Attributes:
		plate: A Plate object.
		date: A Date object.
		_time: A Time object (actual time to road).
		from_time_am: A Time object (lower boundary time to road in the morning).
		to_time_am: A Time object (upper boundary time to road in the morning).
		from_time_pm: A Time object (lower boundary time to road in the afternoon).
		to_time_pm: A Time object (upper boundary time to road in the afternoon).
	"""

	def __init__(self,plate,date,_time,from_time_am,to_time_am,from_time_pm,to_time_pm):
		"""Return a Predictor object"""
		self.plate = plate
		self.date = date
		self._time = _time
		self.from_time_am = from_time_am
		self.to_time_am = to_time_am
		self.from_time_pm = from_time_pm
		self.to_time_pm = to_time_pm

	def inRestriction(self,from_time,to_time):
		"""Return True if _time is between the times restricted to road; False otherwise."""
		if self._time.hour() == to_time.hour() and self._time.min() <= to_time.min():
			return True
		else:
			return from_time.hour() <= self._time.hour() < to_time.hour()
	

	def isRestricted(self):
		"""Return True if a vehicle's plate is restricted to road; False otherwise."""		
		if self.date.weekDay()>4:
			return False
		else:
			if self.inRestriction(self.from_time_am,self.to_time_am) or self.inRestriction(self.from_time_pm,self.to_time_pm):
				return self.plate.lastDigit() in self.date.lastDigits()
			return False

