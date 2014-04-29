import boto
import datetime
import json
import config



def getStuff():
	c = boto.connect_cloudwatch(aws_access_key_id=config.access_key,aws_secret_access_key=config.secret_key)

	networkIn = c.list_metrics(metric_name="NetworkIn")[0]

	end = datetime.datetime.now()
	start = end - datetime.timedelta(hours=12)

	derp = []

	for item in networkIn.query(start,end,'Sum','Bytes'):
		item['Timestamp'] = str(item['Timestamp'])
		derp.append(item)

	return json.dumps(derp)