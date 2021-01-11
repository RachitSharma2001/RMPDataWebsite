from bs4 import BeautifulSoup
import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import sys

school_list = ["UC Berkeley", "UC Davis", "UC Irvine", "UCLA", "UC Riverside", "UC Santa Barbara", "UC Santa Cruz", "UC San Diego"]

for i in range(8):
    school_id = 1072 + i
    school_id_str = str(school_id)
   
    department_ratings = {}
    department_num_professors = {}
    current_dep_list = []
    
    num_pages = 1
    curr_num_professors = 0
    num_dep = 0

    #print("Department ratings for ", school_list[i], ":")
    while(True):
        url = 'https://www.ratemyprofessors.com/filter/professor/?&page=' + str(num_pages) + '&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=' + school_id_str
        page = requests.get(url)
        page_txt = page.text
        json_row = json.loads(page_txt)
        j = 0
        
        while(True):
            department = ""
            try:
                department = json_row["professors"][j]["tDept"]
            except:
                break

            department = json_row["professors"][j]["tDept"]
            score_str = json_row["professors"][j]["overall_rating"]
            num_ratings = json_row["professors"][j]["tNumRatings"]
            
            if(score_str != "N/A"):
                score = float(score_str)

                if(department in current_dep_list):
                    curr_numerator = department_ratings[department]
                    curr_total = curr_numerator + score*num_ratings

                    department_ratings[department] = curr_total
                    department_num_professors[department] += num_ratings
                else:
                    current_dep_list.append(department)
                    department_num_professors[department] = num_ratings
                    department_ratings[department] = score*num_ratings
                    num_dep += 1
                    
            j += 1
            
        if(json_row["remaining"] == 0):
            break
       
        num_pages += 1

    #print(current_dep_list)
    sorted(department_ratings, key=lambda dep: dep[1])    
    for dep, avg_score in department_ratings.items():
        print(school_list[i], dep)
        print(float(avg_score/department_num_professors[dep]))

    print("---------------------------------------------------------------------")      
