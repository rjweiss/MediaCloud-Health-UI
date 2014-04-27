# Media Cloud Sentence Histogram

import mediacloud
import datetime
import json


def publishDateRange(d1, d2):
	return u'+publish_date: [{0} TO {1}]'.format(zi_time(d1), zi_time(d2))
	
# ISO Date Format w/ time zeroed
def zi_time(d):
	return datetime.datetime.combine(d, datetime.time.min).isoformat() + "Z"

mc = mediacloud.api.MediaCloud() # apikey goes in MediaCloud()

# Keywords To Query
mc_query = u'*'

# How May Days Back To Go From Current Date
num_days = 31*6

# Data Array for JSON Output
data = []

# Create Reverse-Sorted (Oldest to Most Recent) Range of Dates To Query Across
base = datetime.datetime.today()
dateList = [ base - datetime.timedelta(days=x) for x in range(0,num_days) ][::-1]

# Iterate Over Dates (minus 1) and Query Media Cloud for Sentence Counts
for x in range(num_days-1):
	mc_filter = publishDateRange(dateList[x], dateList[x+1])
	
	res = mc.sentenceList(mc_query, mc_filter, 0, 0)
	data.append({"Date": dateList[x].isoformat(), "Count": res['response']['numFound']})

# This is what should return from the web service
print(json.dumps(data))
