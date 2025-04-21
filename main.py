from polygon import RESTClient

client = RESTClient("Fk_L8BpDagq1F62ed5WObk3uhxWSJbMA")

tickers = []
for t in client.list_tickers(
	market="stocks",
	active="true",
	order="asc",
	limit="100",
	sort="ticker",
	):
    tickers.append(t)

print(tickers)