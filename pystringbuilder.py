'''

StringBuilder() 	Creates an empty string builder with a capacity of 16 (16 empty elements).
StringBuilder(CharSequence cs) 	Constructs a string builder containing the same characters as the specified CharSequence, plus an extra 16 empty elements trailing the CharSequence.
StringBuilder(int initCapacity) 	Creates an empty string builder with the specified initial capacity.
StringBuilder(String s) 	Creates a string builder whose value is initialized by the specified string, plus an extra 16 empty elements trailing the string.

void setLength(int newLength) 	Sets the length of the character sequence. If newLength is less than length(), the last characters in the character sequence are truncated. 
If newLength is greater than length(), null characters are added at the end of the character sequence.
void ensureCapacity(int minCapacity) 	Ensures that the capacity is at least equal to the specified minimum.

StringBuilder append(boolean b)
StringBuilder append(char c)
StringBuilder append(char[] str)
StringBuilder append(char[] str, int offset, int len)
StringBuilder append(double d)
StringBuilder append(float f)
StringBuilder append(int i)
StringBuilder append(long lng)
StringBuilder append(Object obj)
StringBuilder append(String s) 	Appends the argument to this string builder. The data is converted to a string before the append operation takes place.

StringBuilder delete(int start, int end)
StringBuilder deleteCharAt(int index) 	The first method deletes the subsequence from start to end-1 (inclusive) in the StringBuilder's char sequence. The second method deletes the character located at index.

StringBuilder insert(int offset, boolean b)
StringBuilder insert(int offset, char c)
StringBuilder insert(int offset, char[] str)
StringBuilder insert(int index, char[] str, int offset, int len)
StringBuilder insert(int offset, double d)
StringBuilder insert(int offset, float f)
StringBuilder insert(int offset, int i)
StringBuilder insert(int offset, long lng)
StringBuilder insert(int offset, Object obj)
StringBuilder insert(int offset, String s) 	Inserts the second argument into the string builder. The first integer argument indicates the index before which the data is to be 
inserted. The data is converted to a string before the insert operation takes place.

StringBuilder replace(int start, int end, String s)
void setCharAt(int index, char c) 	Replaces the specified character(s) in this string builder.

StringBuilder reverse() 	Reverses the sequence of characters in this string builder.
String toString() 	Returns a string that contains the character sequence in the builder.

'''
from py_array_list.ArrayList import ArrayList
import functools

class StringBuilder:
    def __init__(self, string = None, init_capacity = 16):
        '''
        Constructor for StringBuilder.

        Parameters:
            string (str): Initial string for the String Builder. 
            init_capacity (int): The starting size of the String Builder. Default 16 characters.
        '''
        self.__capacity = init_capacity
        self.__string_list = ArrayList(capacity = init_capacity)

        #If a string is provided. Append each char to internal array list.
        if not string == None:
            string = str(string) #Ensure that it is a string.
            for c in string:
                self.__string_list.add(c)

    def setLength(self, new_length):
        pass

    def ensureCapacity(self, min_capacity):
        pass

    def append(self, element):
        pass

    def delete(self, start, end):
        pass

    def deleteCharAt(self, index):
        pass

    def insert(self, offset, element):
        pass

    def replace(self, start, end, element):
        pass

    def setCharAt(self, index, char):
        pass

    def reverse(self):
        pass

    def toString(self):
        return self.__str__()

    def __str__(self):
        return functools.reduce(lambda string, c: string+c, self.__string_list)
    
    def __eq__(self):
        return False
    
