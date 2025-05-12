from polygon import RESTClient
import time
import pprint
import re

client = RESTClient("Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA")
vowels = r'^[aeiouAEIOU]\w*'

tickers = []
count = 0
# for t in client.list_tickers(
# 	market="stocks",
# 	active="true",
# 	order="asc",
# 	limit="100",
# 	sort="ticker",
# 	):
#     tickers.append(t)
#     count += 1
#     time.sleep(.1)
#     if count > 10:
#         break
    
matches = [s for s in client.list_tickers(market="stocks",active="true",order="asc",limit="100",sort="ticker",) if re.match(vowels, s.ticker)]
print(matches)
# pprint.pprint(tickers[8].ticker)



# try:
#     response = client.list_tickers(limit=1)  # Minimal request
#     print("API connection successful:", response)
# except Exception as e:
#     print("API connection error:", str(e))
