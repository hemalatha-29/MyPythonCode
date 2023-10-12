#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Calculate Total Number of Vowels


# In[1]:


str=input("enter string")
vowels="aeiou"
d=dict()
d=d.fromkeys(vowels,0)
for char in str:
    if char in vowels:
        d[char]+=1
print(d)


# In[ ]:


# 2. write a function that takes a string and returns a new string will all the vowels removed.


# In[12]:


string="Guvi Geeks Network Private Limited"
vowels =['a','e','i','o','u']
result=""
for char in string:
    if char not in vowels:
        result+=char
print(result)


# In[ ]:


# 3. Write a function that takes a string and returns the number of unique characters in it.


# In[13]:


string="Guvi Geeks Network Private Limited"
count=0
temp=[]
for i in string:
    if(i not in temp):
        count+=1
        temp.append(i)
print('Total Unique Characters Count:',count)


# In[ ]:


# 4. write a function that takes a string and returns True if it is a palindrome,false othrwise.


# In[45]:


def is_palindrome(s):
    
    if len(s) < 1:
        
        return True
    else:
        
        if s[0] == s[-1]:
            
            return is_palindrome(s[1:-1])
        else:
        
         return False

if(is_palindrome ==True):
    
    print("String is a palindrome!")

else:
    
    print("String is not a palindrome!")


# In[ ]:


# 5. write a function that takes two strings and returns the longest common substring between them.


# In[29]:


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

   
    max_len = 0
    end_pos = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i

    
    longest_substring = str1[end_pos - max_len:end_pos]

    return longest_substring

str1 = "abcdef"
str2 = "abefcde"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)


# In[ ]:


# 6. Write a function that takes a string and returns the most frequent charcater in it.


# In[127]:


string=input("Enter a string:")
count = {}
for letter in string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print("Count Frequency is ...")
for key,value in count.items():
    print(f"{key} occurs {value} times")


# In[ ]:


# 7. write a function that takes a string and returns True if it is an anagram of another string, False otherwise


# In[30]:


def is_anagram(str1, str2):
  
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)

if result:
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')


# In[ ]:


# 8. create a pyramid of numbers from 1 to 20 using For loop?


# In[39]:



total_rows = 6


current_number = 1


for i in range(1, total_rows + 1):
   
    print(" " * (total_rows - i), end="")

    for j in range(1, i + 1):
        print(current_number, end=" ")
        current_number += 1
        if current_number > 20:
            break

    print()


# In[ ]:


# 9. write a function that takes a string and returns the number of words in it


# In[40]:


def count_words(input_string):
   
    words = input_string.split()
    
    return len(words)


input_string = "This is a sample sentence."
word_count = count_words(input_string)
print("Number of words:", word_count)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




