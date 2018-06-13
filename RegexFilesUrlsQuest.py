#Quest: Regex, Files, Urls

import re, pytest

__STUDENT_ID__  = "47555408"        # replace with your 8 digit student id
__CODING_NAME__ = "tkyaagba"           # replace with your coding name - max 15 characters
__QUEST_NAME__ ="rex_io"
__VOWELS__ = "AEIOUaeiou"

#COMPLETE / PASSED
def count_vowels(mystr):
    """return the number of vowels, upper and lowercase a,e,i,o,u in the string
    >>> count_vowels('aaacvemmikkOOzzuU')  -> 9
    """
    #First, convert string to lower case for ease of comparison
    #lowerString = mystr.lower()
    vowelCount = 0
    
    for char in mystr:
        if char in __VOWELS__:
            vowelCount += 1
    
    return vowelCount

#COMPLETE / PASSED
def is_valid_python_hex(mystr):
    """is string a valid hex: begins with 0x and contains only 0-9 and A-F (lower or upper)
     >>> is_valid_python_hex('0x1A2f') -> True
     >>> is_valid_python_hex('x1A2f')  -> False
     >>> is_valid_python_hex('0x1A2G') -> False
    """
    answer = False
    
    #not valid hex if it doesn't begin with '0x'
    if not mystr.startswith("0x"):
        answer = False
    #not valid hex if string contains non alpha-numeric characters
    elif not mystr.isalnum():
        answer = False
    else:
        for i in range(2, len(mystr)):
            #check that alphabet characters are only from a through f or A through F
            char = mystr[i]
            if char.isalpha():
                if (char.islower() and char < 'g') or (char.isupper() and char < 'G'):
                    answer = True
                else:
                    #if any character is not within spec., end the loop and declare invalid hex
                    answer = False
                    break
    
    return answer

#COMPLETE / PASSED
def has_vowel(mystr):
    """   return True if a vowel upper or lowercase in string
    >>> has_vowel("zcxvsd")     -> False
    >>> has_vowel("vcbxvefjk")  -> True
    """
    answer = False
    for char in mystr:
        if char in __VOWELS__:
            answer = True
            break
    return answer

#COMPLETE / PASSED
def is_integer(mystr):
    """ returns True if integer with optional minus sign
    >>> is_integer("2345")     -> True
    >>> is_integer("-192345")  -> True
    >>> is_integer("234x5")    -> False
    """

    if not mystr[1:].isdigit():
        return False
    elif mystr[0].isdigit() or mystr[0] == '-':
        return True

#COMPLETE / PASSED
def get_extension(mystr):
    """ returns the extension for a filename or 'NONE' if no extension
    >>> get_extension('foo.zip')     -> 'zip'
    >>> get_extension('foo.doc.txt') -> 'txt'
    >>> get_extension('foozip')      -> 'NONE'
    """
    #find last index of '.'
    i = mystr.rfind('.')
    #return 'NONE' if '.' is the last character or is not found at all
    if i == len(mystr) - 1 or i == -1:
        return 'NONE'
    else:
        return mystr[i+1 : ]

#COMPLETE / PASSED
def is_number(mystr):
    """ floating point number with optional - sign and optional decimal point
    >>> is_number('234')        -> True
    >>> is_number('-234')       -> True
    >>> is_number('234.')       -> True
    >>> is_number('234.999')    -> True
    >>> is_number('234.99.77')  -> False
    >>> is_number('234a.88')    -> False
    """
    mystrList = mystr.split('.')
    
    #number is invalid if list has more than 2 items
    if len(mystrList) > 2:
        return False
    #number is invalid if integer portion is not a number
    elif not is_integer(mystrList[0]):
        return False
    #number is invalid if decimal portion is not a number
    elif len(mystrList) == 1:
        return True
    #number is invalid if decimal portion is neither a number nor empty
    elif not (is_integer(mystrList[1]) or mystrList[1] == ''):
        return False
    #if non of the previous conditions is satisfied, the number is valid
    else:
        return True

#COMPLETE / PASSED
def convert_date_format(mystr):
    """ convert date format YYYY-MO-DAY  TO MO-DAY-YYYY. If not in date format
        return "NONE" . Check only 4 digits for year and 2 digits for MO and DAY
    >>> convert_date_format('2018-03-04')  -> '03-04-2018'
    >>> convert_date_format('2018.03-04')  -> 'NONE'
    >>> convert_date_format('2018-03-054') -> 'NONE'
    """
    
    dateList = mystr.split('-')
    
    #invalid delimiter
    if not len(dateList) == 3:
        return 'NONE'
    #invalid year, month, or day based on number of digits
    elif not (len(dateList[0]) == 4) or not (len(dateList[1]) == 2) or not (len(dateList[2]) == 2):
        return 'NONE'
    else:
        dateList.append(dateList.pop(0))
        return '-'.join(dateList)


#File functions

#COMPLETE / PASSED
def readFileCountLines(filename):
    """use download file from Canvas: pytestFile1.txt - return number of lines
    >>> readFileCountLines('pytestFile1.txt')  -> 4
    """
    numLines = 0
    with open(filename,'r') as fileReader:
        fileContent = fileReader.readlines()
        numLines = len(fileContent)

    return numLines

#COMPLETE / PASSED
def readFileCountStringOccurrences(filename, stringval):
    """read file: pyTestFile1.txt  - return number of times  stringval appears
    >>> readFileCountStringOccurrences('pytestFile1.txt','rollo')  -> 3
    """
    numStrings = 0
    with open(filename, 'r') as fileReader:
        fileContent = fileReader.read()
        contentList = fileContent.split()
        for item in contentList:
            if item == stringval:
                numStrings += 1
    return numStrings

#COMPLETE / PASSED
def readFileSumDigitsGreaterThanNumber(filename, number):
    """e.g. file = "hello22world2100and18and 1000", number =999 -> 3100
     >>> readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)  -> 88
    """
    digiSum = 0
    with open(filename, 'r') as fileReader:
        fileContent = fileReader.read()
        contentList = fileContent.split()
        for item in contentList:
            if item.isdigit() and int(item) > number:
                digiSum += int(item)
    return digiSum

#COMPLETE / PASSED
def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    alphaList = [char for char in mystr if char.isalpha()]
    return ''.join(alphaList)

#URL functions
def readurlCountStringOccurrences(urlname, stringval):
    """return number of times  stringval appears in text of url - ignore case
     >>> readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')  -> 3
    """
    return 100

def readurlCountValidPhoneNumbers(urlname):
    """return count of valid phone number formats: no separator, dash separator, period separator:
    valid: 2126663333, 212-666-3333, 212.666.3333
    invalid: 212-444.5555, 212.333-4444, 212, 6363636363636
    >>> readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')  -> 3
    """
    return 100



if __name__  == '__main__':
    print ("To test your code execute: python test_QuestFilesUrls.py  or on command line execute: pytest ")



