import requests
from datetime import datetime, timedelta

current = datetime.now()
url_template = "https://simurg.space/gen_file?data=obs&date={date}"
while True:
    date = now.strftime("%Y-%m-%d")
    url = url_template.format(date=date)

    response = requests.get(url = url, stream = True)
    print(f"For {date} got: ", response)
    if response.status_code == 200:
        print("Last available data are for {date}")
        break
    else:
        current = current - timedelta(days = 1)