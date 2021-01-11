import json
import matplotlib.pyplot as plt
import numpy as np

school_list = ["UC Berkeley", "UC Davis", "UC Irvine", "UCLA", "UC Riverside", "UC Santa Barbara", "UC Santa Cruz", "UC San Diego"]

overall_departments = open("OverallRatings.txt", "r")                 
search_department = input()
search_term = school_list[0] + " " + search_department
school_list_id = 0

average_ratings = {}

with open("OverallRatings.txt") as overall_departments:
    college_dep = f.read()
    ratings = f.read()

    if(college_dep == search_term):
        average_ratings[college_dep]
        search
    
    

'''    
sorted(department_ratings, key=lambda dep: dep[1])    
for dep, avg_score in department_ratings.items():
    print(dep, avg_score, department_num_professors[dep])

print("---------------------------------------------------------------------")      
'''
