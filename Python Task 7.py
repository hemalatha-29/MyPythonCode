#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. write a python program using function to which will do the following: 
# a) The file content should have the content of the current timestamp


# In[33]:


from datetime import datetime
timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(timestr)


# In[ ]:


# b) The function will create a text file with current timestamp


# In[34]:


from datetime import datetime
timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(timestr)
file_name = "mydata"+timestr+".text"
print(file_name)


# In[ ]:





# In[ ]:


# 2. write another python  function to read from a text file. The function will take the name of text file and display 
# the content of the file into the console


# In[51]:


def read_text_file(file_name):
    
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


file_name = "example.txt"  
read_text_file(file_name)


# In[ ]:





# In[ ]:




