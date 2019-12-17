import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xmltodict
import json

url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
queryParams = '?' + '&ServiceKey='+'GWU1bJv%2B0m3Z9vtOX5pgNQSR%2FDuv9X6%2BZOjcqEpCkNXzR1EIOgafKBKuMlRjoLIyJlmBibi59h2rg96Qfo8GZQ%3D%3D'\
              + '&pageNo='+'11'\
              + '&numOfRows='+'10'\
              + '&addr='+'전라남도 나주시 전력로 55'\

url = url + queryParams
result = requests.get(url)
dict_type = xmltodict.parse(result.content)
json_type = json.dumps(dict_type)
dict2_type = json.loads(json_type)

body = dict2_type['response']['body']
items = body['items']

for item in items["item"]:
    print(item)







