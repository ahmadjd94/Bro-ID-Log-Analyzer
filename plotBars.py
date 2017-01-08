
import plotly.graph_objs as go
import plotly.offline as py
global connection

def plotbars(connection):
    ls=[]
    overall_count=0
    flags=[]
    percentages=[]
    test=[]
    flags_query="select distinct (name) from weird"
    connection.DBquery.exec_(flags_query)
    while connection.DBquery.next():
        flags.append(connection.DBquery.value(0))
        test.append(connection.DBquery.value(1))
    overall_count_query = "select count  (*) from weird "
    connection.DBquery.exec_(overall_count_query)
    while connection.DBquery.next():
        overall_count=(connection.DBquery.value(0))
    print (flags)
    print(type(flags))
    for i in flags:
        qu = "select count  (*) from weird where name='%s'"%str(i)
        print(qu)
        connection.DBquery.exec_(qu)
        while connection.DBquery.next():
            count=(connection.DBquery.value(0))
            ls.append(count)
            percentages.append("%s of file"%str(count/overall_count*100))

    trace0 = go.Bar(
        x=flags,
        y=ls,
        text=percentages,
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title='weird flags',
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='text-hover-bar')