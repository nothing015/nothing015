'''
Create a function that transforms any positive number to a string representing the number in words.
The function should work for all numbers between 0 and 999999.

Examples
number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
number2words(9)  ==>  "nine"
number2words(10)  ==>  "ten"
number2words(17)  ==>  "seventeen"
number2words(20)  ==>  "twenty"
number2words(21)  ==>  "twenty-one"
number2words(45)  ==>  "forty-five"
number2words(80)  ==>  "eighty"
number2words(99)  ==>  "ninety-nine"
number2words(100)  ==>  "one hundred"
number2words(301)  ==>  "three hundred one"
number2words(799)  ==>  "seven hundred ninety-nine"
number2words(800)  ==>  "eight hundred"
number2words(950)  ==>  "nine hundred fifty"
number2words(1000)  ==>  "one thousand"
number2words(1002)  ==>  "one thousand two"
number2words(3051)  ==>  "three thousand fifty-one"
number2words(7200)  ==>  "seven thousand two hundred"
number2words(7219)  ==>  "seven thousand two hundred nineteen"
number2words(8330)  ==>  "eight thousand three hundred thirty"
number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"
'''

#Nuaiman's Solution(upto 99)
'''
def NumberToWords(n):
    string = ""
    l = len(str(n))
    single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_digits = [" "," ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_power = ["hundred", "thousand"]
    if l == 1:
        if n == 0:
            return "zero"
        return single_digits[n]
    if l == 2:
        if n < 20:
            return two_digits[n-10]
        else:
            for m in range(l):
                if m == 0:  # m is the digit position
                    string += tens_digits[int(str(n)[m])]
                else:
                    string +='-'+ single_digits[int(str(n)[m])]
            if string[len(string)-1] == "-":
                string = string.strip("-")
                return string
            return string
     
      
     if l == 3:
        string += single_digits[int(str(n)[0])] + " hundred"
        if int(str(n)[1]) == 0 and int(str(n)[2]) == 0:
                return string
        else:
            if int(str(n)[1]+str(n)[2]) < 20:
                return string + two_digits[n-10-int(str(n)[0])]
            else:
                for m in range(2):
                    if m == 0:  # m is the digit position
                        string += tens_digits[int(str(n)[m])]
                    else:
                        string +='-'+ single_digits[int(str(n)[m])]
                if string[len(string)-1] == "-":
                    string = string.strip("-")
                    return string
                return string 
'''


#Solution 1
words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words(n):
    n = int(n)
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')

#Solution 2
'''
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
20:'twenty',30:'thirty',40:'forty',50:'fifty',
60:'sixty',70:'seventy',80:'eighty',90:'ninety',
100:'hundred',1000:'thousand'}
def number2words(n):
    """ works for numbers between 0 and 999999 """
    if 0<=n<=20:return d[n]
    if 20<n<=99 and n%10:return d[10*(n//10)]+'-'+d[n%10]
    if 20<n<99:return d[10*(n//10)]
    if n<1000 and n%100==0:return d[n//100]+' '+d[100]
    if 100<n<=999:return d[n//100]+' '+d[100]+' '+number2words(n%100)
    if n%1000==0:return d[n//1000]+' '+d[1000]
    return number2words(n//1000)+' '+d[1000]+' '+number2words(n%1000)
'''

while True:
    print(number2words(input("Enter any integer between 0 and 999999 to convert it to string: ")))
    
            
