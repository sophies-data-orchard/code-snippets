# Regex - Regular expression
# https://docs.python.org/3/howto/regex.html
# https://regex101.com/

re.findall(): returns a list containing all matches.
re.search(): searches the string for a match, and returns a Match object if there is a match.
re.compile():Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.
.group:This method returns a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern
re.split()
re.sub()
re.finditer()


import re

txt = " The rain in Spain"
print(re.findall("ai",txt))
# ['ai', 'ai']

print(re.findall('a..',txt))
# ['ain', 'ain']

x=re.search("S",txt)
print(x)
# <re.Match object; span=(13, 14), match='S'>
print("the matched postion:",x.start())
# the matched postion: 13

#Check if the string contains either "falls" or "stays":
txt = "The rain in Spain falls mainly in the plain!"
print(re.findall("fall|stays",txt))
# ['fall']
if re.findall("fall|stays",txt):
    print("Yes")
else:
    print("No match")
# Yes

# Special Characters
# If we want to match our characters that already have a meaning, like |, we have to "escape" them.

txt = "is there | in this line"
x = re.findall("|", txt)
print(x)
# ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
x = re.findall("\|", txt)
print(x)
# ['|']

# Character Class
txt = 'abcdef'
print(re.findall('[a-c]',txt))
# ['a', 'b', 'c']

print(re.findall('[^a-c]',txt))
# ['d', 'e', 'f']


re_names2=re.compile(r'''^
                        ([a-zA-Z]+)
                        \s+
                        ([a-zA-Z]+\s)?
                        ([a-zA-Z]+)
                        $
                        ''',
                        re.VERBOSE)
print((re_names2).match('Brad Haddin').groups())
# ('Brad', None, 'Haddin')



# The re.VERBOSE flag in Python’s re module allows you to write regular expressions in a more readable and organized way. When you use re.VERBOSE, you can include whitespace and comments within your regex pattern, which makes it easier to understand and maintain. Here’s a quick overview:

# Key Features of re.VERBOSE:
# Whitespace Ignored:
# Whitespace within the pattern is ignored, except when inside a character class or when preceded by an unescaped backslash.
# Comments:
# You can add comments using the # character. Everything from the # to the end of the line is ignored.
# Example Without re.VERBOSE:
# Python

import re

pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')


# Example With re.VERBOSE:
# Python

import re

pattern = re.compile(r'''
    ^           # Start of the string
    \d{3}       # Area code (3 digits)
    -           # Separator
    \d{2}       # First part of the number (2 digits)
    -           # Separator
    \d{4}       # Second part of the number (4 digits)
    $           # End of the string
''', re.VERBOSE)

# # Named groups
re_names3 = re.compile(r'''^
                           (?P<first>[a-zA-Z]+)
                           \s
                           (?P<middle>[a-zA-Z]+\s)?
                           \s*
                           (?P<last>[a-zA-Z]+)
                           $
                        ''',
                        re.VERBOSE)
print(re_names3.match('Brad Haddin').group('first'))
# Brad
print(re_names3.match('Brad J Haddin').group('middle'))
# J
print(re_names3.match('Brad J Haddin').group('last'))
# Haddin



# NB5-part0
### Define demo inputs
demo_str_ex0_0 = '832-38-1847'
demo_str_ex0_1 = '832 -38 -  1847'
demo_str_ex0_2 = '832-bc-3847'
demo_str_ex0_3 = '832381847'

parts = demo_str_ex0_0.split('-')
# print(parts)
def is_ssn(s):
    parts = s.split('-')  #['832', '38', '1847']
    correct_len = [3,2,4]
    if len(parts)!= len(correct_len):
        return False
    for p,n in zip(parts,correct_len):
        if not (p.isdigit()) and len(p)==n:
            return False
    return True

print(is_ssn(demo_str_ex0_0))





# regexone.com
# Exercise 1: Matching characters
# Task	Text	 
# match	abcdefg	Success
# match	abcde	Success
# match	abc
abc

# Exercise 1½: Matching digits
# Task	Text	 
# match	abc123xyz	To be completed
# match	define "123"	To be completed
# match	var g = 123;
\w
or

