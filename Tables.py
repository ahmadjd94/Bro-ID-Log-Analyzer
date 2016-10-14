# this list declares main tables in the database
tables = ['dhcp',
          "smtp",
          "irc",
          "weird",
          "ssh",
          "conn",
          'ftp',
          "http",
          "dns",
          "signature",
          "ssl",
          "ids",
          "files",
          'ssh',
          'main']
table_created ={'dhcp':False,
          "smtp":False,
          "irc":False,
          "weird":False,
          "ssh":False,
          "conn":False,
          'ftp':False,
          "http":False,
          "dns":False,
          "signature":False,
          "ssl":False,
          "ids":False,
          "files":False,
          'ssh':False,
          'main':False}
# the following dictionary denotes normalized FIELDS
normalized_fields = {'fuids': 'fuid',
                     'path': 'path',
                     'to': 'to',
                     'rcptto': 'receipent',
                     'analyzers': 'analyzer',
                     'conn_uids': 'conn_uid',
                     'rx_hosts': 'rx_host',
                     'tx_hosts': 'tx_host',
                     "tunnel_parents": 'parent',
                      "ttls": 'ttl',
                     'answers': 'answer',
                     'resp_meme_types': 'resp_meme_type',
                     'resp_fuids': 'resp_fuid',
                     'orig_meme_types': 'orig_meme_types',
                     'orig_fuids': 'orig_fuid',
                     'proxied_headers': 'header',
                     'tags': 'tag',
                     'validation_status': 'validation_status'}

#the following list shows the names of normalized tables
normalized_tables = ['http_proxied_headers',
                     'http_resp_meme_types',
                     'http_tags',
                     'http_orig_meme_types',
                     'http_orig_fuids',
                     'http_resp_fuids',
                     'files_tx_hosts',
                     'files_conn_uids',
                     'files_analyzers',
                     'files_rx_hosts',
                     'ftp_data_channel',
                     'conn_tunnel_parents',
                     'dns_ttls',
                     'dns_answers',
                     'smtp_analyzers',
                     'smtp_rcptto',
                     'smtp_to',
                     'smtp_fuids',
                     'smtp_path',
                     'ssl_validation_status']

valid = ['conn.log', 'dhcp.log', 'dns.log', 'ftp.log', 'http.log', 'irc.log',
         'smtp.log', 'ssl.log', 'files.log', 'signatures.log', 'weird.log',
         'ssh.log']  # this list stores the valid log files bila currently supports

#the fol;owing line declares the files bila doesnt currently support
UnsupportedFiles = ['x509.log', 'packet_filter.log', 'app_stats.log', 'capture_loss.log', 'dnp3.log', 'intel.log',
                    'known_certs.log', 'radius.log', 'modbus.log', 'notice.log', 'reporter.log',
                    'notice.log', 'software.log', 'snmp.log', 'socks.log',
                    'syslog.log', 'traceroute.log',
                    'known_hosts.log']

validQueries ={
        'http':['select * from http',
            'SELECT USER_AGENT FROM HTTP',
            'SELECT REQUEST FROM HTTP',
            'SELECT URI FROM HTTP',
            'SELECT METHOD FROM HTTP',
            'SELECT STATUS_CODE ,STATUS_MSG FROM HTTP'] ,

        'dns':["SELECT QUERY FROM DNS",
            "SELECT ANSWER FROM DNS_ANSWERS",
            "SELECT RESP_H FROM IDS",
            "SELECT QTYPE FROM DNS "],

        'conn':[
            "SELECT DURATION FROM CONN",
            "SELECT UID FROM CONN",
            "SELECT ORIG_H , ORIG_P FROM IDS",
            "SELECT RESP_H ,RESP_P FROM IDS",
            "SELECT PROTO FROM CONN",
            "SELECT ORIG_BYTES FROM CONN",
            "SELECT RESP_BYTES FROM CONN",
            "SELECT CONN_STATE FROM CONN"],

        'ssl':[
            "SELECT VERSION FROM SSL",
            "SELECT CIPHER FROM SSL",
            "SELECT SERVER_NAME FROM SSL",
            "SELECT SUBJECT FROM SSL",
            "SELECT ISSUER FROM SSL"],

        'ssh':["SELECT HOST KEY FROM SSH",
              "SELECT DIRECTION FROM SSH",
              "SELECT CLIENT FROM SSH",
              "SELECT SERVER FROM SSH",
              "SELECT CIPHER_ALG FROM SSH",
              "SELECT VERSION FROM SSH"],
        'weird':[
              "SELECT NAME FROM WEIRD",
              "SELECT ADDI FROM WEIRD",
              "SELECT NOTICE FROM WEIRD",
              "SELECT PEER FROM WEIRD"],
}


