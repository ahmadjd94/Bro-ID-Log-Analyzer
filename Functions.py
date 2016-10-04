from BilaFieldIndecies import validFields  # import indecies dictionary
from Tables import normalized_tables,normalized_fields # import fields of normalized tables
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
