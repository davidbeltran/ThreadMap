from polygon import RESTClient
import time

client = RESTClient("Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA")

tickers = []
#for t in client.list_tickers(
# for t in client.list_tickers(
# 	market="stocks",
# 	active="true",
# 	order="asc",
# 	limit="100",
# 	sort="ticker",
# 	):
#     tickers.append(t)
#     time.sleep(1)

# print(tickers)
try:
    response = client.list_tickers(limit=1)  # Minimal request
    print("API connection successful:", response)
except Exception as e:
    print("API connection error:", str(e))
