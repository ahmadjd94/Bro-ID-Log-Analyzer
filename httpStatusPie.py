import plotly.offline as py
global connection
import plotly.graph_objs as go
def plot_http_status_pir(connection):
    count_http_requests_count="select count (*) from http"
    connection.DBquery.exec_(count_http_requests_count)
    while(connection.DBquery.next()):
        overall_count=int(connection.DBquery.value(0))
    labels=[]
    values=[]
    statuses_query='select distinct status_code from http'
    connection.DBquery.exec_(statuses_query)
    while (connection.DBquery.next()):
        labels.append(str(connection.DBquery.value(0)))
    for i in labels :
        count_query="select count(*) from http where status_code=%d"%int(i)
        connection.DBquery.exec_(count_query)
        while (connection.DBquery.next()):
            values.append(str(connection.DBquery.value(0)))
    fig = {
      "data": [
        {
          "values": values,
          "labels": labels,
          "domain": {"x": [0, .48]},
          "name": "status codes of HTTP log",
          "hoverinfo":"label+percent+name",
          "hole": .4,
          "type": "pie"
        }],
      "layout": {
            "title":"status codes of HTTP log",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "statuses",
                    "x": 0.20,
                    "y": 0.5
                }
            ]
        }
    }
    py.plot(fig)