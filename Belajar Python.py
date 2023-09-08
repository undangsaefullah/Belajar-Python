#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# data_manager.py

# Inisialisasi dictionary untuk menyimpan data
data = {}

# Fungsi untuk memasukkan data
def masukkan_data():
    id_operator = input("Masukkan ID Opertor: ")
    id_station_proses = input("Masukkan ID Station Proses: ")
    data[id_operator] = id_station_proses
    print("Data berhasil dimasukkan.")

# Fungsi untuk mengubah data
def ubah_data():
    id_operator = input("Masukkan id operator yang ingin diubah: ")
    if id_operator in data:
        id_station_proses = input("Masukkan id station: ")
        data[id_operator] = id_station_proses
        print("Data berhasil diubah.")
    else:
        print("Id operator tidak ditemukan.")

# Fungsi untuk menghapus data
def hapus_data():
    id_operator = input("Id operator yang ingin dihapus: ")
    if id_operator in data:
        del data[id_operator]
        print("Data berhasil dihapus.")
    else:
        print("Id operator tidak ditemukan.")

# Fungsi untuk melakukan scan barcode
def scan_barcode():
    barcode = input("Masukkan barcode yang ingin di-scan: ")
    print(f"Barang dengan barcode {barcode} berhasil di-scan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Pilih menu:")
    print("1. Masukan Data")
    print("2. Cari Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Scan barcode")
    print("6. Kirim Data")
    print("7. Keluar")

# Fungsi untuk mengirim data
def kirim_data():
    print("Data yang akan dikirim:")
    for id_operator, id_station in data.items():
        print(f"{id_operator}: {id_station_proses}")
    print("Data berhasil dikirim.")

# Fungsi untuk mencari data

def cari_data():
    kata_kunci = input("Masukkan kata kunci pencarian: ")
    found = False
    for id_operator, id_station_proses in data.items():
        if kata_kunci.lower() in id_operator.lower() or kata_kunci.lower() in id_station_proses.lower():
            print(f"ID Operator: {id_operator}, ID Station Proses: {id_station_proses}")
            found = True
    if not found:
        print("Data tidak ditemukan.")
    
# Fungsi untuk menjalankan program utama
def jalankan_program():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            masukkan_data()
        elif pilihan == "2":
            cari_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            scan_barcode()
        elif pilihan == "6":
            kirim_data()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

# Jika modul ini dijalankan sebagai program utama, jalankan programnya
if __name__ == "__main__":
    jalankan_program()

# In[ ]:




