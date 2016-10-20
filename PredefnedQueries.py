from Queries import *

def initQueries(Key):
    if Key=='http':
        http=[
              QueryStatment('select * from http',1,'http',['uid','ts']),
              QueryStatment('select uid,ts,`user_agent` from http',2,'http',['uid','ts','user agent']),
              QueryStatment('select uid,ts,`request` from http',3,'http',['uid','ts','request']),
              QueryStatment('select uid,ts,`uri` from http',4,'http',['uid','ts','uri']),
              QueryStatment('select uid,ts,`method` from http',5,'http',['uid','ts','method']),
              QueryStatment('select uid,ts,`method` from http',6,'http',['uid','ts','status_code'])
              ]
        return http
    elif Key == 'dns':
        dns= [QueryStatment("SELECT uid,ts,`QUERY` FROM DNS",7,'dns',['uid','ts','dns']),
              QueryStatment("SELECT uid,ts,`ANSWER` FROM DNS_ANSWERS",8,'dns',['uid','ts','answer']),
              QueryStatment("SELECT uid,ts,`RESP_H` FROM IDS",9,'dns',['uid','ts','RESP_H']),
              QueryStatment("SELECT uid,ts,`QTYPE` FROM DNS ",10,'dns',['uid','ts','QTYPE'])
        ]
        return dns
    elif Key=='conn':
        conn=[QueryStatment("SELECT uid,ts,DURATION FROM CONN",11,'conn',['uid','ts','duration']),
          QueryStatment("SELECT uid,ts FROM CONN",12,'conn',['uid','ts']),
          QueryStatment("SELECT uid,ts,ORIG_H , ORIG_P FROM IDS",13,'conn',['uid','ts','orig_h','orig_p']),
          QueryStatment("SELECT uid,ts,RESP_H ,RESP_P FROM IDS",14,'conn',['uid','ts','resp_h','resp_p']),
          QueryStatment("SELECT uid,ts,PROTO FROM CONN",15,'conn',['uid','ts','proto']),
          QueryStatment("SELECT uid,ts,ORIG_BYTES FROM CONN",16,'conn',['uid','ts','orig_bytes']),
          QueryStatment("SELECT uid,ts,RESP_BYTES FROM CONN",17,'conn',['uid','ts','resp_bytes']),
          QueryStatment("SELECT uid,ts,CONN_STATE FROM CONN",18,'conn',['uid','ts','conn_state'])]
        return conn
    elif Key == 'ssl':
        ssl=[QueryStatment("SELECT uid,ts,VERSION FROM SSL",19,'ssl',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,CIPHER FROM SSL",20,'ssl',['uid','ts','CIPHER']),
          QueryStatment("SELECT uid,ts,`SERVER_NAME` FROM SSL",21,'ssl',['uid','ts','SERVER_NAME']),
          QueryStatment("SELECT uid,ts,SUBJECT FROM SSL",22,'ssl',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,ISSUER FROM SSL",23,'ssl',['uid','ts','version']),]
        return ssl
    elif Key == 'ssh':
        ssh= [QueryStatment("SELECT uid,ts,HOST KEY FROM SSH",24,'ssh',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,DIRECTION FROM SSH",24,'ssh',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,CLIENT FROM SSH",24,'ssh',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,SERVER FROM SSH",24,'ssh',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,CIPHER_ALG FROM SSH",24,'ssh',['uid','ts','version']),
          QueryStatment("SELECT uid,ts,VERSION FROM SSH",24,'ssh',['uid','ts','version'])]
        return ssh
    elif Key == 'weird':
        weird= [
        QueryStatment("SELECT uid,ts,`NAME` FROM WEIRD",25,'WEIRD',['uid','ts','NAME']),
        QueryStatment("SELECT uid,ts,`ADDI` FROM WEIRD",26,'WEIRD',['uid','ts','ADDI']),
        QueryStatment("SELECT uid,ts,`NOTICE` FROM WEIRD",27,'WEIRD',['uid','ts','NOTICE']),
        QueryStatment("SELECT uid,ts,`PEER` FROM WEIRD",28,'WEIRD',['uid','ts','PEER'])
            ]
        return weird
    else :
        False



