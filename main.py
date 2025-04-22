from polygon import RESTClient
import time

client = RESTClient("Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA")

tickers = []
cursor = None
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

while True:
    # Make API call without the 'cursor' argument
    response = client.list_tickers(
        market="stocks",
        active="true",
        order="asc",
        limit=100,
        sort="ticker"
    )
    
    # Add tickers to the list
    tickers.extend(response)
    
    # Check for the next page of results
    if not response.next_url:  # Adjust if 'next_url' is named differently
        break
    
    # Update cursor for the next API call
    cursor = response.next_url
    client.request(cursor)  # Replace with correct way to call the next URL
    time.sleep(1)  # Pause to avoid rate limits



# try:
#     response = client.list_tickers(limit=1)  # Minimal request
#     print("API connection successful:", response)
# except Exception as e:
#     print("API connection error:", str(e))
