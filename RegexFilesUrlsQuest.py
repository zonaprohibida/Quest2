#Quest: Regex, Files, Urls
#Master Build, answering questions with regular expressions
import re, pytest, urllib.request

__STUDENT_ID__  = "47555408"        # replace with your 8 digit student id
__CODING_NAME__ = "tkyaagba"           # replace with your coding name - max 15 characters
__QUEST_NAME__ ="rex_io"
__VOWELS__ = "AEIOUaeiou"

#COMPLETE / PASSED
def count_vowels(mystr):
    """return the number of vowels, upper and lowercase a,e,i,o,u in the string
    >>> count_vowels('aaacvemmikkOOzzuU')  -> 9
    """
    vowels = re.findall(r'[AEIOUaeiou]', mystr)
    return len(vowels)

#COMPLETE / PASSED
def is_valid_python_hex(mystr):
    """is string a valid hex: begins with 0x and contains only 0-9 and A-F (lower or upper)
     >>> is_valid_python_hex('0x1A2f') -> True
     >>> is_valid_python_hex('x1A2f')  -> False
     >>> is_valid_python_hex('0x1A2G') -> False
    """
    matchObj = re.match(r'0x[0-9a-fA-F]+', mystr)
    if matchObj and matchObj.group() == mystr:
        return True
    else:
        return False

#COMPLETE / PASSED
def has_vowel(mystr):
    """   return True if a vowel upper or lowercase in string
    >>> has_vowel("zcxvsd")     -> False
    >>> has_vowel("vcbxvefjk")  -> True
    """
    searchObj = re.search(r'[AEIOUaeiou]', mystr)
    if searchObj:
        return True
    else:
        return False

#COMPLETE / PASSED
def is_integer(mystr):
    """ returns True if integer with optional minus sign
    >>> is_integer("2345")     -> True
    >>> is_integer("-192345")  -> True
    >>> is_integer("234x5")    -> False
    """
    matchObj = re.match(r'[\-\d]\d+', mystr)
    if matchObj and matchObj.group() == mystr:
        return True
    else:
        return False

#COMPLETE / PASSED
def get_extension(mystr):
    """ returns the extension for a filename or 'NONE' if no extension
    >>> get_extension('foo.zip')     -> 'zip'
    >>> get_extension('foo.doc.txt') -> 'txt'
    >>> get_extension('foozip')      -> 'NONE'
    """
    extension = re.search(r'\.(\w+)$', mystr)
    if extension:
        return extension.group(1)
    else:
        return 'NONE'

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
    
    matchObj = re.match(r'([\-\d]\d*)(\.?)(\d*)', mystr)
    if matchObj and matchObj.group() == mystr:
        return True
    else:
        return False

#COMPLETE / PASSED
def convert_date_format(mystr):
    """ convert date format YYYY-MO-DAY  TO MO-DAY-YYYY. If not in date format
        return "NONE" . Check only 4 digits for year and 2 digits for MO and DAY
    >>> convert_date_format('2018-03-04')  -> '03-04-2018'
    >>> convert_date_format('2018.03-04')  -> 'NONE'
    >>> convert_date_format('2018-03-054') -> 'NONE'
    """
    matchObj = re.match(r'(\d{4})\-(\d{2})\-(\d{2})', mystr)
    if matchObj and matchObj.group() == mystr:
        formatedDate = '%s-%s-%s' % (matchObj.group(2), matchObj.group(3), matchObj.group(1))
        return formatedDate
    else:
        return 'NONE'

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
        contentList = re.findall(stringval, fileContent)
        numStrings = len(contentList)
    return numStrings

#COMPLETE / PASSED
def readFileSumDigitsGreaterThanNumber(filename, number):
    """e.g. file = "hello22world2100and18and 1000", number =999 -> 3100
     >>> readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)  -> 88
    """
    digiSum = 0
    with open(filename, 'r') as fileReader:
        fileContent = fileReader.read()
        contentList = re.findall(r'(\d+)', fileContent)
        for item in contentList:
            if item.isdigit() and int(item) > number:
                digiSum += int(item)
    return digiSum

#COMPLETE / PASSED
def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    alphaList = re.findall(r'[a-zA-Z]+', mystr)
    return ''.join(alphaList)

#URL functions
#COMPLETE / PASSED
def readurlCountStringOccurrences(urlname, stringval, flags= re.I):
    """return number of times  stringval appears in text of url - ignore case
     >>> readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')  -> 3
    """
    urlObj = urllib.request.Request(urlname)
    urlReader = urllib.request.urlopen(urlObj)
    urlContentBytes = urlReader.read()
    urlContentString = urlContentBytes.decode("ASCII")
    
    matchList = re.findall(stringval, urlContentString, flags= re.I)
    return len(matchList)

#COMPLETE / PASSED
def readurlCountValidPhoneNumbers(urlname):
    """return count of valid phone number formats: no separator, dash separator, period separator:
    valid: 2126663333, 212-666-3333, 212.666.3333
    invalid: 212-444.5555, 212.333-4444, 212, 6363636363636
    >>> readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')  -> 3
    """
    urlObj = urllib.request.Request(urlname)
    urlReader = urllib.request.urlopen(urlObj)
    urlContentBytes = urlReader.read()
    urlContentString = urlContentBytes.decode("ASCII")
    
    matchList = re.findall(r'\d{10}|\d{3}([\.\-])\d{3}\1\d{4}', urlContentString)
    
    return len(matchList)



if __name__  == '__main__':
    print ("To test your code execute: python test_QuestFilesUrls.py  or on command line execute: pytest ")