# Exercise 2: Matching with wildcards
# Task	Text	 
# match	cat.	To be completed
# match	896.	To be completed
# match	?=+.	To be completed
# skip	abc1
...\. 
# You can use ...\. to match the first three (wildcard) characters, 
# and escape the final wildcard meta-character to match the period instead. 
# This ensures that it will not match the '1' in the fourth line.

# Exercise 3: Matching characters
# Task	Text	 
# match	can	Success
# match	man	Success
# match	fan	Success
# skip	dan	To be completed
# skip	ran	To be completed
# skip	pan
[cmf]an  #[cmf]an to match only 'can', 'man' and 'fan' without matching any other line.
[^drp]an #match any three letter word ending with 'an' that does not start with 'd', 'r' or 'p'.




# ex4: excluding char
# Task	Text	 
# match	hog	Success
# match	dog	Success
# skip	bog
[^b]og
or
[hd]og

# Exercise 5: Matching character ranges
# Task	Text	 
# match	Ana	Success
# match	Bob	Success
# match	Cpc	Success
# skip	aax	To be completed
# skip	bby	To be completed
# skip	ccz
[^a-c][n-p][a-c]
or
[A-C][n-p][a-c]

# Exercise 6: Matching repeated characters
# a{1,3} will match the a character no more than 3 times, but no less than once for example.
# Task	Text	 
# match	wazzzzzup	Success
# match	wazzzup	Success
# skip	wazup
waz{3,5}up

# Exercise 7: Matching repeated characters
# Task	Text	 
# match	aaaabcc	Success
# match	aabbbbc	Success
# match	aacc	Success
# skip	a

aa+[bc]+
or
aa+b*c+
or
aa+b*c*

#Alternatively, an even more restrictive expression would be 
a{2,4}b{0,4}c{1,2} #which puts both an upper and lower bound on the number of each of the characters.

# Exercise 8: Matching optional characters
# Task	Text	 
# match	1 file found?	Success
# match	2 files found?	Success
# match	24 files found?	Success
# skip	No files found.
\d+ files? found\?  #\? is to escaple the ?

# Exercise 9: Matching whitespaces
# Task	Text	 
# match	1.   abc	Success
# match	2.	abc	Success
# match	3.           abc	Success
# skip	4.abc
\d\.\s+abc 
#\d match digit
\. escape period
\s+ one or more white space 

# Exercise 10: Matching lines
#  if you combine both the hat and the dollar sign, you create a pattern that matches the whole line completely at the beginning and end.
# Task	Text	 
# match	Mission: successful	Success
# skip	Last Mission: unsuccessful	To be completed
# skip	Next Mission: successful upon capture of target
^Mission: successful$  #to only match the full string that starts with 'Mission' and ends with 'successful'.

# Exercise 11: Matching groups
# you could use the pattern ^(IMG\d+)\.png$ which only captures the part before the period.
# Task	Text	Capture Groups	 
# capture	file_record_transcript.pdf	file_record_transcript	Success
# capture	file_07241999.pdf	file_07241999	
^(file\w*)\.pdf$
  or
^(file.+)\.pdf$

