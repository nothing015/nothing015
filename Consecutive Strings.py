'''
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
'''

#Nuaiman's Solution
def longest_consec(strarr, k):
    SortArray = []
    largest = 0
    if strarr == "" or k > len(strarr) or k < 0:
        return("")
    for e in range(len(strarr)-(k-1)):
        string = ''
        for j in range(k):
            string = string + strarr[e+j]
        SortArray.append(string)
    largest = max(SortArray, key = len)

    return largest

#Solution 1
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

#Solution 2
def longest_consec(strarr, k):
    # Make sure that k is greater than zero and less that the
    # length of the array of strings. Otherwise return an empty string
    if k <= 0 or k > len(strarr):
        return ''

    # Finding the longest string consisting of k consecutive
    # strings is equivalent to finding the maximum sum of
    # k consecutive elements of an array that represents the
    # lengths of an array of strings.

    # star_lengths represents a list of lengths of the initial
    # array of strings.
    starr_lengths = list(map(len, strarr))
    # Find the maximum sum of k consecutive elements
    # requires keeping a temperary maximum length.
    temp_max_len = 0
    # We also need to keep the position of the first element of
    # each group.
    position = 0

    # Scan the whole list of lengths except the final k elements
    for p in range(len(starr_lengths) - (k - 1)):
        # We need to find the sum of the current set of elements
        # starting at position p
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p+i]
        
        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position+k]])

























