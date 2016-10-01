validFields = {  #this line stores the indecies of the fields at each line for every log file type

        "http": {'uid': -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1,
                 "id.resp_h": -1, "id.resp_p": -1, "trans_depth": -1,
                 "method": -1, "host": -1, "uri": -1, "referrer": -1,
                 "user_agent": -1, "request_body_len": -1, "status_code": -1,
                 "status_msg": -1, "info_code": -1,"info_msg": -1,
                 "filename":-1,"tags": -1, "username": -1,
                 "password": -1, "proxied": -1,
                 "orig_fuids": -1, "orig_meme_type": -1,
                 "orig_fuid": -1,"resp_meme_ty": -1},

        'ftp': {"uid": -1, "ts": -1, "id.orig_h": -1, "id.orig_p": .1, "id.resp_h": -1, "id.resp_p": -1,  "user": -1, "password": -1, "command": -1, "arg": -1,
                "mime_type": -1, "file_size": -1, "reply_code": -1, "reply_msg": -1,
                "data_channel": -1, "fuid": -1},

        "files": {"ts": -1, "fuid": -1, "tx_hosts": -1, "rx_hosts": -1, "conn_uids": -1, "source": -1, "depth": -1,
                  "analyzers": -1, "mime_type": -1,
                  "filename": -1, "duration": -1, "local_orig": -1, "is_orig": -1, "seen_bytes": -1, "total_bytes": -1,
                  "missing_bytes": -1, "overflow_bytes": -1, "timedout": -1, "parent_fuid": -1,
                  "md5": -1, "sha1": -1, "sha256": -1, "extracted": -1},  # check this again

        'irc': {"uid": -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,  "nick": -1, "user": -1, "command": -1, "value": -1, "addi": -1,
                "dcc_file_name": -1, "dcc_file_size": -1, "dcc_mime_type": -1, "fuid": 1},

        'smtp': {'ts': -1, 'uid': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, 'trans_depth': -1, "helo": -1, "mailfrom": -1, "rcptto": -1
            , "date": -1, "from": -1, "to": -1, "reply_to": -1, "msg_id": -1, "in_reply_to": -1, "subject": -1
            , "x_originating_ip": -1, "first_received": -1
            , "second_received": -1, "last_reply": -1, "path": -1, "user_agent": -1
            , "tls": -1, "fuids": -1, "is_webmail": -1},

        'ssh': {"uid": -1,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,"status": -1, "direction": -1, "client": -1, "server": -1, "resp_size": -1,'ts':-1},

        'ssl': {"uid": -1,'ts':-1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "version": -1,
                "cipher": -1,
                "server_name": -1, "session_id": -1, "subject": -1,
                "issuer_subject": -1, "not_valid_before": -1,
                "last_alert": -1, "client_subject": -1, "clnt_issuer_subject": -1, "cert_hash": -1,
                "validation_status": -1},

        'weird': {"uid": -1,'ts':-1 ,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1 , "name": -1, "addi": -1, "notice": -1, "peer": -1},

        'signatures': {"ts": -1, 'src_addr': -1,"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1,
                       'src_port': -1, 'dst_adr': -1, 'dst_port': -1, 'note': -1, 'sig_id': -1,
                       'event_msg': -1, 'sub_msg': -1, 'sig_count': -1, 'host_count': -1},
                    # the following tables have the subset of conn table
                    #1 dhcp ,2 dns,3 http,4 irc,5 ftp,6 smtp,7 ssl,8 ssh,9 weird
        'ids':{"id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1},

        'conn': {'ts':-1,"uid": -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "proto": -1,
                  "service": -1,
                  "duration": -1, "orig_bytes": -1,
                  "resp_bytes": -1, "conn_state": -1, "local_orig": -1, "missed_bytes": -1, "history": -1,
                  "orig_pkts": -1,
                  "orig_ip_bytes": -1, "resp_pkts": -1, "resp_ip_bytes": -1, "tunnel_parents": -1, "orig_cc": -1,
                  "resp_cc": -1},

        'dhcp': {"uid": -1,'ts':-1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "mac": -1, "assigned_ip": -1, "lease_time ": -1, "trans_id": -1},

        'dns': {"uid": -1, 'ts': -1, "id.orig_h": -1, "id.orig_p": -1, "id.resp_h": -1, "id.resp_p": -1, "proto": -1, "trans_id": -1,
                "query": -1, "qclass": -1, "qclass_name": -1, "qtype": -1, "qtype_name": -1, "rcode": -1,
                "rcode_name": -1, "qr": -1,
                "aa": -1, "tc": -1, "rd": -1, "ra": -1, "z": -1, "answers": -1, "ttls": -1, "rejected": -1}
        # check tables strucutre !!! normalize conn_ID table
    }