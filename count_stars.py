import requests
url1 = "https://api.github.com/users/emaadmanzoor/repos?page=1&per_page=100"
data_json1 = requests.get(url1)
data1 = data_json1.json()
url2 = "https://api.github.com/users/emaadmanzoor/repos?page=2&per_page=100"
data_json2 = requests.get(url2)
data2 = data_json2.json()
sum1 = 0
for i in data1:
 sum1 = sum1 + i["stargazers_count"]
sum2 = 0
for i in data2:
 sum2 = sum2 + i["stargazers_count"]
print(sum1+sum2)
