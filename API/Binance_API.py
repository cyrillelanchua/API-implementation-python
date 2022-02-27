import urllib.request, urllib.error, urllib.parse
import json
import datetime
#The APi returns JSON data
serviceUrl = "https://api2.binance.com/api/v3/ticker/24hr"
handle = urllib.request.urlopen(serviceUrl)
data = handle.read().decode()    

print("retrieving ",serviceUrl)
print("Retrieved",len(data), "characters")


try:
    js = json.loads(data)
except:
    js = None

hash = dict()
position = 0
for crypto in js:
    hash[crypto["symbol"]] = position
    position +=1

user_input = input("Enter a crypto symbol (ex. ETHBTC) : ")
position = hash[user_input]

print(user_input, "information")
print("Price Change:",js[position]["priceChange"])
print("High Price:",js[position]["highPrice"])
open_time = js[position]["openTime"]
close_time = js[position]["closeTime"]

#converts the millisecond time format into a date time format
print("Open Time:",datetime.datetime.fromtimestamp(open_time / 1000.0, tz=datetime.timezone.utc))
print("Close Time:",datetime.datetime.fromtimestamp(close_time / 1000.0, tz=datetime.timezone.utc))
