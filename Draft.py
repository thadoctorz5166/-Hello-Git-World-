import requests

# make call to weboste and fetch data


def get_web_data(zip=None, city=None):
  baseUrl = ("http://api.openweathermap.org/data/2.5/weather?767d3b1cbcc650c0b3a6a7d84828fd72")
# api id for the site
apiid = "767d3b1cbcc650c0b3a6a7d84828fd72" 

# zip code and city check
if zip is not None:
# us at the end id for usa country , change it as required
  baseUrl += "&zip="+str(zip)+",us"
else:
  baseUrl += "&q="+str(city)+",us"
# finally append the api id
baseUrl += "&appid="+str(apiid)
# make get requetss using requests module
r = requests.get(baseUrl)
# return the response
return r

# show data in readable format


def display(resp):
  if "resp".status_code == 200:
    data = "resp".json()
print(f"""{data['name']} Weather Forecast:
Type: {data['weather'][0]['description']}
Wind Speed : {data['wind']['speed']} miles/hr
Visibility : {data['visibility']} m
Min. Temp : {data['main']['temp_min']} F
Max Temp : {data['main']['temp_max']} F
""")
else:
print("Request Failed, Error : ", resp.status_code)


def main():
  while True:
    choice = int(
input("How do you want to search ? :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

if choice == 1:
  try:
    zCode = int(input("Enter zip code : "))
# fetch data from website
resp = get_web_data(zCode, None)
display(resp)
except Exception as ex:
print("Error : ", ex)
elif choice == 2:
try:
  cname = input("Enter city name : ")
# mak call to fetch fetch_data
resp = get_web_data(None, cname)
display(resp)
except Exception as ex:
print("Error : ", ex)
elif choice == 3:
break
else:
print("Incorrect Option..\n")


if __name__ == "__main__":
  main()