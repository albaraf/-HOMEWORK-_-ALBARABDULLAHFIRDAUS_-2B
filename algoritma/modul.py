import algoritma as ag

data_barang = {}

while True:
    print("\nPilih menu:")
    print("1. Tambah data barang")
    print("2. Hapus data barang")
    print("3. Tampilkan data barang")
    print("4. Hitung jumlah data barang")
    print("5. Pencarian data barang")
    print("6. Edit data barang")
    print("7. Keluar")

    menu = int(input("Masukkan pilihan Anda: "))

    if menu == 1:
        ag.tambah_data(data_barang)
    elif menu == 2:
        ag.hapus_data(data_barang)
    elif menu == 3:
        ag.tampilkan_data(data_barang)
    elif menu == 4:
        ag.hitung_jumlah_data(data_barang)
    elif menu == 5:
        ag.pencarian_data(data_barang)
    elif menu == 6:
        ag.edit_data(data_barang)
    elif menu == 7:
        break
    else:
        print("Pilihan tidak valid")