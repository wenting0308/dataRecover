from dataRecover.rds_config import *
from dataRecover.link_to_mysql import *
import pymysql
import json
import time
import datetime

def main():
# request station data from API
    file_in = '../in.json'
    data_json = open(file_in).read()
    station_json = json.loads(data_json) # data type: list
    
    # get connection of MySQL server
    conn = connect_to_sql(object)
    cur = conn.cursor()
    
    # delete data before insert new data
    stm = ('DELETE FROM stations_real_time WHERE `number` is not null')
    cur.execute(stm)
        
    # insert data into table station
    insert_stmt = (
        "INSERT INTO stations_real_time (number, contract_name, banking, bonus, status, bike_stands, \
        available_bike_stands, available_bikes, last_update_timestamp, last_update_date, data_insert_date)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" )
    
    count = 0
    for d in station_json:
        t = d["last_update_date"]
        st = time.strptime(t, '%Y-%m-%d %H:%M:%S')
        
        if( time.mktime(st) > time.mktime(time.strptime('2017-03-25', '%Y-%m-%d')) and \
            time.mktime(st) < time.mktime(time.strptime('2017-04-02', '%Y-%m-%d'))  ):
            
            #print(type(d["number"]), d["contract_name"])
            cur.execute(insert_stmt, (d["number"], d["contract_name"], d["banking"], \
                                  d["bonus"], d["status"], d["bike_stands"], d["available_bike_stands"], \
                                  d["available_bikes"], d["last_update_timestamp"], d["last_update_date"], d["data_insert_date"]))
            #print('still run..insert row number: ', count)
            conn.commit()
    
    cur.close()
    conn.close()
    print("Done")
    
if __name__ == '__main__':
    main()
