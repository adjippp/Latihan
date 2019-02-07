import json
import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="adji",
  passwd="123456",
  database="datascience"
)
kursor=mydb.cursor()

data=[]
def getKota():
    query='select o.id, o.nama, k.nama, k.id from orang o,orangkotax z,kotax k where o.id=z.id_orang and z.id_kota=k.id'
    kursor.execute(query)
    hasil=kursor.fetchall()
    panjang=len(hasil)
    for i in range(panjang):
        isi={
            'id_orang' : hasil[i][0],
            'nama_orang' : hasil[i][1],
            'nama_kota' : hasil[i][2],
            'id_kota': hasil[i][3]
        }
        data.append(isi)

    return data

isijson=json.dumps(getKota())
file = open('backupdatabaseorangdankota.json','w+')
file.write(isijson)
file.close()