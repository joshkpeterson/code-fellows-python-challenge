import pdb 

class library(list): 
	def __init__(self, shelves):
		# super(library, self).__init__([shelf()])
		for x in range(shelves):
			list.append(self, shelf())

	def num_shelves(self): 
		return len(self)

class shelf(list): 
	def __init__(self):
		super(shelf, self).__init__([])


	def list_books(self):
		# if not self:
		# 	print "Shelf is empty" 
		for book in self: 
			print book.name

class book():
	name = ""
	#current_shelf = None

	def __init__(self, book_name, shelf):
		name = book_name
		pdb.set_trace();
		self.enshelf(name, shelf)

	def enshelf(self, book_name, shelf):
		#if they dont give a shelf, prompt them for a shelf

		#if library contains shelf:
		if library.count(shelf) == 1:
			#put this in a method?
			library[shelf].append(book_name) 
		else:
			#shelf 
			library[shelf].append(book_name)
		current_shelf = shelf; 
		print book_name + " is currently on shelf " + current_shelf


pdb.set_trace();
