from bs4 import BeautifulSoup
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

school_list = ["UC Berkeley", "UC Davis", "UC Irvine", "UCLA", "UC Riverside", "UC Santa Barbara", "UC Santa Cruz", "UC San Diego"]
avg_rating_list = []
for i in range(8):
    school_id = 1072 + i
    school_id_str = str(school_id)
    url = 'https://solr-aws-elb-production.ratemyprofessors.com//solr/rmp/select/?solrformat=true&rows=10000&wt=json&json.wrf=noCB&callback=noCB&q=*%3A*+AND+schoolid_s%3A' + school_id_str + '&defType=edismax&qf=teacherfirstname_t%5E2000+teacherlastname_t%5E2000+teacherfullname_t%5E2000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=averageratingscore_rf+desc&siteName=rmp&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s&fq='
    page = requests.get(url)
    page_txt = page.text
    json_save = json.loads(page_txt[5:len(page_txt) - 1])
    numProfessors = json_save["response"]["numFound"]

    avgScore = float(0)
    divisor = 0

    professor_ratings = []
    num_of_ratings = []
    for j in range(numProfessors):
        tot_num_ratings = json_save["response"]["docs"][j]["total_number_of_ratings_i"]
        if(tot_num_ratings == 0):
            continue
        specificAvgScore = json_save["response"]["docs"][j]["averageratingscore_rf"]
        professor_ratings.append(specificAvgScore)
        num_of_ratings.append(tot_num_ratings)

    avgScore = np.average(professor_ratings, weights=num_of_ratings)
    avg_rating_list.append(avgScore)
    print(school_list[i], " :     ", avgScore)

plt.figure(figsize=[14,5])
plt.xlabel("Colleges")
plt.ylabel("Average Ratings of all professors")
plt.bar(school_list, avg_rating_list)
plt.show()
