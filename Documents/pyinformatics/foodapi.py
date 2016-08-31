# first project using apis
import urllib
import json

k=str(raw_input("enter country"))
z=str(raw_input("enter locality"))
k=k.replace(' ','%20')
z=z.replace(' ','%20')
m='country='+k+"&locality="
m=m+z
y='https://api.locu.com/v1_0/venue/search/?'+m+'&category=RESTAURANT&api_key=b60e865fe41dfd85daead33a8b30123869f2e37c'
locu_api='b60e865fe41dfd85daead33a8b30123869f2e37c'
x=urllib.urlopen(y)
js=json.load(x)
for i in js['objects']:
     print i['name']

