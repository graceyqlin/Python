class Account:
    
    def __init__(self, account_id, account_name):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__account_history = []

    def get_account_id(self):
        return self.__account_id
    
    def set_account_id(self, new_id):
        self.__account_id = new_id
    
    def get_account_name(self):
        return self.__account_name
    
    def set_account_name(self, new_name):
        self.__account_name = new_name
        
    def get_account_history(self):
        print("Account Borrow History:")
        if self.__account_history:
            for item in self.__account_history:
                if item[2] == 'borrow':
                    print("** Datetime {0} borrowed Book {1}".format(item[0], item[1]))
                if item[2] == 'return':
                    print("** Datetime {0} returned Book {1}".format(item[0], item[1]))
        else:
            print("No borrow history found!")
            
    def update_account_history(self, datetime, book, typ):
        self.__account_history.append((datetime, book.get_book_id(), typ))
        return True
    