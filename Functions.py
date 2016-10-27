from BilaFieldIndecies import validFields  # import indecies dictionary
from Tables import normalized_tables,normalized_fields,table_created # import fields of normalized tables
from BilaTypes import BilaTypes #import field types
import time
from datetime import datetime #needed for formating

def SQLcreator( table, line):  # this function creates SQL Queries based on table based to it
    normalized_inserts = []

    print(len(validFields[table]), len(line))

    # if len (line) < len(validFields[table]):
    #     print ("invalid line detected")
    #     return
    print(line)
    print(table)
    exist = {}  # stores the values of existing fields that can be extracted from the log file
    # THIS FUNCTION WILL RAISE AN EXCEPTION INCASE OF INVALID TABLE TYPE
    # HANDLED IN THE CALLER FUNCTION
    # use time.time to get the current time in epoch format
    # print('inside creator ', validFields[table])

    try:
        print(validFields[table])
        exist = dict(validFields[table])
    except:
        print('error making list')
    print(exist)
    # missing cast
    keys = list(exist.keys())
    print(type(keys))
    print(keys)
    print(exist.values())
    print('prepare to cast ')
    try:
        print(type(exist))
        value = list(exist.values())
    except:
        print("error getting values of dict")
        raise Exception

    print(value)
    # todo : check if the arrays are sorted already
    for i1 in range(len(value)):  # the following algorithm sorts the exist dictionary , python dictionary are not sorted
        # the algorithm is a modified version of bubble sort
        for i2 in range(len(value) - 1):
            if value[i2] > value[i2 + 1]:
                valuetemp = value[i2]
                keytemp = keys[i2]
                value[i2] = value[i2 + 1]
                keys[i2] = keys[i2 + 1]
                value[i2 + 1] = valuetemp
                keys[i2 + 1] = keytemp
    try:
        keys = keys[value.index(0):]  # slice keys based based on the values array
        value = value[value.index(0):]  # slice values array accoridng to the first 0 seen in the array
        print(value, keys)
    except Exception as exc4:
        print(str(exc4))

    try:
        # print(validFields['conn'])
        if table == "files":
            pass
        else:
            main_insert = "insert into main (uid,ts) values ('%s',%s)" % (line[exist['uid']], line[exist['ts']])
            print(main_insert)
    except Exception as exc5:
        print("WTF")
        print('test in main', str(exc5))
    inserts = []

    ################################ ids-SPECIFIC INSERTS AND STATMENTS######################
    ids_values = ""  # string will stores the values of insert statment for ids table
    ids_insert = "insert into ids("
    ids_field = field = values_string = ""  # variable field stores the field name in table
    #######################################################################################

    normal_table_insert = "insert into %s (" % table  # insert statment
    print(normal_table_insert)

    for i in keys:
        if i in dict(validFields[table]):
            #####################SPECIAL FIELDS OF IDS TABLE#####################################
            if i == "id.orig_h":
                ids_field += "`orig_h`" + ","
            elif i == "id.orig_p":
                ids_field += "`orig_p`" + ","
            elif i == "id.resp_h":
                ids_field += "`resp_h`" + ","
            elif i == "id.resp_p":
                ids_field += "`resp_p`" + ","

            elif i not in normalized_fields:
                field += "`" + str(i) + "`,"

        else:
            pass  # neglecting the invalid fields detected

    field = field[:len(field) - 1]  # this line will remove the colon at the end of fileds string
    # print (field)
    print(len(value))
    print("312341231234214")
    print(line)
    print(keys)
    for key in keys:
        print(key, line[exist[key]])
        # print (validFields['ids'])
        if key in validFields['ids'].keys():
            if line[exist[key]] != '-':
                if BilaTypes[key] == str:
                    ids_values += "\'" + line[exist[key]] + '\','

                else:
                    ids_values += line[exist[key]] + ","
            else:
                ids_values += "" + "null" + ','

        elif key in normalized_fields.keys():
            try:

                if line[exist[key]] in ["(empty)", '-']:
                    normalized_insert = "insert into %s_%s( " % (table, key)
                    if table == 'files':
                        normalized_insert += "`ts`,`%s`) values (%f,'null')" % (
                        normalized_fields[key], float(line[exist["ts"]]))

                    else:
                        normalized_insert = "insert into %s_%s (`uid`,`ts`,`%s`) values (\'%s\',%f,'null')" % (
                            table, key, normalized_fields[key], line[exist["uid"]], float(line[exist["ts"]]))
                    print(normalized_insert)
                    normalized_inserts.append(normalized_insert)
                else:
                    values = line[exist[key]].split(',')
                    if table == 'files':
                        files_normalized_insert = ""
                        normalized_insert = "insert into %s_%s ( `ts`,`%s`) values (%f," % (
                        table, key, normalized_fields[key], float(line[exist["ts"]]))
                        for value in values:
                            files_normalized_insert += normalized_insert + "\'%s\')" % (value)
                            normalized_inserts.append(files_normalized_insert)
                    else:
                        for value in values:
                            normalized_insert = "insert into %s_%s (`uid`,`ts`,`%s`) values (\'%s\',%f,\'%s\')" % (
                                table, key, normalized_fields[key], line[exist["uid"]], float(line[exist["ts"]]), value)
                            normalized_inserts.append(normalized_insert)
            except Exception as exc6:
                print('rcptto error', str(exc6), key)



        elif (line[exist[key]] != '-' or line[exist[key]] != "-") and key not in normalized_tables:
            try:
                if BilaTypes[key] == datetime:  # checking for datetime type
                    #  NOTE converting epoch to datetime is redundent since sqlite drivers are capable of handle epoch time
                    a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(line[exist[key]])))
                    # print (a)
                    values_string += "\'" + str(a) + "\',"  # concatenating the value to the values string

                elif BilaTypes[key] == int:
                    print(line[exist[key]], 'test1')
                    values_string += line[exist[key]] + ","
                elif BilaTypes[key] == float:
                    values_string += line[exist[key]] + ","

                elif BilaTypes[key] == bool:
                    if line[exist[key]] == "F" or line[exist[key]] == "f":
                        values_string += "0,"
                    elif line[exist[key]] == "t" or line[exist[key]] == "T":
                        values_string += "1,"
                    else:
                        values_string += "null,"

                else:
                    values_string += "\'" + str(line[exist[key]]) + "\',"
            except Exception as exc7:
                print("faga33334443", exc7)
        else:
            values_string += "null,"
        print(values_string)
    # print (values_string)
    try:
        ids_values = ids_values[:len(ids_values) - 1]
        print(ids_values)
    except:
        print("no ids values")

    try:
        values_string = values_string[:len(values_string) - 1]  # split the colons
        print(values_string)
    except Exception as exc8:
        print(str(exc8), "error splitting values string ")

    print(type(field))
    normal_table_insert += field + ") values (" + values_string + ")"  # construct the final insert statment
    inserts.append(normal_table_insert)
    try:
        ids_insert = ids_insert + "ts" + ",uid," + ids_field[:len(ids_field) - 1] + ")values(" + line[exist['ts']] + ",\'" + \
                     line[exist['uid']] + "\'," + ids_values + ")"
        inserts.append(ids_insert)
        print(ids_insert)

    except Exception as exc9:
        print(str(exc9), 'exception happend while appending')
    if len(normalized_inserts) > 0:
        inserts.extend(normalized_inserts)

    print(normal_table_insert)
    print('returned tables')
    if table != 'files':
        inserts.insert(0, main_insert)
    print(inserts)
    return inserts


