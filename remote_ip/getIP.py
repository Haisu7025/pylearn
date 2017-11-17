#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import MySQLdb

db = MySQLdb.connect("")
cursor = db.cursor()
response = requests.get("http://ip.chinaz.com")
res = re.search('<dd class="fz24">(.*)</dd>',
                response.text.encode('utf - 8'), re.M | re.I)

sql = "SELECT * FROM IPTABLE WHERE place='home'"
cursor.execute(sql)
l = len(cursor.fetchall())
print l
if l == 0:
    sql = "INSERT INTO IPTABLE (ip,place,time) VALUES ('" + \
        res.group(1) + "','home',SYSDATE())"
    cursor.execute(sql)
    db.commit()
else:
    sql = "UPDATE IPTABLE set ip='" + \
        res.group(1) + "',time=SYSDATE() WHERE place='home'"
    cursor.execute(sql)
    db.commit()
db.close()
