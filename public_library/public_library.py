import pdb 

def main():
	global my_library
	print 'Welcome to the virtual Library-o-matic.'
	shelves = input('How man shelves would you like: ')
	my_library = library(shelves)
	print 'Ok, here\'s a library with ' + str(shelves) + ' shelves.'

class library(list): 
	def __init__(self, shelves):
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
	current_shelf = None

	def __init__(self, book_name, shelf):
		name = book_name
		num_shelves = my_library.num_shelves()
		while ( shelf > (num_shelves - 1) ):
			print 'The library only has ' + str(num_shelves) + ' shelves.'
			shelf = input('Pick a different shelf: ')
		self.enshelf(name, shelf)
			


	def enshelf(self, book_name, shelf):
		my_library[shelf].append(book_name)
		current_shelf = shelf;
		print book_name + ' is currently on shelf ' + str(current_shelf) + '.' 
		
		
main()

pdb.set_trace();
