#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. create a python class called circle with constructor which will take a list as an argument for the task  the list is 
# [10, 501, 22, 37, 100 ,999, 87, 351]


# In[3]:


class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * r**2 for r in self.radius_list]
        return areas


radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

areas = circle_instance.calculate_area()

for i, radius in enumerate(radius_list):
    print(f"The area of a circle with radius {radius} is {areas[i]:.2f}")


# In[ ]:


# 2. create proper member variable inside the task if required and use them when necessary. 
# for example this task create a class private variable name pi=3.141


# In[4]:


class Circle:
    def __init__(self, radius):
        self.__pi = 3.141  
        self.radius = radius

    def calculate_area(self):
        
        area = self.__pi * (self.radius ** 2)
        return area

    def calculate_circumference(self):
        
        circumference = 2 * self.__pi * self.radius
        return circumference


circle = Circle(5)


area = circle.calculate_area()
circumference = circle.calculate_circumference()

print("Area:", area)
print("Circumference:", circumference)


# In[ ]:


# 3. from the given list create two class methods area and perimeter which will be going 
# to calculate the  area and radius


# In[6]:


class GeometryCalculator:
    @staticmethod
    def area(shape_type, dimensions):
        if shape_type == "rectangle" and len(dimensions) == 2:
            length, width = dimensions
            return length * width
        elif shape_type == "circle" and len(dimensions) == 1:
            radius = dimensions[0]
            return 3.141 * radius * radius
        else:
            return "Invalid shape or dimensions."

    @staticmethod
    def perimeter(shape_type, dimensions):
        if shape_type == "rectangle" and len(dimensions) == 2:
            length, width = dimensions
            return 2 * (length + width)
        elif shape_type == "circle" and len(dimensions) == 1:
            radius = dimensions[0]
            return 2 * 3.141 * radius
        else:
            return "Invalid shape or dimensions."

    @staticmethod
    def calculate_radius(area):
        return (area / 3.141) ** 0.5


rectangle_dimensions = [5, 3]
circle_dimensions = [12.566]  

rectangle_area = GeometryCalculator.area("rectangle", rectangle_dimensions)
rectangle_perimeter = GeometryCalculator.perimeter("rectangle", rectangle_dimensions)
circle_area = GeometryCalculator.area("circle", circle_dimensions)
circle_perimeter = GeometryCalculator.perimeter("circle", circle_dimensions)
circle_radius = GeometryCalculator.calculate_radius(circle_area)

print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)
print("Circle Radius:", circle_radius)


# In[ ]:


# 4. kindly visit the below URL and convert the UML diagram into a python class and its methods.


# In[7]:


class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  
        self.inches = 0 
        self.on = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"LED TV Details: {self.brand}, {self.inches} inches, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"Plasma TV Details: {self.brand}, {self.inches} inches, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"


led_tv = LedTV("Samsung", "Thin", "Low", "5 years", "60Hz")
plasma_tv = PlasmaTV("Panasonic", "Medium", "Moderate", "7 years", "180 degrees", "Full Array")

print(led_tv.status())
led_tv.increase_volume()
led_tv.set_channel(8)
print(led_tv.status())
print(led_tv.display_details())

print(plasma_tv.status())
plasma_tv.decrease_volume()
plasma_tv.reset_tv()
print(plasma_tv.status())
print(plasma_tv.display_details())


# In[ ]:





# In[ ]:





# In[ ]:




