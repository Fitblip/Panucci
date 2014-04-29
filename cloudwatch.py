import boto
import datetime
import json
import config



def getStuff():
	c = boto.connect_cloudwatch(aws_access_key_id=config.access_key,aws_secret_access_key=config.secret_key)

	networkIn = c.list_metrics(metric_name="NetworkIn")[0]

	end = datetime.datetime.now()
	start = end - datetime.timedelta(days=31)

	derp = []

	for item in networkIn.query(start,end,'Sum','Bytes',period=3600):
		item['Timestamp'] = str(item['Timestamp'])
		derp.append(item)
	derp.sort(key=lambda r: r['Timestamp'])
	return json.dumps(derp)