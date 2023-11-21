#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[ ]:


# https://restcountries.com/v3.1/all  write a python Program which will do the following:-


# In[2]:


# 1.Using the OOPS Concept for the following task.


# In[3]:


import requests

class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_countries(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                countries = []
                for country_data in countries_data:
                    name = country_data['name']['common']
                    capital = country_data['capital'][0] if 'capital' in country_data else 'N/A'
                    population = country_data['population'] if 'population' in country_data else 'N/A'
                    country = Country(name, capital, population)
                    countries.append(country)
                return countries
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error: {e}")
            return []


api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)
countries = country_api.get_countries()


for country in countries:
    print(country)


# In[ ]:





# In[ ]:


# 2. Use the class Constructor for taking input the above mentioned URL 


# In[2]:


import requests

class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_countries(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                countries = []
                for country_data in countries_data:
                    name = country_data['name']['common']
                    capital = country_data['capital'][0] if 'capital' in country_data else 'N/A'
                    population = country_data['population'] if 'population' in country_data else 'N/A'
                    country = Country(name, capital, population)
                    countries.append(country)
                return countries
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error: {e}")
            return []


api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)
countries = country_api.get_countries()

for country in countries:
    print(country)


# In[ ]:


# 3. Create a method that will fetch all the JSON data from the URL mentioned above


# In[1]:


import requests

class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url
        self.countries = []
        self.fetch_data()

    def fetch_data(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                for country_data in countries_data:
                    name = country_data['name']['common']
                    capital = country_data.get('capital', ['N/A'])[0]
                    population = country_data.get('population', 'N/A')
                    country = Country(name, capital, population)
                    self.countries.append(country)
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def get_countries(self):
        return self.countries

    def fetch_all_data(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None


api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)


all_data = country_api.fetch_all_data()


if all_data:
    for country_data in all_data[:3]:
        print(country_data)


# In[ ]:


# 4. create a method that will display the name of countries,currencies & currency symbols


# In[18]:


import requests

class Country:
    def __init__(self, name, capital, population, currencies):
        self.name = name
        self.capital = capital
        self.population = population
        self.currencies = currencies

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}, Currencies: {self.currencies}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url
        self.countries = []
        self.fetch_data()

    def fetch_data(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                for country_data in countries_data:
                    name = country_data.get('name', {}).get('common', 'N/A')
                    capital = country_data.get('capital', {}).get('0', 'N/A') if isinstance(country_data.get('capital'), dict) else 'N/A'
                    population = country_data.get('population', 'N/A')
                    currencies_data = country_data.get('currencies', [])
                    currencies = self.extract_currencies(currencies_data)
                    country = Country(name, capital, population, currencies)
                    self.countries.append(country)
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def get_countries(self):
        return self.countries

    def extract_currencies(self, currencies_data):
        if isinstance(currencies_data, list):
            return [(curr.get('name', 'N/A'), curr.get('symbol', 'N/A')) for curr in currencies_data]
        elif isinstance(currencies_data, dict):
            return [(code, currencies_data[code].get('symbol', 'N/A')) for code in currencies_data.keys()]
        return []

    def display_country_info(self):
        for country in self.countries:
            print(country)

    def display_countries_currencies_symbols(self):
        print("Countries, Currencies, and Currency Symbols:")
        for country in self.countries:
            print(f"{country.name}:")
            for currency, symbol in country.currencies:
                print(f"  Currency: {currency}, Symbol: {symbol}")
            print()

api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)

country_api.display_countries_currencies_symbols()


# In[ ]:





# In[ ]:


# 5. create a method that will display all those countries which have DOLLAR as its currency.


# In[16]:


import requests

class Country:
    def __init__(self, name, capital, population, currencies):
        self.name = name
        self.capital = capital
        self.population = population
        self.currencies = currencies

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}, Currencies: {self.currencies}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url
        self.countries = []
        self.fetch_data()

    def fetch_data(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                for country_data in countries_data:
                    name = country_data.get('name', {}).get('common', 'N/A')
                    capital = country_data.get('capital', {}).get('0', 'N/A') if isinstance(country_data.get('capital'), dict) else 'N/A'
                    population = country_data.get('population', 'N/A')
                    currencies_data = country_data.get('currencies', [])
                    currencies = self.extract_currencies(currencies_data)
                    country = Country(name, capital, population, currencies)
                    self.countries.append(country)
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def get_countries(self):
        return self.countries

    def extract_currencies(self, currencies_data):
        if isinstance(currencies_data, list):
            return [curr.get('code', 'N/A') for curr in currencies_data if curr.get('code')]
        elif isinstance(currencies_data, dict):
            return [code for code in currencies_data.keys() if code]
        return []

    def display_country_info(self):
        for country in self.countries:
            print(country)

    def display_countries_with_dollar(self):
        dollar_countries = [country for country in self.countries if 'USD' in country.currencies]
        if dollar_countries:
            print("Countries with DOLLAR as currency:")
            for country in dollar_countries:
                print(country)
        else:
            print("No countries found with DOLLAR as currency.")

api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)

country_api.display_countries_with_dollar()


# In[ ]:


# 6. Create a method that will display all those countries which have EURO as its currency


# In[17]:


import requests

class Country:
    def __init__(self, name, capital, population, currencies):
        self.name = name
        self.capital = capital
        self.population = population
        self.currencies = currencies

    def __str__(self):
        return f"Country: {self.name}, Capital: {self.capital}, Population: {self.population}, Currencies: {self.currencies}"

