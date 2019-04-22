
class Book:
	def __init__(self, title, year, pages):
		self.title = title.title()
		self.release = {1: year}
		self.num_pages = [pages]
	
	def new_release(self, year, pages = None):
		if year in self.release.values():
			# KeyError (raised when a key is not found in a dictionary) as placeholder
			raise KeyError('year already listed')
		
		self.release[len(self.release) + 1] = year
		
		if pages is None:
			self.num_pages.append(self.num_pages[-1])
		else:
			self.num_pages.append(pages)
	
	def print_info(self, year = None):
		if year is None:
			ver = max(self.release, key=self.release.get)
		elif year not in self.release.values():
			# KeyError (raised when a key is not found in a dictionary) as placeholder
			raise KeyError('year is not listed')
		else:
			for key, value in self.release.items():
				if year == value:
					ver = key
					break
		
		print("%s:" % self.title)
		print("   Version %d released in %d" % (ver, self.release[ver]))
		print("   %d pages" % self.num_pages[ver - 1])