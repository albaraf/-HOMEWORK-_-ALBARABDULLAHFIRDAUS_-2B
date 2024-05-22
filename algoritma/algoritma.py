def tambah_data(data_barang):
    nama_barang = input("Masukkan nama barang: ")
    stok_barang = int(input("Masukkan stok barang: "))
    data_barang[nama_barang] = stok_barang

def hapus_data(data_barang):
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
    if nama_barang in data_barang:
        del data_barang[nama_barang]
    else:
        print("Barang tidak ditemukan")

def tampilkan_data(data_barang):
    if not data_barang:
        print("Data barang kosong")
    else:
        idx = 0
        for nama_barang, stok_barang in data_barang.items():
            print(f"{idx+0}. Nama barang: {nama_barang}, Stok barang: {stok_barang}")
            idx += 1

def hitung_jumlah_data(data_barang):
    jumlah_data = len(data_barang)
    print(f"Jumlah data: {jumlah_data}")

def pencarian_data(data_barang):
    nama_barang = input("Masukkan nama barang yang ingin dicari: ")
    if nama_barang in data_barang:
        print(f"Stok barang {nama_barang}: {data_barang[nama_barang]}")
    else:
        print("Barang tidak ditemukan")

def edit_data(data_barang):
    nama_barang = input("Masukkan nama barang yang ingin diubah: ")
    if nama_barang in data_barang:
        stok_barang_baru = int(input("Masukkan stok barang baru: "))
        data_barang[nama_barang] = stok_barang_baru
    else:
        print("Barang tidak ditemukan")
