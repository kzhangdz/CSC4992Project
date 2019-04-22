
from book import Book



try:
	book1 = Book("Too Many Houses", 2008, 562)
	book1.new_release(2010, 565)
	book1.new_release(2014, 568)
	book1.new_release(2016)
	book1.new_release(2018, 570)
	book1.print_info()
	print()
	book1.print_info(2014)
	
	#test exceptions
	book1.new_release(2014)
	book1.print_info(2012)
	
except KeyError as excpt:
	print()
	print("Error with versions: ", end = " ")
	print(excpt)