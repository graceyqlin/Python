class StringUtility(object):
    
    def reverse(self, data):
        """
        Return the reverse of the string
        """
        return data[::-1]
    
    def char_frequency(self, data, char):
        """
        Return the number times char is in data
        """
        return data.count(char)
    
    def is_palindrone(self, data):
        """
        Returns true if data is a palidrone, false otherwise
        """
        return data == data[::-1]