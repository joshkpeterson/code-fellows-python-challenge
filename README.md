code-fellows-python-challenge
=============================

Commands:

Your library can be accessed using the variable my_library. 

Number of shelves is taken via user input at runtime.

Add a book:
book('book name', shelf)
moby_dick = book('Moby Dick', 0)

Print how many shelves in the library:
my_library.num_shelves()

List all the books in the library: 
my_library.list_books()

List all the books in a single shelf: 
my_library[2].list_books()

Move the book: 
my_library[0][0].unshelf()
moby_dick.unshelf()

CAVEATS:
0-indexing for the shelves is confusing; this could be handled more nicely for the user. 

When you unshelf, you actually create an identical new book object. 
What happens to the old one?

In this library, you must enshelf after you unshelf. You don't just go laying books around.
This is to prevent a potential 'bug' where a copy of a book could be made by enshelving it again.

Requires that you run it either with python -i publiclibrary.py or with pdb.
This is because of the way I rely on global my_library. 
I don't know how to conveniently refer to the list that an object is in. 