def table_creator(fname,DBquery):  # this function creates tables based on the fname argument
    print('fname passes to function', fname)
    fname = fname.lower()

    if fname == 'ids':
        if table_created['ids'] == False:
            DBquery.exec_("""CREATE TABLE ids (uid text,ts int ,ORIG_H TEXT,
                                ORIG_P INT,RESP_H TEXT,RESP_P INT,FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`),foreign key (`ts`) references  main (`ts`))""")
            table_created['ids'] = True
            print("success creating ids  table ")

    elif fname == "ftp.log":  # DONE # create FTP table //THIS TABLE HAS RELATION WITH IDS TABLE #checled and works correctly
        try:
            if table_created['ids'] == False:
                table_creator('ids')
            DBquery.exec_("""CREATE TABLE FTP(UID TEXT,ts int
            ,USER TEXT,PASSWORD TEXT,COMMAND TEXT,ARG TEXT,
            MIME_TYPE TEXT,FILE_SIZE INT,REPLY_CODE INT,REPLY_MSG TEXT,
            FUID TEXT,FOREIGN KEY (UID)REFERENCES MAIN(UID),FOREIGN KEY (ts)REFERENCES MAIN(ts))""")
            print("step3")
            table_created['FTP'] = True
            return True
        except:
            return False

    elif fname == "dhcp.log":  # create DHCP table //THIS TABLE HAS RELATION WITH IDS TABLE # checked and working
        try:
            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE DHCP(UID TEXT,TS int
            ,MAC TEXT, ASSIGNED_IP TEXT,LEASE_TIME TEXT
            , TRANS_ID INT,FOREIGN KEY(UID) REFERENCES MAIN(UID),FOREIGN KEY(ts) REFERENCES MAIN(ts) )""")
            print("step2")
            table_created['DHCP'] = True
            return True
        except:
            return False

    elif fname == "irc.log":  # DONE  create IRC table //THIS TABLE HAS RELATION WITH IDS TABLE  #check and working
        try:
            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE IRC (UID TEXT,ts int
            , NICK TEXT,USER TEXT,COMMAND TEXT,VALUE TEXT,ADDI TEXT,
            DCC_FILE_NAME TEXT,DCC_FILE_SIZE INT,DCC_MIME_TYPE TEXT,FUID TEXT,FOREIGN KEY(UID) REFERENCES MAIN(UID),
            FOREIGN KEY(ts) REFERENCES MAIN(ts) )""")
            print("step4")
            table_created['IRC'] = True
            return True
        except:
            return False

    elif fname == "weird.log":  # create weird table WORKING FINE
        try:

            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("CREATE TABLE WEIRD(UID TEXT,ts int, NAME TEXT,"
                          "ADDI TEXT,NOTICE BOOL,PEER TEXT,FOREIGN KEY(UID) REFERENCES MAIN(UID),"
                          "FOREIGN KEY(ts) REFERENCES MAIN(ts) )""")
            table_created['WEIRD'] = True
            print("step5")
        except:
            return False

    elif fname == "ssh.log":  # DONE create SSH table CHECKED and working correctly
        try:

            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE SSH( UID TEXT,TS INT,host_key TEXT,STATUS TEXT,
            DIRECTION TEXT,CLIENT TEXT, SERVER TEXT,RESP_SIZE INT,cipher_alg text ,version text,
            FOREIGN KEY(UID) REFERENCES MAIN(UID),FOREIGN KEY(ts) REFERENCES MAIN(ts) )""")
            table_created['SSH'] = True
            print("step6")
            return True
        except:
            return False

    elif fname == "conn.log":  # DONE  create CONN table
        try:
            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE CONN(UID TEXT,TS INT,PROTO TEXT,SERVICE TEXT,DURATION TIME,ORIG_BYTES INT,
            RESP_BYTES INT,CONN_STATE TEXT,LOCAL_ORIG BOOL,MISSED_BYTES COUNT,HISTORY TEXT,ORIG_PKTS INT,ORIG_IP_BYTES INT,
            RESP_PKTS INT,RESP_IP_BYTES INT,TUNNEL_PARENTS BLOB,ORIG_CC TEXT,RESP_CC TEXT,
            FOREIGN KEY (UID)REFERENCES MAIN(UID),FOREIGN KEY (ts)REFERENCES MAIN(ts))""")

            DBquery.exec_("""CREATE TABLE CONN_TUNNEL_PARENTS (UID TEXT , TS INT , PARENT TEXT ,FOREIGN KEY (UID) REFERENCES conn (UID),
                         FOREIGN KEY (TS) REFERENCES conn (TS))""")
            table_created['CONN'] = True

            print("step7")
            return True
        except:
            return False

    elif fname == "http.log":  # todo: needs furhter checking

        try:

            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE  HTTP (
                                    UID TEXT,ts int
                                    ,TRANS_DEPTH INT,METHOD TEXT,HOST TEXT,URI TEXT,REFERRER TEXT,
                                    USER_AGENT TEXT,REQUEST_BODY_LEN INT,
                                    STATUS_CODE INT,STATUS_MSG TEXT,INFO_CODE INT,INFO_MSG TEXT,filename text,USERNAME TEXT,
                                    PASSWORD TEXT,PROXIED TEXT,
                                    FOREIGN KEY  (UID) REFERENCES MAIN (UID),
                                    FOREIGN KEY  (ts) REFERENCES MAIN (ts))""")

            DBquery.exec_(
                "CREATE TABLE HTTP_TAGS (UID TEXT , TS INT , TAG TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),"
                "FOREIGN KEY  (ts) REFERENCES http (ts))")

            DBquery.exec_("""CREATE TABLE HTTP_PROXIED_HEADERS (UID TEXT , TS INT ,
                          HEADER TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                FOREIGN KEY  (ts) REFERENCES http (ts))""")

            DBquery.exec_("""CREATE TABLE HTTP_ORIG_FUIDS (UID TEXT , TS INT
                      , ORIG_FUID TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                FOREIGN KEY  (ts) REFERENCES http (ts))""")

            DBquery.exec_("""CREATE TABLE HTTP_ORIG_MEME_TYPES (UID TEXT , TS INT
                ,ORIG_MEME_TYPES TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                FOREIGN KEY  (ts) REFERENCES http (ts))""")

            DBquery.exec_(
                """CREATE TABLE HTTP_RESP_FUIDS (UID TEXT , TS INT ,
                RESP_FUIDS TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                FOREIGN KEY  (ts) REFERENCES http (ts))""")

            DBquery.exec_("""CREATE TABLE HTTP_RESP_MEME_TYPES (UID TEXT , TS INT
                        , RESP_MEME_TYPES TEXT,FOREIGN KEY (UID) REFERENCES HTTP(UID),
                FOREIGN KEY  (ts) REFERENCES http (ts))""")

            table_created['HTTP'] = True
            table_created['HTTP_RESP_MEME_TYPES'] = True
            table_created['HTTP_RESP_FUIDS'] = True
            table_created['HTTP_ORIG_MEME_TYPES'] = True
            table_created['HTTP_ORIG_FUIDS'] = True
            table_created['HTTP_PROXIED_HEADERS'] = True
            table_created['HTTP_TAGS'] = True
            print("step8")

        except:
            return False
    elif fname == "dns.log":  # DONE # create DNS table    continously crashing
        try:
            # if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
            try:
                if table_created['ids'] == False:
                    table_creator('ids')  # call the table creator function to create the ids table
            except Exception as DNS_exc:
                print('error creating ids of dns ', DNS_exc)

            DBquery.exec_("""CREATE TABLE DNS (
                                    UID TEXT,ts int,PROTO TEXT,TRANS_ID INT,
                                    `QUERY` TEXT,`QCLASS` INT,`QCLASS_NAME` TEXT,`QTYPE` INT,`QTYPE_NAME` TEXT,`RCODE` INT,
                                    `RCODE_NAME` TEXT,`QR` bool,`AA` BOOL,`TC` BOOL,
                                    `RD` BOOL,`RA` BOOL,`Z`INT,`rejected` BOOL,FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`),
                                    FOREIGN KEY (`UID`) REFERENCES MAIN(`UID`))""")

            DBquery.exec_("CREATE TABLE DNS_ANSWERS (UID TEXT , TS INT ,ANSWER TEXT,"
                          "FOREIGN KEY (UID) REFERENCES DNS(UID),"
                          "FOREIGN KEY (ts) REFERENCES DNS(ts))")

            DBquery.exec_("CREATE TABLE DNS_TTLS (UID TEXT , TS INT ,TTL INT,"
                          "FOREIGN KEY (UID) REFERENCES DNS(UID),"
                          "FOREIGN KEY (ts) REFERENCES DNS(ts))")

            table_created['DNS_ANSWERS'] = True
            table_created['DNS_TTLS'] = True

            print("step9")
        except:
            return False

    elif fname == "signature.log":  # create SIGNATURES table  needs testing
        try:
            DBquery.exec_("""CREATE TABLE SIGNATURE(TS INT ,SRC_ADDR TEXT ,
                        SRC_PORT INT ,DST_ADR TEXT ,DST_PORT INT ,NOTE TEXT ,SIG_ID TEXT,
                        EVENT_MSG TEXT ,SUB_MSG TEXT ,SIG_COUNT INT ,HOST_COUNT INT )""")
            table_created['SIGNATURE'] = True

            print("step10")
            return True
        except:
            return False
    elif fname == "ssl.log":  # DONE # create SSL table and it's realted tables
        try:
            # if list(dropped)[tables.index("IDS")] == 0:  # indicates if the IDS exists or not
            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE SSL(UID TEXT,ts int,VERSION TEXT ,CIPHER TEXT ,
            SERVER_NAME TEXT ,SESSION_ID TEXT ,SUBJECT TEXT ,
            ISSUER_SUBJECT TEXT ,NOT_VALID_BEFORE TIME ,
            LAST_ALERT TEXT ,CLIENT_SUBJECT TEXT ,CLNT_ISSUER_SUBJECT TEXT ,CERT_HASH TEXT ,
            FOREIGN KEY (UID)REFERENCES MAIN(UID))""")
            table_created['SSL'] = True

            DBquery.exec_("CREATE TABLE SSL_VALIDATION_STATUS (UID TEXT , TS INT,"
                          "VALIDATION_STATUS TEXT,FOREIGN KEY (UID,TS) REFERENCES SSL(UID,TS))")
            table_created['SSL_VALIDATION_STATUS'] = True

            print("step11")
            return True
        except:
            return False

    elif fname == "files.log":  # DONE # create files table and it's related tables #needs testing
        try:
            DBquery.exec_(
                """CREATE TABLE FILES (TS INT , FUID TEXT,TX_HOSTS TEXT,RX_HOSTS TEXT,SOURCE TEXT ,DEPTH INT,
                ANALYZERS TEXT,MIME_TYPE TEXT,
                FILENAME TEXT,DURATION TIME,LOCAL_ORIG BOOL,IS_ORIG BOOL,SEEN_BYTES INT,TOTAL_BYTES INT ,
                MISSING_BYTES INT,OVERFLOW_BYTES INT,TIMEDOUT INT,PARENT_FUID STRING,
                MD5 TEXT,SHA1 TEXT,SHA256 TEXT,EXTRACTED BOOL)""")
            table_created['FILES'] = True

            DBquery.exec_("CREATE TABLE FILES_TX_HOSTS(UID TEXT,TS INT,TX_HOST"
                          ",FOREIGN KEY (UID) REFERENCES FILE(UID)"
                          ",FOREIGN KEY (TS) REFERENCES FILE(TS))")
            table_created['FILES_TX_HOSTS'] = True

            DBquery.exec_("CREATE TABLE FILES_RX_HOSTS(UID TEXT,TS INT,RX_HOST TEXT"
                          ",FOREIGN KEY (UID) REFERENCES FILE(UID)"
                          ",FOREIGN KEY (TS) REFERENCES FILE(TS))")
            table_created['FILES_RX_HOSTS'] = True

            DBquery.exec_("CREATE TABLE FILES_CONN_UIDS(UID TEXT,TS INT,CONN_UID TEXT"
                          ",FOREIGN KEY (UID) REFERENCES FILE(UID)"
                          ",FOREIGN KEY (TS) REFERENCES FILE(TS))")
            table_created['FILES_CONN_UIDS'] = True

            DBquery.exec_("CREATE TABLE FILES_ANALYZERS (UID TEXT , TS INT ,ANALYZER TEXT,"
                          "FOREIGN KEY (UID) REFERENCES FILE(UID)"
                          ",FOREIGN KEY (TS) REFERENCES FILE(TS))")
            table_created['FILES_ANALYZERS'] = True

        except:
            return False

    elif fname == "smtp.log":  # DONE # create SMTP table and it's related tables
        try:

            if table_created['ids'] == False:
                table_creator('ids')  # call the table creator function to create the ids table

            DBquery.exec_("""CREATE TABLE SMTP (UID TEXT ,TS INT,
            TRANS_DEPTH INT ,HELO TEXT,MAILFROM STRING,RCPTTO TEXT
            ,`DATE` TEXT ,`FROM` TEXT ,`TO` TEXT,`REPLY_TO` TEXT,`MSG_ID` TEXT ,`IN_REPLY_TO` TEXT ,`SUBJECT` TEXT
            ,`X_ORIGINATING_IP` TEXT,`FIRST_RECEIVED` TEXT ,
            `SECOND_RECEIVED` TEXT ,`LAST_REPLY` TEXT ,`USER_AGENT` TEXT ,
            `TLS` BOOL,`IS_WEBMAIL` BOOL , FOREIGN KEY (UID) REFERENCES  MAIN(UID),
            FOREIGN KEY (ts) REFERENCES main(ts))""")
            table_created['SMTP'] = True

            DBquery.exec_("""CREATE TABLE  SMTP_RCPTTO (UID TEXT , TS INT ,receipent TEXT,
            FOREIGN KEY (UID) REFERENCES SMTP(UID),FOREIGN KEY (ts) REFERENCES SMTP(ts))""")
            table_created['SMTP_RCPTTO'] = True

            DBquery.exec_("CREATE TABLE  SMTP_TO (`UID` TEXT , `TS` INT ,`TO` TEXT,"
                          "FOREIGN KEY (UID) REFERENCES SMTP(UID),FOREIGN KEY (ts) REFERENCES SMTP(ts))")
            table_created['SMTP_TO'] = True

            DBquery.exec_("CREATE TABLE SMTP_PATH (`UID` TEXT ,`TS` INT , `PATH` TEXT,"
                          "FOREIGN KEY (UID) REFERENCES SMTP(UID),FOREIGN KEY (ts) REFERENCES SMTP(ts))")
            table_created['SMTP_PATHS'] = True

            DBquery.exec_("CREATE TABLE SMTP_FUIDS(`UID` TEXT ,`TS` INT,`FUID` TEXT ,"
                          "FOREIGN KEY (UID) REFERENCES SMTP(UID),FOREIGN KEY (ts) REFERENCES SMTP(ts))")
            table_created['SMTP_FUIDS'] = True

            # `RCPTO` AND `TO` COLUMNS ARE ASSUMED TO BE SETS
            return True
        except:
            return False
