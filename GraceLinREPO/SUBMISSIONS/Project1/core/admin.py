import pickle
from core.account import Account

class Admin:
    
    def __init__(self, lib):
        self.__db_location = 'db/account_db.pkl'
        _init_db = {}
        self.__dump_account_db(_init_db)
        self._lib = lib
    
    def register_account(self, account_id = None, account_name = None):
        ## account_id must be unique
        ## account_name allow duplicates

        if not account_id or not account_name:
            print("FAIL: Please enter account_id and account_name!\n")
            return
        account_db = self.__load_account_db()
        if account_id in account_db.keys():
            print("FAIL: Account ID {0} already used!\n".format(account_id))
            return 
        
        new_account = Account(account_id, account_name)
        account_db[account_id] = new_account
        self.__dump_account_db(account_db)
        print("SUCCESS: Account {} registered!\n".format(account_id))
        print("#### INFO ####")
        self.__print_account_info(new_account)
        print("#############")
    
    def purge_account(self, account_id):
        account_db = self.__load_account_db()
        if account_id in account_db:
            account_db.remove(account_id)
            self.__dump_account_db(account_db)
            print("SUCCESS: account {} is removed!\n".format(account_id))
        else:
            print("FAIL: account {} is not found!\n".format(account_id))

    def __load_account_db(self):
        with open(self.__db_location, 'rb') as f:
            return pickle.load(f)
        
    def __dump_account_db(self, account_db):
        with open(self.__db_location, 'wb') as f:
            pickle.dump(account_db, f)
    
    def search_account(self, account_id = None, account_name = None):
        if account_id:
            account = self.__search_account_by_id(account_id)
            if account:
                print("#### INFO ####")
                self.__print_account_info(account)
                print("#############")
        elif account_name:
            accounts_list = self.__search_account_by_name(account_name)
            if len(accounts_list) > 0:
                print("INFO: Below are accounts satisfying search keywords")
                for account in accounts_list:
                    print("#### INFO ####")
                    self.__print_account_info(account)
                    print("#############")
            else:
                print("FAIL: No account satisfying keywords in search.\n")
        else:
            print("FAIL: Please enter keywords for search.\n")
            return

    def __search_account_by_id(self, account_id):
        account_db = self.__load_account_db()
        if account_id not in account_db:
            print("FAIL: Account {} is not found!\n".format(account_id))
            return
        else:
            print("SUCCESS: Account {} is Found!\n".format(account_id))
            return account_db[account_id]

    def __search_account_by_name(self, account_name):
        account_db = self.__load_account_db()
        re = []
        for key in account_db:
            account = account_db[key]
            if account.get_account_name() == account_name: ## this can be exactly match or fuzzy match
                re.append(account)
        return re

    def __print_account_info(self, account):
        account_id = account.get_account_id()
        account_name = account.get_account_name()
        print("Account id: {0}\nAccount name: {1}".format(account_id, account_name))
        account.get_account_history()
        
    def borrow_book(self, book_id, account_id, datetime):
        book = self._lib.get_book(book_id)

        if not book or book.get_status() is False:
            print("FAIL: Book {} is not available\n".format(book_id))
            return
        
        account_db = self.__load_account_db()
        if account_id not in account_db:
            print("FAIL: Account is not registered!\n")
            return
        
        account = account_db[account_id]
        if account.update_account_history(datetime = datetime, book = book, typ = 'borrow'):
            self._lib.update_book_status(book_id, False)
            print("SUCCESS: Account {0} borrowed book {1} on datetime {2}!\n".format(account.get_account_name(), book.get_book_name(), datetime))
        self.__dump_account_db(account_db)

    def return_book(self, book_id, account_id, datetime):
        book = self._lib.get_book(book_id)

        if book.get_status() is True:
            print("FAIL: This book is not borrowed\n")
            return
        
        account_db = self.__load_account_db()
        if account_id not in account_db:
            print("FAIL: Account is not registered!\n")
            return
        
        account = account_db[account_id]
        if account.update_account_history(datetime = datetime, book = book, typ = 'return'):
            self._lib.update_book_status(book_id, True)
            print("SUCCESS: Account {0} return book {1} on datetime {2}!\n".format(account.get_account_name(), book.get_book_name(), datetime))
        self.__dump_account_db(account_db)
