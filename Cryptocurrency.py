import requests
import json
#
result = requests.get('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc')
data = json.loads(result.text)


print(data)
iiii = data['bitcoin']['usd']
print(iiii)
