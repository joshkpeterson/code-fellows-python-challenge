import pdb 

def main():
	global my_library
	my_library = library(3)


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

	current_shelf = None

	def __init__(self, book_name, shelf):
		name = book_name
		pdb.set_trace();
		self.enshelf(name, shelf)

	def enshelf(self, book_name, shelf):
		#if they dont give a shelf, prompt them for a shelf

		pdb.set_trace();

		num_shelves = my_library.num_shelves()

		#if library contains shelf:
		if num_shelves > (shelf):
			my_library[shelf].append(book_name)
			current_shelf = shelf;
			print book_name + ' is currently on shelf ' + str(current_shelf) + '.' 
		else:
			print 'The library only has ' + str(num_shelves) + ' shelves.'
		 
		
main()

pdb.set_trace();
