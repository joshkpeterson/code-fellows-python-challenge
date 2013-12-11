import pdb 

class library(list): 
	def __init__(self):
		pass 
		#library[0] = shelf

	def num_shelves(self): 
		return len(self)

class shelf(list): 
	def __init__(self):
		pass

	def list_books(shelf):
		for book in shelf: 
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
		if False:
			#put this in a method?
			library[shelf].append(book_name) 
		else:
			#shelf 
			library[shelf].append(book_name)
		current_shelf = shelf; 
		print book_name + " is currently on shelf " + current_shelf


pdb.set_trace();
