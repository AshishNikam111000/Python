import re, os
os.system('cls')

#message = 'Call me 8107106678 or at 8118006343' 
#regexNo = re.compile(r'\d*\d')  #compiling the type of pattern we want  #the \d*\d pattern means search a string which starts and ends with digit having as many as digits between them as * means 0 or more times the pattern appeares
#print (regexNo.findall(message))  #findall() will find all the matches matching the pattern and return a list of it.

#batRegex = re.compile(r'(Batman|Batmobile|Batcopter)')  #pipe(|) helps to search multiple patterns
#mo = batRegex.search('Batman is driving his Batmobile')  #seach() return Match Object which comes 1st and group them 
#print (mo.group())  #group(0) will give the whole searched pattern and group(1) will give the pattern that is being searched by search()


#the ? search for 1 or 0 time it appeared in the string
#the * means 0 or more times, ? means 0 or 1 time and + means 1 or more times


#batRegex = re.compile(r'Bat(wo)?man')  #Batman|Batwomen can be written as Bat(wo)?man
#mo = batRegex.search('The Adventures of Batman and Batwoman')  #so it will find Both Batman/woman but not Batwowowowoman
#print(mo.group())


#to search something a definite number of time use (thing that you want to search){specify number of times here} this type of pattern
#here the ha will be searched for 3 times in the provided text
# (ha){3} is equal to hahaha but (ha){3} is really short handed and it gets easy if you have long pattern of same type, so insted of typing that pattern and making it more complicate to read we use the short hand method
#regex = re.compile(r'(ha){3}')
#mo = regex.search('he said hahaha')
#print (mo.groups())



# (pattern){at least number, at most number}
# ex. (ha){3,5} will match ha of inclusive times from 3 to 5
# if no. of time of pattern is not in given range then it will match no. of times greater than the at most value and return the search upto the at most no. of times but will not match no. of times less the at least value.
# for above pattern type hahahahahaha will match which is 6 times 'ha' but will return 'hahahahaha' which is 5 times 'ha', on the other hand haha will not match
# also {,5} == {0,5} & {3,} == {3,more no. of times}, like we do slicing of lists

# maximum longest possible search is return which is a greedy match
# ex. (\d){3,5} will match upto 5 for search('123456789') which is '12345'
# for non-greedy match use ? 
# ex. (\d){3,5}? will match upto 3 for search('123456789') which is '123'



# Character Classes :-
# \d - Any nueric digit from 0 to 9
# \D - Any Character that is not a numeric Digit from 0 to 9
# \w - Any word(letter,digit,underscore)
# \W - Any character that is not a letter,digit or underscore
# \s - Any space,tab or newline
# \S - Any character that is not space,tab,newline

# Creating own character class
# ex. vowelRegex = re.compile(r'[aeiouAEIOU]')
# so to create any charater class that you want, just put it in square brackets[]
# Also if you put ^ before you character class it will make it a -ve Character class
# ex. r'[^aeiouAEIOU], it will match for character that doesn't match vowel(pattern provided) including space,puntuations,digit etc.
# or in simplee word r'[^anything] this will match anything that is not included in sqaure brackets(opposite of [anything] is [^anything]).



# beginsWithCharacter - r'^Character'  // ^ will match if the string that is to be search begins with the given pattern, otherwise it will return None
# endsWithCharacter - r'Character$'  // $ will match if the string that is to be search ends with the given pattern, otherwise it will return None
# . - Any single character except newline
# to match any single character including newline with . is to give compile 2nd argument -- re.compile(r'.*',re.DOTALL)

# .* - find all character (performs greedy match)
# .*? - find all character (performs non-greedy match)

# 2nd arguments for re.compile(pattern,2nd Argument), 2nd argument are listed below:
# 1. re.DOTALL - match any character include newlinee
# 2. re.IGNORECASE/re.I - ignores case sensivity rule(matchs lower and upper case)
# 3. re.VERBOSE - can use multi-line(triple quotes) to specify the pattern and also use comment to make pattern readable 
# 4. re.I | re.DOTALL | re.VERBOSE - use '|' if you want to pass more than 1 argument to re.compile() method


# find & replace with regex can be done by sub() method
# ex. regex.sub('replacement string','sting that contain the replacement sting')
# sub() will replace the sting which match the pattern with the replacement string and return the whole new replaced string
# \1,\2....\n can be use to replace the sting with the groups respectively that findall() found
