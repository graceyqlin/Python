class Book:
    
    def __init__(self, book_id, book_name, author, status = True):
        self.__book_id = book_id
        self.__status = status ## init status is available to borrow
        
        self.__book_name = book_name
        self.__author = author
            
    def get_book_id(self):
        return self.__book_id
    
    def get_book_name(self):
        return self.__book_name
    
    def set_book_name(self, new_name):
        self.__book_name = new_name
    
    def get_author(self):
        return self.__author
            
    def set_author(self, author):
        self.__author = author
        
    def set_status(self, status):
        self.__status = status
        
    def get_status(self):
        return self.__status
    