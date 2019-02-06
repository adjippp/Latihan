class AnggotaSekolah:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        print('Membuat anggota sekolah baru: %s' % self.nama)
    def info(self):
        "cetak info"
        print('Nama: %s, Umur: %s' % (self.nama, self.umur))
class Guru(AnggotaSekolah):
    def __init__(self,nama,umur,gaji):
        AnggotaSekolah.__init__(self,nama,umur)
        self.gaji = gaji
        print('Membuat guru: %s' % self.nama)
    def info(self):
        AnggotaSekolah.info(self)
        print('Gaji: %s' % self.gaji)

class Siswa(AnggotaSekolah):
    def __init__(self, nama,umur, nilai):
        AnggotaSekolah.__init__(self, nama, umur)
        self.nilai = nilai
        print('Membuat siswa: %s' % self.nama)
    def info(self):
        AnggotaSekolah.info(self)
        print('Nilai: %s' % self.nilai)

guru=Guru('Adji Pratama', 27, 10000000)
siswa=Siswa('You Know Who', 15, 78)
print('')
print('')
anggota = [guru,siswa]
for orang in anggota:
    orang.info()