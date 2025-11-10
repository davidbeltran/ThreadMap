# from polygon import RESTClient
# import time
# import pprint
# import re

# client = RESTClient("Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA")
# vowels = r'^[aeiouAEIOU]\w*'

# tickers = []
# matches = [s for s in client.list_tickers(market="stocks",active="true",order="asc",limit="100",sort="ticker",) if re.match(vowels, s.ticker)]
# print(matches)
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

# pprint.pprint(tickers[8].ticker)



# try:
#     response = client.list_tickers(limit=1)  # Minimal request
#     print("API connection successful:", response)
# except Exception as e:
#     print("API connection error:", str(e))


#####################################################################################################################################################################


from polygon import RESTClient
import time
import re

# Load API key securely (consider environment variables instead of hardcoding)
API_KEY = "Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA"
client = RESTClient(API_KEY)

# Regex pattern for tickers starting with a vowel
vowel_pattern = re.compile(r'^[AEIOUaeiou][A-Za-z]*$')

# Pagination setup
cursor = None
matches = []
RATE_LIMIT_DELAY = 1  # Adjust based on your API plan

while True:
    response = client.list_tickers(
        market="stocks", active="true", order="asc", limit="100", sort="ticker", cursor=cursor
    )
    
    # Filter tickers that start with a vowel
    filtered_tickers = [ticker for ticker in response if vowel_pattern.match(ticker.ticker)]
    matches.extend(filtered_tickers)

    # Pagination handling
    cursor = response.next_url  # Get the next cursor
    if not cursor:
        break

    # Introduce a delay to respect rate limits
    time.sleep(RATE_LIMIT_DELAY)

# Display results
print(f"Total tickers found: {len(matches)}")
for ticker in matches:
    print(ticker.ticker)
