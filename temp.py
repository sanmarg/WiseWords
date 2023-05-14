import requests, markdown
#This code is for parsing the readme file from github and show as doccumentation. 

url='https://raw.githubusercontent.com/lukePeavey/quotable/master/README.md'
response = requests.get(url)
content = response.text

html = markdown.markdown(content)

with open("temp.html", "w", encoding="utf-8") as file:
    file.write(html)