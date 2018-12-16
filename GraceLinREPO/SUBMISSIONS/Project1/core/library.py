from core.book import Book
import pickle

class Library:
    def __init__(self, library_id, library_name):
        self.__library_id = library_id
        self.__library_name = library_name
        self.__db_location = 'db/book_db.pkl'
        _init_db = {}
        self.__dump_book_db(_init_db)
        
    def register_book(self, book_id = None, book_name = None, author = None):
        if not book_id or not book_name or not author:
            print("Please enter book_id, book_name and author")
            return
        book_db = self.__load_book_db()
        if book_id in book_db.keys():
            print("Book {0} already registered!".format(book_id))
            return
        
        new_book = Book(book_id, book_name, author)
        book_db[book_id] = new_book
        self.__dump_book_db(book_db)
        print("SUCCESS: Book {} registered!".format(book_id))
        print("#### INFO ####")
        self.__print_book_info(new_book)
        print("#############")

    def purge_book(self, book_id):
        book_db = self.__load_book_db()
        if book_id in book_db:
            book_db.remove(book_id)
            self.__dump_book_db(book_db)
            print("SUCCESS: book {} is removed!".format(book_id))
        else:
            print("FAIL: book {} is not found!".format(book_id))

    def get_library_name(self):
        return self.__library_name

    def set_library_name(self, new_name):
        self.__library_name = new_name

    def __load_book_db(self):
        with open(self.__db_location, 'rb') as f:
            return pickle.load(f)
    
    def __dump_book_db(self, book_db):
        with open(self.__db_location, 'wb') as f:
            pickle.dump(book_db, f)
    
    def search_book(self, book_id = None, book_name = None, author = None):
        if book_id:
            book = self.__search_book_by_id(book_id)
            if book:
                print("#### INFO ####")
                self.__print_book_info(book)
                print("#############")
        elif book_name or author:
            books_list = self.__search_book_by_name(book_name) + self.__search_book_by_author(author)
            if len(books_list) > 0:
                print("Below are accounts satisfying search keywords")
                for book in books_list:
                    print("#### INFO ####")
                    self.__print_book_info(book)
                    print("#############")
            else:
                print("No book satisfying keywords in search")
        else:
            print("please enter keywords for search")
            return

    def get_book(self, book_id):
        if book_id:
            return self.__search_book_by_id(book_id, False)
   
    def update_book_status(self, book_id, status):
        book_db = self.__load_book_db()
        if book_id in book_db:
            book = book_db[book_id]
            book.set_status(status)
            self.__dump_book_db(book_db)

    def __search_book_by_id(self, book_id, verbose = True):
        book_db = self.__load_book_db()
        if book_id in book_db:
            if verbose:
                print("SUCCESS: Book {} is found!".format(book_id))
            return book_db[book_id]
        else:
            if verbose:
                print("FAIL: Book {0} is not found!".format(book_id))
            return
    
    def __search_book_by_name(self, book_name):
        re = []
        if not book_name:
            return re
        
        book_db = self.__load_book_db()
        
        for key in book_db:
            book = book_db[key]
            if book.get_book_name() == book_name: ## this can be exactly match or fuzzy match
                re.append(book)
        return re

    def __search_book_by_author(self, author):
        re = []
        if not author:
            return []

        book_db = self.__load_book_db()
        
        for key in book_db:
            book = book_db[key]
            if book.get_author() == author: ## this can be exactly match or fuzzy match
                re.append(book)
        return re

    def __print_book_info(self, book):
        book_id = book.get_book_id()
        book_name = book.get_book_name()
        author = book.get_author()
        status = "Available" if book.get_status() else "Not Available"
        print("Book id: {0}\nBook Name: {1}\nBook Author: {2}\nBook Status: {3}".format(book_id, book_name, author, status))
        