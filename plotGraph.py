global connection
from plotly.graph_objs import *
import plotly.offline  as py
import networkx as nx

def graph_plot(connection):
    nodes=[]
    edges=[]
    labels=[]
    query1="select ts,uid from dns order by (ts)"
    result1= connection.DBquery.exec_(query1)
    while (connection.DBquery.next()):
        print (type(connection.DBquery.value(0)))
        subquery="select orig_h,resp_h from dns where ts=%s  and uid =%s"%(connection.DBquery.value(0),connection.DBquery.value(1))

    query = 'SELECT ORIG_H,RESP_H FROM ids'
    result = connection.DBquery.exec_(query)
    G = nx.DiGraph()
    if result:
        while connection.DBquery.next():
            # i+=1
            print(connection.DBquery.value(0))
            nodes.append(connection.DBquery.value(0))
            nodes.append(connection.DBquery.value(1))
            labels.append(connection.DBquery.value(0))
            labels.append(connection.DBquery.value(1))
            # if G.has_edge(connection.DBquery.value(0), connection.DBquery.value(1)):
            #     G[connection.DBquery.value(0)][connection.DBquery.value(1)]['weight'] += 1
            # else:
            edges.append((connection.DBquery.value(0), connection.DBquery.value(1)))
                # edge_labels.append(i)
    sever_response = "select resp_h ,orig_h from ids"

    result = connection.DBquery.exec_(sever_response)
    if result:
        while connection.DBquery.next():
            print(connection.DBquery.value(0))
            # graph.add_node(connection.DBquery.value(0))
            # graph.add_node(connection.DBquery.value(1))
            edges.append((connection.DBquery.value(0), connection.DBquery.value(1)))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos1 = nx.spring_layout(G)
    pos2 = nx.spectral_layout(G)
    pos3 = nx.spring_layout(G)
    import plotly.offline  as py

    def make_annotations(pos, text, font_size=14, font_color='rgb(25,25,25)'):
        L = len(pos)
        if len(text) != L:
            raise ValueError('The lists pos and text must have the same len')
        annotations = Annotations()
        for k in pos.keys():
            annotations.append(
                Annotation(
                    text=str(k),
                    x=pos[k][0], y=pos[k][1],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )
        return annotations

    def scatter_nodes(pos, labels=None, color='red', size=20, opacity=1):
        labels=[]
        # pos is the dict of node positions
        # labels is a ldistinctist  of labels of len(pos), to be displayed when hovering the mouse over the nodes
        # color is the color for nodes. When it is set as None the Plotly default color is used
        # size is the size of the dots representing the nodes
        # opacity is a value between [0,1] defining the node color opacity
        L = len(pos)
        trace = Scatter(x=[], y=[], mode='markers', marker=Marker(size=[]))
        print (pos)
        requests_count=0
        join="select distinct dns.ts,dns.uid,ids.orig_h,ids.resp_h from dns inner join ids on dns.uid = ids.uid AND dns.ts=ids.ts" #
        for k in pos.keys():
            print (k)
            trace['x'].append(pos[k][0])
            trace['y'].append(pos[k][1])

            query_requests_count=""" select distinct count(*) from dns
                                  inner join ids on dns.uid = ids.uid AND dns.ts=ids.ts and ids.orig_h='%s'"""%str(k)
            result=connection.DBquery.exec_(query_requests_count)
            label=label2=''
            while connection.DBquery.next():
                requests_count=connection.DBquery.value(0)
                print (str(requests_count)+'wtf')
                label="requested addresses : %s"%str(requests_count)

            query_responses_count = """ select distinct count(*) from dns
                                  inner join ids on dns.uid = ids.uid AND dns.ts=ids.ts and ids.resp_h='%s'"""%str(k)

            result = connection.DBquery.exec_(query_responses_count)
            print(result)

            while connection.DBquery.next():
                requests_count = connection.DBquery.value(0)
                label2 = "responded to %s requests" % str(requests_count)
            labels.append(label+'\n'+label2)
        attrib = dict(name='', text=labels, hoverinfo='text', opacity=opacity)  # a dict of Plotly node attributes
        print (attrib)
        trace = dict(trace, **attrib)  # concatenate the dict trace and attrib
        trace['marker']['size'] = 30
        return trace

    def scatter_edges(G, pos, line_color=None, line_width=1):
        trace = Scatter(x=[], y=[], mode='lines')
        for edge in G.edges():
            trace['x'] += [pos[edge[0]][0], pos[edge[1]][0], None]
            trace['y'] += [pos[edge[0]][1], pos[edge[1]][1], None]
            trace['hoverinfo'] = 'none'
            trace['line']['width'] = line_width
            # if line_color is  None:  # when it is None a default Plotly color is used
            trace['line']['color'] = 'red'
        return trace

    pos = nx.fruchterman_reingold_layout(G)

    # labels = [str(k) for k in range(len(pos))]  # labels are  set as being the nodes indices in the list of nodes
    trace1 = scatter_edges(G, pos)
    trace2 = scatter_nodes(pos)

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                title=''
                )
    layout = Layout(title='DNS connections',  #
                    font=Font(),
                    showlegend=False,
                    autosize=True,
                    # width=width,
                    # height=height,
                    xaxis=XAxis(axis),
                    yaxis=YAxis(axis),
                    margin=Margin(
                        l=40,
                        r=40,
                        b=85,
                        t=100,
                        pad=0,

                    ),
                    plot_bgcolor='#EFECEA',  # set background color
                    )

    data = Data([trace1, trace2])

    fig = Figure(layout=layout,data=data)

    fig['layout'].update(annotations=make_annotations(pos, [str(k) for k in range(len(pos))]))
    # py.sign_in('', '')
    py.plot(fig, filename='12312',auto_open=True)