# Exercise 12: Matching nested groups
# Task	Text	Capture Groups	 
# capture	Jan 1987	Jan 1987 1987	Success
# capture	May 1969	May 1969 1969	Success
# capture	Aug 2011	Aug 2011 2011	Success
^(\w+\s+(\d+))
 ^(\w+  
   # output whole dates: Jan 1987
\s+(\d+)
# escape the space btw month and year, only output year number   

# Exercise 13: Matching nested groups
# Task	Text	Capture Groups	 
# capture	1280x720	1280 720	Success
# capture	1920x1600	1920 1600	Success
# capture	1024x768	1024 768	Success

(\d+)x(\d+)
#  we just need to capture the two groups of digits as such (\d+)x(\d+).
# (\d+) to get 1280, then second(\d+) to get 720

# Exercise 14: Matching conditional text

# Specifically when using groups, you can use the | (logical OR, aka. the pipe) to denote 
# different possible sets of characters. In the above example, I can write the pattern 
# "Buy more (milk|bread|juice)" to match only the strings Buy more milk, Buy more bread, or Buy more juice.

# Like normal groups, you can use any sequence of characters or metacharacters in a condition, for example, 
# ([cb]ats*|[dh]ogs?) would match either cats or bats, or, dogs or hogs. Writing patterns with many conditions
#   can be hard to read, so you should consider making them separate patterns if they get too complex.

# Task	Text	 
# match	I love cats	Success
# match	I love dogs	Success
# skip	I love logs	To be completed
# skip	I love cogs

I love (cats|dogs)


# Exercise 15: Matching other special characters
# to capture digits using \d, 
# whitespace using \s, 
# and alphanumeric letters and digits using \w, 
# but regular expressions also provides a way of specifying the opposite sets of each of these metacharacters by using 
# their upper case letters. For example, 
# \D represents any non-digit character, 
# \S any non-whitespace character, and 
# \W any non-alphanumeric character (such as punctuation). 
# Depending on how you compose your regular expression, it may be easier to use one or the other.

# Additionally, there is a special metacharacter 
# \b which matches the boundary between a word and a non-word character. 
# It's most useful in capturing entire words (for example by using the pattern 
# \w+\b).


# Task	Text	 
# match	The quick brown fox jumps over the lazy dog.	Success
# match	There were 614 instances of students getting 90.0% or above.	Success
# match	The FCC had to censor the network for saying &$#*@!.

.*

import copy

original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

# Modify the nested list in the shallow copy
shallow_copy[2][0] = 'changed'

print("Original:", original)  # Output: [1, 2, ['changed', 4]]
print("Shallow Copy:", shallow_copy)  # Output: [1, 2, ['changed', 4]]
print("Deep Copy:", deep_copy)  # Output: [1, 2, [3, 4]]

test_str = "Geeks  forGeeks"
if test_str.find(" ")!=-1: # when space not found, it returns -1
    raise ValueError
else:
    print("space is not found")

s= 'sss@edu.com'
s.split('@')
tuple(s.split('@'))


import re

# Sample email addresses
emails = ["test@example.com", "invalid-email@", "user.name@domain.co", "user@domain"]

# Function to validate email addresses
def validate_email(email):
    # Regex pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print(re.match.group())

    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
for email in emails:
    print(f"{email}: {validate_email(email)}")


# test@example.com: True
# invalid-email@: False
# user.name@domain.co: True
# user@domain: False

import re
pattern = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
s='invalid-email@'
# print(pattern.match(s).group())

print(re.findall(pattern,s))


import re

pattern = re.compile ('''
            ^
            (?P<p0>\s*\(|\()
            (?P<p1>\d{3})
            \)
            (?P<p2>\s*\d{3})
            \-
            (?p<p3>\d{4}\s*|\d{4})
            $
        ''',
        re.VERBOSE)    

pattern=r'^(\s*?\(\d{3}\)\s*?\d{3}\-\d{4}\s*?$)'


# Make the expression more readable with a re.VERBOSE pattern
re_names2 = re.compile(r'''^              # Beginning of string
                           ([a-zA-Z]+)    # First name
                           \s+            # At least one space
                           ([a-zA-Z]+\s)? # Optional middle name
                           ([a-zA-Z]+)    # Last name
                           $              # End of string
                        ''',
                        re.VERBOSE)
print(re_names2.match('Rich Vuduc').groups())
print(re_names2.match('Rich S Vuduc').groups())
print(re_names2.match('Rich Salamander Vuduc').groups())
# ('Rich', None, 'Vuduc')
# ('Rich', 'S ', 'Vuduc')
# ('Rich', 'Salamander ', 'Vuduc')
import re
pattern=re.compile(r'''^
                    \s*\(
                    (\d{3}) #area code
                    \)\s*
                    (\d{3}) #first_three
                    \-
                    (\d{4}) #last_four
                    \s*
                    $ 
                    ''',
                    re.VERBOSE)
print(pattern.match('404-121-2121'))


    pattern = re.compile(r'''^
                            \s*\(
                            (\d{3}) #area code
                            \)\s*
                            (\d{3}) #first_three
                            \-
                            (\d{4}) #last_four
                            \s*
                            $ 
                            ''',
                            re.VERBOSE)

    match_result = pattern.match(s)
    try:
        return match_result.groups()  
    except AttributeError:
        raise ValueError

    pattern = re.compile ('''^
                           ([a-zA-Z][\w\-\.\+]+) #username
                           \@
                           ([\w\-\.\+]+[a-zA-Z]) #domainname
                           $
                            ''',
                        re.VERBOSE)
    match_result = pattern.match(s)
    s='richie@cc.gatech.edu7'0
    print(match_result.groups())


    p1 = re.compile("\s*\(\d{3}\)\s*\-?\d{3}\-?\d{4}\s*)|(^\s*\d{3}\-?\d{3}\-?\d{4}\s*$")
    # s= '(404-555-1212' #None
    s= '(404)-555-1212'
    print(p1.match(s).groups())

p11=re.compile(r'''^
                \s*\(
                (\d{3}) #area code
                \)\s*\-?
                (\d{3}) #first 3
                \-?
                (\d{4}) #second 4
                \s*
                $
                ''',
                re.VERBOSE)
s= '(404)-555-1212'
# s ='404-555-1212'
print(p11.match(s).groups())

p12=re.compile(r"^\s*(\d{3})\-?(\d{3})\-?(\d{4})\s*$")
# s= '(404)-555-1212'
s ='455-5551212'
print(p12.match(s).groups())


# p = re.compile(r'^\s*\((\d{3})\)\s*\-?(\d{3})\-?(\d{4})\s*$|^\s*(\d{3})\-?(\d{3})\-?(\d{4})\s*$')
p = re.compile(r'^\s*\((\d{3})\)\s*\-?(\d{3})\-?(\d{4})\s*$|^\s*(\d{3})\-?(\d{3})\-?(\d{4})\s*$')
# s ='455-5551212'  (None, None, None, '455', '555', '1212')
s= '(404-555-1212' # ('404', '555', '1212', None, None, None)       
# s= '(404-555-1212'   AttributeError: 'NoneType' object has no attribute 'groups' 
matched =  p.match(s).groups()

result = []
for item in matched:
    if item != None:
        result.append(item)
print(tuple(result))
        
        
print(p.match(s).groups()) 




    \s*\(?(\d{3})\)?\-?\s*(\d{3})\-?(\d{4})\s*

    check ()
    (\s*\(\d{3}\)\s*\-?\d{3}\-?\d{4}\s*)|
     
     /(\s*\(\d{3}\)\s*\-?\d{3}\-?\d{4}\s*)|(^\s*\d{3}\-?\d{3}\-?\d{4}\s*$)/gm
       
<span class="indexed-biz-name">1 


pattern_bizname = re.compile(r'^\s+<span class="indexed-biz-name">(\d{1})\.\s*<a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="[^"]+"\s+data-hovercard-id="[^"]+"><span>(.*?)<\/span><\/a>$')



# s='                                    <span class="indexed-biz-name">2.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" data-hovercard-id="tvYceAR7TJ7zS6N6kF5y8g"><span>South City Kitchen - Midtown</span></a>'
s='                                    <span class="indexed-biz-name">3.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/mary-macs-tea-room-atlanta?osq=fried+chicken" data-hovercard-id="J1q9KDyfksvcce8qiv3wXA"><span>Mary Mac’s Tea Room</span></a>'
matched = pattern_bizname.match(s)
# print(matched.groups())
output = matched.groups()
print(output)
rankings =[]
rankings[item]['names']= output[1]

for item in rankings
    rankings[item]['name'] = matched.groups[1]
print(rankings)

# rankings = {'name': ,}
# rankings[item]['name'] 

yelp_html ='                                    <span class="indexed-biz-name">3.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/mary-macs-tea-room-atlanta?osq=fried+chicken" data-hovercard-id="J1q9KDyfksvcce8qiv3wXA"><span>Mary Mac’s Tea Room</span></a>'



for item in yelp_html2:
    try:
        pattern_bizname.match(item).groups()
    except AttributeError:
        raise ValueError    

s='</span>
                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix"> 
    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">'

pattern_rate=re.compile(r'<\/span>[\n\r\s]+<\/h3>[\n\r\s]+<div\sclass="biz-rating\sbiz-rating-large\sclearfix">[\n\r\s]+<div[\w\-\"\s]*|\"{1}(\d{1}\.\d{1})\sstar\srating\">')
s='</span></h3><div class="biz-rating biz-rating-large clearfix"><div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">'
print(pattern_rate.match(s).groups())

<span class="indexed-biz-name">1.
<span>Gus’s World Famous Fried Chicken</span>

<span class="review-count rating-qualifier">
            549 reviews
    </span>

<span class="business-attribute price-range">$$</span>


\s+<span class="indexed-biz-name">(\d{1})\.\s*<a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="[^"]+"\s+data-hovercard-id="[^"]+"><span>(.*?)|<\/span>^<\/span>[\n\r\s]+<\/h3>[\n\r\s]+<div\sclass="biz-rating\sbiz-rating-large\sclearfix">[\n\r\s]+<div[\w\-\"\s]*|\stitle="{1}(\d{1}\.\d{1})\sstar\srating\">^[\n\r\s]+<span\sclass="review-count\srating-qualifier">[\n\r\s]*(\d+)\s*reviews[\n\r\s]+<\/span>\s*<span class="business-attribute price-range">\s*(\${1,5})\s*<\/span>'

re.compile(r'<span\sclass="indexed-biz-name">(?P<rank>\d*)[\s\S]*?<span>(?P<name>[\s\S]*?)</span></a>[\s\S]*?(?P<star>\d\.\d)[\s\S]*?(?P<numrevs>\d*)\sreviews[\s\S]*ge">(?P<price>\${1,5})</span>')

# for memeory only, silly code
    # bizname_p = re.compile(r'^\s+<span class="indexed-biz-name">\d{1}\.\s*<a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="[^"]+"\s+data-hovercard-id="[^"]+"><span>(.*?)<\/span><\/a>$')
    # stars_p = re.compile(r'^<\/span>[\n\r\s]+<\/h3>[\n\r\s]+<div\sclass="biz-rating\sbiz-rating-large\sclearfix">[\n\r\s]+<div[\w\-\"\s]*|\stitle="{1}(\d{1}\.\d{1})\sstar\srating\">$')
    # numrews_p = re.compile(r'^[\n\r\s]+<span\sclass="review-count\srating-qualifier">[\n\r\s]*(\d+)\s*reviews[\n\r\s]+<\/span>$')
    # price_p = re.compile(r'^\s*<span class="business-attribute price-range">\s*(\${1,5})\s*<\/span>$')


match = [('2', 'ABC', '4.5', '19', '$$$'),('3', 'ZZZ', '2.0', '1000', '$'),('1', 'Gus’s World Famous Fried Chicken', '4.0', '549', '$$')]
#  asc_sort4 = sorted(student_tuples, key = lambda a:a[2], reverse = True)
print(sorted(match, key = lambda x:(x[0])))

result =[]
for item in list:
    ranking = { }
    ranking['name']= item[1]
    ranking['stars']= item[2]
    ranking['numrevs'] = item[3]
    ranking['price']=item[4]
    result.append(ranking) #[{'name': 'ZZZ', 'stars': '2.0', 'numrevs': '1000', 'price': '$'}]
print(result)
[{'name': 'Gus’s World Famous Fried Chicken', 'stars': '4.0', 'numrevs': '549', 'price': '$$'},
  {'name': 'ABC', 'stars': '4.5', 'numrevs': '19', 'price': '$$$'}, 
  {'name': 'ZZZ', 'stars': '2.0', 'numrevs': '1000', 'price': '$'}]


#     pattern_object = re.compile('<span\sclass="indexed-biz-name">(?P<rank>\d*)[\s\S]*?<span>(?P<name>[\s\S]*?)</span></a>[\s\S]*?(?P<stars>\d\.\d)[\s\S]*?(?P<numrevs>\d*)\sreviews[\s\S]*?ge">(?P<price>[\s\S]*?)</span>')
#     results = pattern_object.findall(yelp_html)
#     rankings = [{'name': result[1], 'stars':result[2], 'numrevs':int(result[3]), 'price':result[4]} for result in results]
#     return rankings