
import dframe as df
import Admin as adm

from Admin import *

from dframe import *
import socket
import csv

host='10.30.203.247'
port=6000
s = socket.socket()
try :
    s.bind((host,port))
except socket.error as e:
    print(str(e))
print("WAITING FOR THE CONNECTION\n")
s.listen(5)
print("updating database")

while True:
    conn, addr = s.accept()
    print("connected by",addr)

    data=conn.recv(2048).decode()

    with open('Voterlist.csv','w') as file:
        writer = csv.writer(file)
        writer.writerows([row.split(',') for row in data.split('\n')])
        print("database updated")

    conn.close()