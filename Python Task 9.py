#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. what is the expected output of the following python code given below:                                                     
  # data =  [10, 501,  22,  37, 100,999,87,351]                                                                                                                
   # result = filter (lambda x:  x > 4 , data )                                                                                             
   # print(list(result))


# In[1]:


[10, 501, 22, 37, 100, 999, 87, 351]


# In[ ]:


# 2. write a python code using lambda function to check very element of a list is an integer or string? write a python code


# In[2]:


my_list = [10, "Hello", 42, "World", 123]

check_type = lambda x: isinstance(x, int) or isinstance(x, str)
result = all(map(check_type, my_list))

if result:
    print("All elements are either integers or strings.")
else:
    print("Not all elements are integers or strings.")


# In[ ]:


# 3.  using the python Lambda function create a Fibonacci series from 1 to 50 elements write a python code


# In[15]:


from functools import reduce


n = 50


fib = lambda x: reduce(lambda a, _: a + [a[-1] + a[-2]], range(x - 2), [0, 1])


fibonacci_series = fib(n)


print(fibonacci_series)


# In[ ]:


# 4. write a python function to validate the regullar expression for the following:-
# a.) Email Address
# b.) Mobile numbers of Bangladesh
# c.) Telephone numbers of USA 
# d.) 16 character Alpha-Numeric password composed of alphabets of Upper Case,lowercase,special characters,Numbers write python code


# In[14]:





def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))


def is_valid_bangladesh_mobile_number(number):
    # Bangladeshi mobile numbers start with 01 and are followed by 8 more digits
    bd_mobile_regex = r'^01\d{8}$'
    return bool(re.match(bd_mobile_regex, number))

def is_valid_usa_telephone_number(number):
    # US telephone numbers with or without dashes (e.g., 123-456-7890 or 1234567890)
    usa_telephone_regex = r'^\d{3}-?\d{3}-?\d{4}$'
    return bool(re.match(usa_telephone_regex, number))


def is_valid_password(password):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{16}$'
    return bool(re.match(password_regex, password))


email = "example@email.com"
mobile_number = "01712345678"
usa_telephone = "123-456-7890"
password = "Aa@12345678901234"

print(f"Email is valid: {is_valid_email(email)}")
print(f"Bangladesh Mobile number is valid: {is_valid_bangladesh_mobile_number(mobile_number)}")
print(f"USA Telephone number is valid: {is_valid_usa_telephone_number(usa_telephone)}")
print(f"Password is valid: {is_valid_password(password)}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




