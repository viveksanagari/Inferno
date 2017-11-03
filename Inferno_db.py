from influxdb import InfluxDBClient

global influx

def influx(str):
  client=InfluxDBClient('localhost',8086,'admin','admin',database='vivek3')
  for line in iter(str.readline,''):
	line=line.rstrip()
  print line
