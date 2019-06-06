

import requests
import selenium
text = requests.get("http://www.bet-scan.com")
print(text.content)


selenium.webdriver.