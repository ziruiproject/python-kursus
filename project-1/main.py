import csv, services
import pandas as pd

while (True):
    print()
    print("===== Product Management App =====")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan Id")
    print("3. Tambah Barang")
    print("4. Hapus Barang")
    print("5. Keluar")
    user_input = int(input("Masukan pilihan: "))

    if user_input == 1:
        services.Product.read()
    elif user_input == 2:
        user_input = int(input("Masukan Id Produk: "))
        services.Product.get_by_id(2)
    elif user_input == 3:
        user_input = int(input("Masukan banyak produk yang ingin tambahkan: "))
        product_queue = services.ProductCreationQueue()
        for i in range(user_input):
            print()
            print("Barang ke", i + 1)
            nama_barang = str(input("Masukan nama barang: "))
            harga_barang = int(input("Masukan harga barang: "))
            stok_barang = int(input("Masukan stok barang: "))
            data_barang = {
                "name" : nama_barang,
                "price" : harga_barang,
                "stock" : stok_barang
            }
            product_queue.add_product(data_barang)
        product_queue.process_queue()
    elif user_input == 4:
        user_input = int(input("Masukan id barang: "))
        services.Product.delete(user_input)
    else:
        print("Selamat tinggal")
        break
        
        