class Buku:
    def __init__(self,judul,penulis,tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "tersedia"

    

    def pinjam(self):
        if self.status == "tersedia":
            self.status = "dipinjam"
            return True
        return False
    
    def dikembalikan(self):
        self.status = "tersedia"


class Anggota:
    def __init__(self,name,card_id):
        self.name = name
        self.card_id = card_id

class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []
        self.anggota_perpustakaan = []

    def tambah_buku(self,buku):
        self.koleksi_buku.append(buku)

    def daftar_buku(self):
        print("\n","="*10,"DAFTAR BUKU PERPUSTAKAAN","="*10)
        for buku in self.koleksi_buku:
            print(f"\njudul : {buku.judul}\npenulis : {buku.penulis}\ntahun : {buku.tahun}")

    def tambah_anggota(self,anggota):
        self.anggota_perpustakaan.append(anggota)

    def show_all_anggota(self):
        print("\n","="*10,"DAFTAR ANGGOTA PERPUSTAKAAN","="*10)
        for anggota in self.anggota_perpustakaan:
            print(f"\nname = {anggota.name}\ncard_id = {anggota.card_id}")

    def pinjam_buku(self, judul, nama, card_id):
        for buku in self.koleksi_buku:
            if buku.judul == judul:
                if buku.pinjam():
                    print(f"Buku '{buku.judul}' sudah dipinjam oleh {nama} (ID Kartu: {card_id})")
                    return
                else:
                    print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                    return
                
        print(f"Buku '{judul}' tidak ditemukan di perpustakaan.")

    def kembalikan_buku(self,judul):
        for buku in self.koleksi_buku:
            if buku.judul == judul:
                buku.dikembalikan()
                print(f"buku {buku.judul} berhasil di kembalikan")
                return
                
        print(f"{buku.judul}tidak di temukan di perpustakaan")

#penggunaan proyek
perpustakaan = Perpustakaan()

buku1 = Buku("teori charles darwin","charles darwin",2013)
buku2 = Buku("BigBang","isaac newton",1800)
buku3 = Buku("psychology of money","chris swatt",2022)

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)
perpustakaan.daftar_buku()

anggota1 = Anggota("Farel Azizakli","A001")
anggota2 = Anggota("Hasna tri anjani","A002")


perpustakaan.tambah_anggota(anggota1)
perpustakaan.tambah_anggota(anggota2)
perpustakaan.show_all_anggota()

#farel azizakli meminjam buku psychology of money

perpustakaan.pinjam_buku("psychology of money","Farel Azizakli","A001")
perpustakaan.pinjam_buku("psychology of money","Hasna tri anjani","A002")

perpustakaan.kembalikan_buku("psychology of money")
perpustakaan.pinjam_buku("psychology of money","Hasna tri anjani","A002")










