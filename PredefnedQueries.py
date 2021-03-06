from Queries import *

def initQueries(Key):
    if Key=='http':
        http=[
              # QueryStatment('select * from http',1,'http',['uid','ts']),
              QueryStatment("select uid,DateTime(ts,'unixepoch'),`user_agent` from http",2,'http',['uid','ts','user agent']),
              QueryStatment("select uid,DateTime(ts,'unixepoch'),`request_body_len` from http",3,'http',['uid','ts','request length']),
              QueryStatment("select uid,DateTime(ts,'unixepoch'),`uri` from http",4,'http',['uid','ts','uri']),
              QueryStatment("select uid,DateTime(ts,'unixepoch'),`method` from http",5,'http',['uid','ts','method']),
              QueryStatment("select uid,DateTime(ts,'unixepoch'),`status_code` from http",6,'http',['uid','ts','status_code'])
              ]
        return http
    elif Key == 'dns':
        dns= [QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`QUERY` FROM DNS",7,'dns',['uid','ts','dns']),
              QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`ANSWER` FROM DNS_ANSWERS",8,'dns',['uid','ts','answer']),
              QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`RESP_H` FROM IDS",9,'dns',['uid','ts','RESP_H']),
              QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`QTYPE` FROM DNS ",10,'dns',['uid','ts','QTYPE'])
        ]
        return dns
    elif Key=='conn':
        conn=[QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),DURATION FROM CONN",11,'conn',['uid','ts','duration']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch') FROM CONN",12,'conn',['uid','ts']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),ORIG_H , ORIG_P FROM IDS",13,'conn',['uid','ts','orig_h','orig_p']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),RESP_H ,RESP_P FROM IDS",14,'conn',['uid','ts','resp_h','resp_p']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),PROTO FROM CONN",15,'conn',['uid','ts','proto']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),ORIG_BYTES FROM CONN",16,'conn',['uid','ts','orig_bytes']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),RESP_BYTES FROM CONN",17,'conn',['uid','ts','resp_bytes']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),CONN_STATE FROM CONN",18,'conn',['uid','ts','conn_state']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),ORIG_H,RESP_H FROM ids", 19, 'conn', ['uid', 'ts', 'origin host','respondent host'])]
        return conn
    elif Key == 'ssl':
        ssl=[QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),VERSION FROM SSL",19,'ssl',['uid','ts','version']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),CIPHER FROM SSL",20,'ssl',['uid','ts','CIPHER']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`SERVER_NAME` FROM SSL",21,'ssl',['uid','ts','SERVER_NAME']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`SUBJECT` FROM SSL",22,'ssl',['uid','ts','SUBJECT']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`ISSUER_SUBJECT` FROM SSL",23,'ssl',['uid','ts','ISSUER_SUBJECT']),]
        return ssl
    elif Key == 'ssh':
        ssh=  [QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`host_key` FROM SSH",24,'ssh',['uid','ts','host key']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),DIRECTION FROM SSH",24,'ssh',['uid','ts','direction']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),CLIENT FROM SSH",24,'ssh',['uid','ts','client']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),SERVER FROM SSH",24,'ssh',['uid','ts','server']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),CIPHER_ALG FROM SSH",24,'ssh',['uid','ts','cipher']),
          QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),VERSION FROM SSH",24,'ssh',['uid','ts','version'])]
        return ssh
    elif Key == 'weird':
        weird= [
        QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`NAME` FROM WEIRD",25,'weird',['uid','ts','NAME']),
        QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`ADDI` FROM WEIRD",26,'weird',['uid','ts','ADDI']),
        QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`NOTICE` FROM WEIRD",27,'weird',['uid','ts','NOTICE']),
        QueryStatment("SELECT uid,DateTime(ts,'unixepoch'),`PEER` FROM WEIRD",28,'weird',['uid','ts','PEER'])
            ]
        return weird
    else :
        False



