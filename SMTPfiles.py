import plotly.graph_objs as go
import plotly.offline as py
from datetime import datetime as time
global connection
def smtp_files(connection):
    smtp_files_query='select count(smtp.fuid) from smtp_fuids as smtp inner join files on smtp.fuid=files.fuid'
    connection.DBquery.exec_(smtp_files_query)
    mailed_files=0
    while connection.DBquery.next():
        mailed_files=int(connection.DBquery.value(0))

    files_query = 'select count(*) from files'
    connection.DBquery.exec_(files_query)
    all_files = 0
    while connection.DBquery.next():
        all_files = int(connection.DBquery.value(0))

    labels = ['smtp', 'other']
    values = [mailed_files, all_files]

    fig = {
        "data": [
            {
                "values": values,
                "labels": labels,
                "domain": {"x": [0, .48]},
                "name": "status codes of HTTP log",
                "hoverinfo": "label+percent+name",
                "hole": .1,
                "type": "pie"
            }],
        "layout": {
            "autosize": True,
            "title": "ratio of files origin according to smtp",
            "annotations": [
                {
                    "font": {
                        "size": 14
                    },
                    "showarrow": False,
                    "text": "ratio",
                    "x": 0.20,
                    "y": 0.5
                }
            ]
        }
    }



    now = time.now().strftime('%Y-%m-%d %H:%m:%S')
    file = 'BILA-smtp-pie-%s.html' % now






    py.plot(fig,filename=file,auto_open=False)
    return file




