from influxdb import InfluxDBClient

global influx

def influx(str):
  client=InfluxDBClient('localhost',8086,'admin','admin',database='vivek3')
  for line in iter(str.readline,''):
	line=line.rstrip()
	if(line == ''):
		pass
	elif():
		# print line
		lines=line.split()
		t=lines[0].split('.')
		b=lines[1].split('.')
		json_body=[ 
              {
               "measurement": "bitrate",
               "tags": {
                   "host": " ",
                },
               "fields": {
                    "value": b[0],
		    "timestamp": t
                }
              }
             ]
	        client.write_points(json_body)
  
