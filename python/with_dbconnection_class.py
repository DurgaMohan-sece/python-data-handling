import pymysql.cursors
import json
from dbconnection import DbConnection

with DbConnection(host='localhost',
                  user='root',
                  password='dbpassword',
                  db='test') as connection:

    data = json.load(open('sample.json'))
    with connection.cursor() as cursor:
        # Create a new record
        sql = "CREATE TABLE IF NOT EXISTS data (" \
              "ip_proto INTEGER, " \
              "remote_color VARCHAR(20), " \
              "device_model VARCHAR(20), " \
              "destination VARCHAR(20), " \
              "egress_intf VARCHAR(20), " \
              "local_color VARCHAR(20), " \
              "src_ip VARCHAR(20), " \
              "dscp INTEGER, " \
              "statcycletime BIGINT, " \
              "total_bytes INTEGER, " \
              "local_system_ip VARCHAR(20), " \
              "tenant VARCHAR(20), " \
              "dest_port INTEGER, " \
              "entry_time BIGINT, " \
              "flow_active VARCHAR(20), " \
              "total_pkts INTEGER, " \
              "tcpopt VARCHAR(20), " \
              "vmanage_system_ip VARCHAR(20), " \
              "src_port INTEGER, " \
              "start_time BIGINT, " \
              "ingress_intf VARCHAR(20), " \
              "remote_system_ip VARCHAR(20), " \
              "vdevice_name VARCHAR(20), " \
              "dest_ip VARCHAR(20), " \
              "proto VARCHAR(20), " \
              "vip_idx INTEGER, " \
              "tunnel_color VARCHAR(20), " \
              "host_name VARCHAR(20), " \
              "vpn_id INTEGER, " \
              "id VARCHAR(225)" \
              ")"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    for item in data["data"]:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO data VALUES (" \
                  "%(ip_proto)s, " \
                  "%(remote_color)s, " \
                  "%(device_model)s, " \
                  "%(destination)s, " \
                  "%(egress_intf)s, " \
                  "%(local_color)s, " \
                  "%(src_ip)s, " \
                  "%(dscp)s, " \
                  "%(statcycletime)s, " \
                  "%(total_bytes)s, " \
                  "%(local_system_ip)s, " \
                  "%(tenant)s, " \
                  "%(dest_port)s, " \
                  "%(entry_time)s, " \
                  "%(flow_active)s, " \
                  "%(total_pkts)s, " \
                  "%(tcpopt)s, " \
                  "%(vmanage_system_ip)s, " \
                  "%(src_port)s, " \
                  "%(start_time)s, " \
                  "%(ingress_intf)s, " \
                  "%(remote_system_ip)s, " \
                  "%(vdevice_name)s, " \
                  "%(dest_ip)s, " \
                  "%(proto)s, " \
                  "%(vip_idx)s, " \
                  "%(tunnel_color)s, " \
                  "%(host_name)s, " \
                  "%(vpn_id)s, " \
                  "%(id)s" \
                  ")"
            cursor.execute(sql, item)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

print(connection.open)
