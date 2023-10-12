#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Given python list even and odd nos


# In[6]:


list1 = [10, 501, 22, 37, 100, 999, 87, 351]

even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list1: ", even_nos)


# In[8]:


list2 = [10, 501, 22, 37, 100, 999, 87, 351]

only_odd = [num for num in list2 if num % 2 == 1]

print(only_odd)


# In[ ]:


# 2. count all the prime numbers and which will contain all the prime numbers.


# In[12]:


my_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime=[]
for i in my_list :
    c=0
    for j in range (1,i):
        if i%j==0:
            c+=1
    if c==1 :
        prime.append(i)
print(prime)


# In[28]:


def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2,int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes
print([i for i in range (2,50) if 0 not in [i%n for n in range(2,i)]])


# In[ ]:


# 3. Write a python program to find the sum of the first and last digit of an integer.


# In[4]:


number = 124789
number = str(number)
first_digit = int(number[0])
last_digit = int(number[-1])
addition = first_digit + last_digit
print('Addition of first and last digit of the number is', addition)


# In[ ]:


# 4. find the duplicates in the three lists. 


# In[6]:


l=[1,2,3,4,5,2,3,5,6,7,8,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


# In[ ]:


# 5. find if there is a sub - list with sum equal to zero


# In[41]:


size=int(input())
numbers=list(map(int,input().split()))
print(numbers)
sublists=[]
result=0
for i in range(0,size+1):
    for j in range(i+1,size+1):
        sublists.append(numbers[i:j])
for i in sublists:
    if sum(i)==0:
        print("yes")
        print(i)
        result=1
if result==0:
    print("No")


# In[ ]:


# 6. find the triplet


# In[47]:


def findTriplets(lst, k):
    triplet_count = 0
    final_temp_list =[]
    for i in range(0, len(lst)-1): 
        s = set() 
        temp_list = []
        temp_list.append(lst[i])
 
        curr_k = k - lst[i] 
         
        for j in range(i + 1, len(lst)): 
             
            if (curr_k - lst[j]) in s: 
                triplet_count += 1
                temp_list.append(lst[j])
                temp_list.append(curr_k - lst[j])
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(lst[j])
             
    return final_temp_list
lst = [10, 20, 30, 9]
k = 59
print(findTriplets(lst, k))

 


# In[ ]:


# 7. find the minimum element in a rated and sorted list?


# In[61]:


def countRotations(arr, n): 
     if (arr[0] > arr[n - 1]): 
            for i in range(0, n): 
                if (arr[i] > arr[i + 1]): 
                    return i + 1

arr = [15, 18, 2, 3, 6, 12] 
n = len(arr) 
print(countRotations(arr, n))  


# In[ ]:


# 8. find the first non - repeating elements in a given list of integers?


# In[63]:


def nonrepeat(string):
    freq = {}
    for x in string:
        freq[x] = freq.get(x,0) + 1
    for i in string:
        if freq[i] == 1:
            return i
    return -1
print(nonrepeat('abcdabcefg'))
        
    


# In[ ]:


# 9. distribute the mangoes in such a way that each student gets one Bag. the difference between the number fo mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is minimum?


# In[105]:


def distribute_mangoes(mangoes, M):

    mangoes.sort()
    

    min_diff = float('inf')
    best_distribution = []
    
    for i in range(len(mangoes) - M + 1):

        current_diff = mangoes[i + M - 1] - mangoes[i]
        
        if current_diff < min_diff:
            min_diff = current_diff
            best_distribution = mangoes[i:i+M]
    
    return best_distribution

N = [5, 12, 15, 7, 3, 9, 20]
M = 3 

result = distribute_mangoes(N, M)
print("Distribution of mangoes with the minimum difference:", result)


# In[ ]:


# 10. find out how many numbers are there in the given python list which are happy numbers?


# In[24]:


def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def find_happy_numbers(numbers):
    happy_numbers = []
    for num in numbers:
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Find the happy numbers in the list
happy_numbers = find_happy_numbers(numbers)

print("The happy numbers are:", happy_numbers)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




