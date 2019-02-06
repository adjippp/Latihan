class Orang:
    total=0
    def __init__(self, nama):
        self.nama = nama
        Orang.total+=1
    def sayHello(self):
        print("Hallo , apa kabar? nama saya %s" % self.nama)
    def __del__(self):
        Orang.total-=1
    def total_populasi(cls):
        print("Total orang %s" % cls.total)
    total_populasi= classmethod(total_populasi)

org = Orang('Adji')
Orang.total_populasi()
org2 = Orang('Budi')
org3 = Orang('Chandra')
Orang.total_populasi()
print("Hapus 1 Orang")
del org2
Orang.total_populasi()