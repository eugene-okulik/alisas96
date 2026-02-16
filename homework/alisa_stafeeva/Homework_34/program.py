import requests
from decimal import Decimal, ROUND_HALF_UP
from time import sleep
from datetime import datetime


url = "https://www.cbr-xml-daily.ru/latest.js"
while True:
    response = requests.get(url)
    data = response.json()
    rate = data["rates"]["USD"]
    dollar = Decimal(1) / Decimal(str(rate))
    dollar_rounded = dollar.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"{datetime.now()} Курс доллара: {dollar_rounded}$")
    sleep(2)
