import plotly.offline as py
import geoip2.database as reader
from datetime import datetime as time
def map (connection,finder):
    # finder=reader.Reader('GeoLite2-City.mmdb')
    destinations=[]
    query = 'SELECT distinct ORIG_H,RESP_H FROM ids'
    edges=[]
    orphaned_locs=[]
    results = connection.DBquery.exec_(query)
    print (results)
    while connection.DBquery.next():
        loc1_found=False
        try:
            ip1=str(connection.DBquery.value(0))
            l1=finder.city(ip1)
            location1=(l1.location.longitude,l1.location.latitude)
            loc1_found=True
        except:
            loc1_found = False
        ip2=connection.DBquery.value(1)
        try:
            l2 = finder.city(ip2)
            location2 = (l2.location.longitude, l2.location.latitude)
            loc2_found=True
        except:
            loc2_found = False

        if loc1_found and loc2_found:
            edges.append((location1 , location2))
        elif loc1_found:
            orphaned_locs.append(location1)
        elif loc2_found:
            orphaned_locs.append(location2)
    print (edges,orphaned_locs)

    orphaned_longintudes=[]
    orphaned_latitudes = []
    for i in orphaned_locs:
        orphaned_longintudes.append(i[0])
        orphaned_latitudes.append(i[1])
    orphaned_nodes = [dict(
        type='scattergeo',
        locationmode='USA-states',
        lat=orphaned_latitudes,
        lon=orphaned_longintudes,
        hoverinfo='text',
        mode='markers',
        marker=dict(
            size=3,
            color='rgb(0,255, 0)',
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
    edges_longitudes=[]
    edges_latitudes=[]
    for j in edges :
        edges_longitudes.append((j[0][0],j[1][0]))
        edges_latitudes.append((j[0][1], j[1][1]))
    connection_paths = []

    connection_paths.append(
            dict(
                type='scattergeo',
                locationmode='global',
                lon=edges_longitudes,
                lat=edges_latitudes,
                mode='lines',
                line=dict(
                    width=1,
                    color='red',
                ),

            )
        )

    layout = dict(
        title='CONNECTIONS APPROXIMATE LOCATIONS',
        showlegend=False,
        autosize=True,
        geo=dict(
            showocean=True,
            showland=True,
            scope='global',
            projection=dict(
                type='orthographic',
                rotation=dict(
                    lon=-100,
                    lat=40,
                    roll=1
                )
            ),
            oceancolor='rgb(179, 240, 255)',
            landcolor='rgb(138, 138, 92)',
            countrycolor='rgb(204, 204, 204)',
        )
    )

    now = time.now().strftime('%Y-%m-%d %H:%m:%S')
    file = 'BILA-conn-map-%s.html' % now
    fig = dict(data=connection_paths + orphaned_nodes, layout=layout)
    py.plot(fig, filename=file,auto_open=False)
    return file




