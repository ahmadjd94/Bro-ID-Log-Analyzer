global connection
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime as time
def ssl_subjects_pie(connection):
    certified_conns = []
    labels=[]
    temp_array=[]
    values=[]
    connection.DBquery.exec_("select distinct (subject) from ssl ")
    while connection.DBquery.next():
        certified_conns.append(connection.DBquery.value(0))

    for i in certified_conns:
        connection.DBquery.exec_("select count (*) from ssl WHERE subject='%s'"%i)

        while connection.DBquery.next():
            values.append(connection.DBquery.value(0))

    for full_details in certified_conns:
        temp_array=full_details.split(',')
        for i in temp_array:
            if i[:2]=='CN':
                print (i)
                labels.append(i)
    now = time.now().strftime('%Y-%m-%d %H:%m:%S')
    file = 'BILA-SSL-pie-%s.html' % now
    layout=dict(width=600,
        height=400)
    trace = go.Pie(labels=labels, values=values)

    py.plot([trace],filename=file,auto_open=False)
    return file