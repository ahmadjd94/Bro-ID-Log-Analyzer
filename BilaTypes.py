BilaTypes = {  # the foloowing dictionary denotes every field in log files with their data types

        # the following lines denote the types that require a set
        #################sets##############
        "tags": str,"proxied": str , "analyzers": str,
        "orig_fuid": str,"resp_meme_ty": str,"orig_meme_type": str,
        "conn_uids": str,"data_channel":str, "rcptto": str,
        "rx_hosts": str,"path": str, "tx_hosts": str,"validation_status": str,
         "name": str,"tunnel_parents": str, "TTLs": -1, "answers": str, "fuids": str,
        #################end of sets##############

        "uid": str, "ts":float, "id": str, "trans_depth": int, "method": str, "host": str, "uri": str,"trans_id":int,
        "referrer": str, "user_agent": str, "request_body_len": int, "status_code": int, "status_msg": str, "info_code": int,
         "info_msg": str, "username": str, "password": str, "command": str, "arg": str
        , "mime_type": str, "file_size": int, "reply_code": int, "reply_msg": str
        , "fuid": str, "source": str, "depth": int
        , "filename": str, "duration": str, "local_orig": bool, "is_orig": bool, "seen_bytes": int,
             "total_bytes": int,'date':str
        , "missing_bytes": int, "overflow_bytes": int, "timedout": bool, "parent_fuid": str
        , "md5": str, "sha1": str, "sha256": str, "extracted": str
        , "nick": str, "user": str, "value": str, 'addi': str
        , "dcc_file_name": str, "dcc_file_size": int, "dcc_mime_type": str
        , 'trans_depth': int, "helo": str, "mailfrom": str
        , "from": str, "to": str, "reply_to": str, "msg_id": str, "in_reply_to": str, "subject": str
        , "x_originating_ip": str, "first_received": str
        , "second_received": str, "last_reply": str
        , "tls": bool, "is_webmail": bool
        , "status": str, "direction": str, "client": str, "server": str, "resp_size": int
        , "id.orig_h": str, "id.orig_p": int, "id.resp_h": str, "id.resp_p": int, "version": str, "cipher": str,
        "server_name": str, "session_id": str, "issuer_subject": str, "not_valid_before": str,
        "last_alert": str, "client_subject": str, "clnt_issuer_subject": str, "cert_hash": str
        , "notice": bool, "peer": str
        , "src_addr": str, "src_port": int, "dst_adr": str, "dst_port": int, "note": str, "sig_id": str
        , "event_msg": str, "sub_msg": str, "sig_count": int, "host_count": int
        , "id_resp_h": str, "id_resp_p": int, "proto": str, "service": str
        , "orig_bytes": int, "resp_bytes": int, "conn_state": str, "missed_bytes": int, "history": str, "orig_pkts": int
        , "orig_ip_bytes": int, "resp_pkts": int, "resp_ip_bytes": int, "orig_cc": str,
             "resp_cc": str
        , "mac": str, "assigned_ip": str, "lease_time ": str
        , "query": str, "qclass": int, "qclass_name": str, "qtype": int, "qtype_name": str, "rcode": int,
             "rcode_name": str
        , "QR": bool, "AA": bool, "TC": bool, "RD": bool, "RA": bool, "Z": int,
             "rejected": bool
             }  # end of types dictionary declaration