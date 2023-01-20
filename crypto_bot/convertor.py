import requests
import json
from config import keys
class ConvertionExcteption(Exception):
  pass

class Convertor:

  def get_price(base, quote, amount):
    url = "https://api.apilayer.com/currency_data/convert?to="+str(base)+"&from="+str(quote)+"&amount="+str(amount)+""

    if quote == base:
      raise ConvertionExcteption(f'Невозможно перевести одинаковые валюты {base}.')
    try:
      quote_ticker = keys[quote]
    except KeyError:
      raise ConvertionExcteption(f'не удалось обработать валюту {quote}')
    try:
      base_ticker = keys[base]
    except KeyError:
      raise ConvertionExcteption(f'не удалось обработать валюту {base}')


    payload = {}
    headers= {
      "apikey": "QRnSdIWKc6AR8XIUzyaCFEyt5thwUeL0"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    result = response.text
    json_map = json.loads(result)
    return json_map.get("result")


