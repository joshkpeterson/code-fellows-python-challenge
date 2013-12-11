# Requires that you run it either with python -i publiclibrary.py or with pdb
import pdb 

def main():
	global my_library
	print 'Welcome to the virtual Library-o-matic.'
	shelves = input('How man shelves would you like: ')
	my_library = library(shelves)
	print 'Ok, here\'s a library called my_library with ' + str(shelves) + ' shelves.'

	# For debug
	# book('foo', 2)
	# book('goo', 2)	
	# book('poo', 2)

class library(list): 
	def __init__(self, shelves):
		for x in range(shelves):
			list.append(self, shelf())

	def num_shelves(self): 
		return len(self)

	def list_books(self):
		for i, shelf in enumerate(self):
			if shelf: 
				print 'Shelf ' + str(i) + ':'
				shelf.list_books()

class shelf(list): 
	def __init__(self):
		super(shelf, self).__init__([])


	def list_books(self):
		if not self:
			print "Shelf is empty." 
		for book in self: 
			print book.book_name

class book():
	current_shelf = None
	book_name = ''

	def __init__(self, book_name, shelf):
		self.book_name = book_name
		self.enshelf(book_name, shelf)
		
	def _enshelf(self, book_name, shelf):
		num_shelves = my_library.num_shelves()
		while ( shelf > (num_shelves - 1) ):
			print 'The library only has ' + str(num_shelves) + ' shelves.'
			shelf = input('Pick a different shelf: ')
		my_library[shelf].append(self)
		self.current_shelf = shelf;
		print book_name + ' is currently on shelf ' + str(self.current_shelf) + '.' 
		
	def unshelf(self):
		my_library[self.current_shelf].remove(self)
		shelf = input('What would you like the new shelf to be?')
		self.enshelf(self.book_name, shelf)

main()

# Commands:
# 
# Your library can be accessed using the variable my_library. 
# 
# Number of shelves is taken via user input at runtime.
# 
# Add a book:
# book('book name', shelf)
# moby_dick = book('Moby Dick', 0)
# 
# Print how many shelves in the library:
# my_library.num_shelves()
# 
# List all the books in the library: 
# my_library.list_books()
# 
# List all the books in a single shelf: 
# my_library[2].list_books()
# 
# Move the book: 
# my_library[0][0].unshelf()
# moby_dick.unshelf()
# 
# CAVEATS:
# 0-indexing for the shelves is confusing; this could be handled more nicely for the user. 
# 
# When you unshelf, you actually create an identical new book object. 
# What happens to the old one?
# 
# In this library, you must enshelf after you unshelf. You don't just go laying books around.
# This is to prevent a potential 'bug' where a copy of a book could be made by enshelving it again.
# 
# Requires that you run it either with python -i publiclibrary.py or with pdb.
# This is because of the way I rely on global my_library. 
# I don't know how to conveniently refer to the list that an object is in. 


# pdb.set_trace();
