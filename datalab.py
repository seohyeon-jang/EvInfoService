import os
import sys
import urllib.request

client_id = "zweGvwF1KOx4oT08AwJ2"
client_secret = "XUC585A3sx"

url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2019-01-01\",\"endDate\":\"2019-11-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"전기차\",\"keywords\":[\"충전소\"]}]}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",'zweGvwF1KOx4oT08AwJ2')
request.add_header("X-Naver-Client-Secret",'XUC585A3sx')
request.add_header("Content-Type","application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
