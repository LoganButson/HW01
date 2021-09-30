import requests
#Feeding First URL
page1 = "https://api.github.com/users/emaadmanzoor/repos?page=1&per_page=100"
data_json1 = requests.get(page1)
parsed_data1 = data_json1.json()
#Feeding Second URL
page2 = "https://api.github.com/users/emaadmanzoor/repos?page=2&per_page=100"
data_json2 = requests.get(page2)
parsed_data2 = data_json2.json()
#Count One
sum1 = 0
for i in parsed_data1:
 sum1 = sum1 + i["stargazers_count"]
 #Count Two
sum2 = 0
for i in parsed_data2:
 sum2 = sum2 + i["stargazers_count"]
 
#Adding together
print(sum1+sum2)
