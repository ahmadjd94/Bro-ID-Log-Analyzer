import plotly.graph_objs as go
import plotly.offline as py
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

    trace = go.Pie(labels=labels, values=values)

    py.plot([trace])



