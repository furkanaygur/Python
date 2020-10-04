import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

From = input(" [USD , EUR , TRY etc.] From :")
to = input(" [USD , EUR , TRY etc.] To :")
Amount = int(input(" Amount :"))

result = requests.get(api_url + From)
result = json.loads(result.text)

print(f" 1 {From} = {result['rates'][to]} {to}")
print(f" {Amount} {From} = {Amount * result['rates'][to]} {to}")
