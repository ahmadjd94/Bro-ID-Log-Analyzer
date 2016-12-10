import plotly.offline as plotly
import geoip2.database as reader
def map (connection):
    finder=reader.Reader('GeoLite2-City.mmdb')
    destinations=[]
    query = 'SELECT ORIG_H,RESP_H FROM ids'
    result = connection.DBquery.exec_(query)
    while connection.DBquery.next():
        ip1=connection.DBquery.value(0)
        ip2=connection.DBquery.value(1)