class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url
        self.countries = []
        self.fetch_data()

    def fetch_data(self):
        
            response = requests.get(self.api_url)
            if response.status_code == 200:
                countries_data = response.json()
                for country_data in countries_data:
                    name = country_data.get('name', {}).get('common', 'N/A')
                    capital = country_data.get('capital', {}).get('0', 'N/A') if isinstance(country_data.get('capital'), dict) else 'N/A'
                    population = country_data.get('population', 'N/A')
                    currencies_data = country_data.get('currencies', [])
                    currencies = self.extract_currencies(currencies_data)
                    country = Country(name, capital, population, currencies)
                    self.countries.append(country)
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def get_countries(self):
        return self.countries

    def extract_currencies(self, currencies_data):
        if isinstance(currencies_data, list):
            return [curr.get('code', 'N/A') for curr in currencies_data if curr.get('code')]
        elif isinstance(currencies_data, dict):
            return [code for code in currencies_data.keys() if code]
        return []

    def display_country_info(self):
        for country in self.countries:
            print(country)

    def display_countries_with_euro(self):
        euro_countries = [country for country in self.countries if 'EUR' in country.currencies]
        if euro_countries:
            print("Countries with EURO as currency:")
            for country in euro_countries:
                print(country)
        else:
            print("No countries found with EURO as currency.")

api_url = 'https://restcountries.com/v3.1/all'
country_api = CountryAPI(api_url)


country_api.display_countries_with_euro()


# In[ ]:


# https://www.openbrewerydb.org/  write a python script which will do the following:


# In[ ]:


# 1. list the names of all breweries present in the states of Alaska, Maine and new york 



# In[19]:


import requests

def get_breweries_in_states(states):
    base_url = 'https://api.openbrewerydb.org/breweries'
    breweries = []

    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            breweries.extend(response.json())
        else:
            print(f"Error: Unable to fetch data for {state}. Status Code: {response.status_code}")

    return breweries

def display_brewery_names(breweries):
    print("Brewery Names:")
    for brewery in breweries:
        print(brewery.get('name', 'N/A'))


target_states = ['Alaska', 'Maine', 'New York']

breweries_in_states = get_breweries_in_states(target_states)


display_brewery_names(breweries_in_states)


# In[ ]:





# In[ ]:


# 2. what is the count of breweries in each of the states mentioned above


# In[20]:


import requests

def get_breweries_in_states(states):
    base_url = 'https://api.openbrewerydb.org/breweries'
    breweries = []

    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            breweries_data = response.json()
            breweries.extend(breweries_data)
            print(f"Number of breweries in {state}: {len(breweries_data)}")
        else:
            print(f"Error: Unable to fetch data for {state}. Status Code: {response.status_code}")

    return breweries

def display_brewery_names(breweries):
    print("\nBrewery Names:")
    for brewery in breweries:
        print(brewery.get('name', 'N/A'))


target_states = ['Alaska', 'Maine', 'New York']


breweries_in_states = get_breweries_in_states(target_states)

display_brewery_names(breweries_in_states)


# In[ ]:


# 3. count the number of types of breweries present in individual cities of the state mentioned above 


# In[21]:


import requests

def get_breweries_in_states(states):
    base_url = 'https://api.openbrewerydb.org/breweries'
    breweries = []

    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            breweries_data = response.json()
            breweries.extend(breweries_data)
            print(f"Number of breweries in {state}: {len(breweries_data)}")
        else:
            print(f"Error: Unable to fetch data for {state}. Status Code: {response.status_code}")

    return breweries

def count_brewery_types_by_city(breweries):
    city_brewery_count = {}

    for brewery in breweries:
        city = brewery.get('city', 'N/A')
        brewery_type = brewery.get('brewery_type', 'N/A')

        if city not in city_brewery_count:
            city_brewery_count[city] = {}

        if brewery_type not in city_brewery_count[city]:
            city_brewery_count[city][brewery_type] = 1
        else:
            city_brewery_count[city][brewery_type] += 1

    return city_brewery_count

target_states = ['Alaska', 'Maine', 'New York']


breweries_in_states = get_breweries_in_states(target_states)

city_brewery_count = count_brewery_types_by_city(breweries_in_states)


print("\nNumber of brewery types in individual cities:")
for city, types_count in city_brewery_count.items():
    print(f"\nCity: {city}")
    for brewery_type, count in types_count.items():
        print(f"  {brewery_type}: {count}")


# In[ ]:


# 4. Count and list how many breweries have websites in the states of Alaska, Maine and New York.


# In[22]:


import requests

def get_breweries_in_states(states):
    base_url = 'https://api.openbrewerydb.org/breweries'
    breweries = []

    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            breweries_data = response.json()
            breweries.extend(breweries_data)
            print(f"Number of breweries in {state}: {len(breweries_data)}")
        else:
            print(f"Error: Unable to fetch data for {state}. Status Code: {response.status_code}")

    return breweries

def count_and_list_websites_by_state(breweries):
    state_website_count = {}

    for brewery in breweries:
        state = brewery.get('state', 'N/A')
        has_website = 'website_url' in brewery and brewery['website_url'] is not None

        if state not in state_website_count:
            state_website_count[state] = {'total': 0, 'with_website': 0, 'without_website': 0}

        state_website_count[state]['total'] += 1

        if has_website:
            state_website_count[state]['with_website'] += 1
        else:
            state_website_count[state]['without_website'] += 1

    return state_website_count

target_states = ['Alaska', 'Maine', 'New York']


breweries_in_states = get_breweries_in_states(target_states)


state_website_count = count_and_list_websites_by_state(breweries_in_states)


print("\nBrewery websites in individual states:")
for state, counts in state_website_count.items():
    print(f"\nState: {state}")
    print(f"  Total Breweries: {counts['total']}")
    print(f"  Breweries with Websites: {counts['with_website']}")
    print(f"  Breweries without Websites: {counts['without_website']}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




