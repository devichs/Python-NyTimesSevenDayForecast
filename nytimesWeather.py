import requests
import sys,os,pickle

url = "https://www.nytimes.com/svc/weather/v2/current-and-seven-day-forecast/LPPT.json"

file_name = "result_set.pickled"

if os.path.isfile(file_name):
	result_set = pickle.load(open(file_name,"rb"))
else:
	r = requests.get(url)
	print("Status: {0}".format(r.status_code))
	result_set = r.json()["results"]["seven_day_forecast"]
	pickle.dump(result_set,open(file_name,"wb"))
	
#print out result_set 
for i in result_set:
	print("For {0} in {1}, look for {2} with a high of {3} and a low of {4}.".format(i["day"],i["city"],i["phrase"],i["high"],i["low"]))
	

	