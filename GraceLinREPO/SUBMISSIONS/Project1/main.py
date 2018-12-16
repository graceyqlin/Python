from core.admin import Admin
from core.library import Library

def init():
	lib = Library("L000001", "Grace Library")
	admin = Admin(lib)
	return admin, lib

def main():
	admin, lib = init()
	
	print("TEST library register book")
	lib.register_book(book_id = 'b001', book_name = 'Little fire everywhere', author = 'Celeste')
	lib.register_book(book_id = 'b002', book_name = 'Computer History', author = 'Bob')
	print("")
	
	print("TEST library search book")
	
	print("TODO: search book by id")
	lib.search_book(book_id = 'b003')
	lib.search_book(book_id = 'b001')
	
	print("TODO: search book by name")
	lib.search_book(book_name = 'Little fire everywhere')
	
	print("TODO: search book by author")
	lib.search_book(author = 'Bob')
	print("")

	print("TEST admin register account")
	admin.register_account(account_id = 'a001', account_name = 'grace')
	admin.register_account(account_id = 'a002', account_name = 'joyce')
	print("")

	print("TEST admin search account")
	
	print("TODO: search account by id")
	admin.search_account(account_id = 'a001')
	admin.search_account(account_id = 'aaa')
	
	print("TODO: search account by name")
	admin.search_account(account_name = 'joyce')
	print("")

	print("TEST admin borrow book")
	print("TODO: Borrow book b001 for the first time")
	admin.borrow_book(book_id = 'b001', account_id = 'a001', datetime = '2018-07-08')
	
	print("TODO: Check account a001 history")
	admin.search_account(account_id = 'a001')
	
	print("TODO: Check book b001 status")
	lib.search_book(book_id ='b001')

	print("TODO: Borrow book b001 for the second time")
	admin.borrow_book(book_id = 'b001', account_id = 'a001', datetime = '2018-07-08')
	
	print("TODO: Borrow book b002 for the first time")
	admin.borrow_book( book_id = 'b002', account_id = 'a001', datetime = '2018-07-08')
	
	print("TODO: Check account a001 history")
	admin.search_account(account_id = 'a001')
	print("")

	print("TEST admin return book")
	admin.return_book(book_id = 'b001', account_id = 'a001', datetime = '2018-07-08')
	
	print("TODO: Check book b001 status")
	lib.search_book(book_id = 'b001')
	
	print("TODO: Check account a001 history")
	admin.search_account(account_id = 'a001')
	
	print("TODO: Borrow book b001 again")
	admin.borrow_book(book_id = 'b001', account_id = 'a002', datetime ='2018-07-08')
	
	print("TODO: Check account a002 history")
	admin.search_account(account_id = 'a002')
	print("")

main()