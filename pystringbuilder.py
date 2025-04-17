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

    def __copy_array_list(self, list_a, list_b):
        for e in list_a:
            list_b.add(e)
       
    def setLength(self, new_length):
        if new_length < self.__capacity:
            smaller_list = ArrayList(new_length)
            for i in range(0, new_length):
                smaller_list.add(self.__string_list.get(i))
            self.__string_list = smaller_list
            self.__capacity = new_length
        elif new_length > self.__capacity:
            larger_list = ArrayList(new_length)
            self.__copy_array_list(self.__string_list, larger_list)
            difference = new_length - self.__capacity
            for i in range(self.__capacity, self.__capacity+difference):
                larger_list.add(None)
            self.__string_list = larger_list
            self.__capacity = new_length
        #else new length is the same as current length
        #do nothing

    def ensureCapacity(self, min_capacity):
        if not self.__capacity >= min_capacity:
            print('bigger')
            bigger_list = ArrayList(min_capacity)
            self.__copy_array_list(self.__string_list, bigger_list)
            self.__string_list = bigger_list

    def append(self, element):
        self.__string_list.add(str(element))

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
        return_string = []
        for element in self.__string_list:
            return_string.append(str(element))
        return "".join(return_string)
    
    def __eq__(self):
        return False
    

if __name__ == '__main__':
    sb = StringBuilder("hello")
    print(sb)
    sb.setLength(14)
    print(sb)
