#This sample code assumes that both Influxdb and Influxdb Python Module are installed and Influxdb service is started

from influxdb import InfluxDBClient

client=InfluxDBClient('localhost','8086','admin','admin',database='dragon')
client.create_database('dragon')
data = [
{
  "measurement" : "sample",
  "tags" : {
        "server" : "Inferno",
        "author" : "viveksanagari"   
  },
  "fields" : {
         "value" : 1.0,
  }
}
]
         
client.write_points(data)
out=client.query('select value from sample;')
print ("out: {0}".format(out))
