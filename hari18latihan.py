import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="adji",
  passwd="123456",
  database="datascience"
)
kursor = mydb.cursor()

def getIDKota(namaKota):
  cekKota="select id from kotax where nama=%s"
  nama = (namaKota, )
  kursor.execute(cekKota, nama)
  hasilid=kursor.fetchone()

  return hasilid[0]

def getIDOrangTerakhir():
  #nge cek id paling terakhir
  cekIDOrangTerakhir='select * from orang'
  kursor.execute(cekIDOrangTerakhir)
  hasil=kursor.fetchall()
  idOrang=hasil[len(hasil)-1][0]
  return idOrang

def inputDataUser(nama, namaKota):
  perintah = 'insert into orang (nama) values (%s)'
  inputan = (nama, )
  kursor.execute(perintah,inputan)
  mydb.commit()
  return ("id Anda: "+str(getIDOrangTerakhir())+"Nama Anda: "+nama)+" "+kotaChecker(namaKota)

def kotaChecker(namaKota):
  cekKota='select nama from kotax'
  kursor.execute(cekKota)
  hasil=kursor.fetchall()
  tampungKota=[]
  for i in range(len(hasil)):
    tampungKota.append(hasil[i][0])
  idorang=getIDOrangTerakhir()
  idkota=getIDKota(namaKota)
  if (namaKota in tampungKota == True):
      perintah = 'insert into orangkotax (id_orang,id_kota) values (%s,%s)'
      inputan = (idorang,idkota)
      kursor.execute(perintah,inputan)
      mydb.commit()
      return ("Kota "+namaKota," Sudah Terdaftar, id Kota: "+str(idkota))
  else:
      perintah = 'insert into kotax (nama) values (%s)'
      inputan = (namaKota, )
      kursor.execute(perintah,inputan)
      mydb.commit()
      perintah2 = 'insert into orangkotax (id_orang,id_kota) values (%s,%s)'
      inputan2 = (idorang,idkota)
      kursor.execute(perintah2,inputan2)
      mydb.commit()
      return ("Kota "+namaKota+" Akan Ditambahkan (Karena Belum Terdaftar), id Kota: "+str(idkota))

# inputnama=input("Masukkan nama Anda: ")
# inputkota=input("Masukkan kota Anda: ")
# print(inputDataUser(inputnama,inputkota))