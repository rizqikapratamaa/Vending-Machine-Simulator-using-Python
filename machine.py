# TUGAS BESAR 1: VENDING MACHINE

# Kelompok 4
# Jason Fernando / 19622254
# Rizqika Mulia Pratama / 19622258
# Alfaza Naufal Zakiy / 19622264
# Chelvadinda / 19622276

# PROGRAM VENDING_MACHINE

# KAMUS
# makanan = array of array
# minuman = array of array
# saldo = integer
# ulang_program = Boolean
# ulang_pilih = Boolean
# ulang_produk = Boolean
# ulang_beli = Boolean
# cek_habis = Boolean
# pilihan = string
# pilihan_makanan = integer
# jumlah_makanan = integer
# harga_makanan = integer
# tambahan = integer
# lagi = string
# pilihan_minuman = integer
# jumlah_minuman = integer
# harga_minuman = integer


# ALGORITMA
import os, time
from tabulate import tabulate

# Menu makanan dan minuman dalam matriks
makanan = [["No", "Nama Makanan", "Harga", "Stok"], [1, "Kitela", 5000, 10], [2, "Silperkuin", 10000, 10], [3, "Biskuit Badtime", 9000, 10], [4, "Citato", 3000, 10], [5, "Lie's", 3000, 10]]
minuman = [["No", "Nama Minuman", "Harga", "Stok"], [1, "Teh Pucuk Haram", 3000, 10], [2, "Pocari Sweet", 6000, 10], [3, "Susu Kambing Jantan Rasa Apel Hijau", 8000, 10], [4, "Koka Kola", 6000, 10], [5, "Susu Beruang", 8500, 10]]

# Menu masukkan saldo
os.system("cls")                                                                                                                # Clear screen
print("================WELCOME TO DARMAJI VENDING MACHINE=============") 
isi_saldo = True
while isi_saldo == True:                                                                                                        # Looping input saldo
    saldo = int(input("Masukkan uang anda: "))
    if saldo == 0:                                                                                                              # Jika saldo hasil input = 0
        os.system("cls")
        print("Harap masukkan saldo!")
    else:                                                                                                                       # Jika saldo hasil input tidak 0 (asumsikan user selalu memasukkan angka positif)
        isi_saldo = False                                                                                                       # Hentikan loop input saldo

# Menu utama
ulang_program = True
while ulang_program == True:                                                                                                    # Looping agar selalu kembali ke menu utama
    os.system("cls")                                                                                                            # Clear screen
    print("=====================DARMAJI VENDING MACHINE===================")                                                    # Print header
    print("Jumlah saldo:", saldo)                                                                                               # Tampilkan jumlah saldo
    print()                                                                                                                     # Beri spasi
    ulang_pilih = True
    while ulang_pilih == True:                                                                                                  # Looping saat memilih makanan atau minuman
        os.system("cls")                                                                                                        # Clear screen
        print("=====================DARMAJI VENDING MACHINE===================")                                                # Print header
        print("Jumlah saldo:", saldo)                                                                                           # Tampilkan jumlah saldo
        print("Pilihan menu:")                                                                                                  # Tampilkan pilihan menu
        print("1. Makanan")
        print("2. Minuman")
        pilihan = input("Silahkan pilih menu: ")                                                                                # Input pilihan menu

        # Menu makanan
        if pilihan == "1" or pilihan == "Makanan" or pilihan == "makanan":                                                      # Jika pilihan = "1" atau "Makanan" atau "makanan", masuk ke halaman makanan
            ulang_produk = True
            while ulang_produk == True:                                                                                         # Mengulang menu makanan
                cek_habis = True
                while cek_habis == True:                                                                                        # Mengulang saat produk habis
                    os.system("cls")                                                                                            # Clear screen
                    print("=====================DARMAJI VENDING MACHINE===================")                                    # Tampilkan header
                    print("Jumlah saldo:", saldo)                                                                               # Tampilkan jumlah saldo
                    print(tabulate(makanan, headers="firstrow", tablefmt="fancy_grid"))                                         # Print menu makanan dengan menggunakan tabulate
                    pilihan_makanan = int(input("Masukkan nomor produk yang anda inginkan: "))                                  # Input pilihan makanan
                    jumlah_makanan = int(input("Jumlah produk yang hendak anda beli: "))                                        # Input jumlah makanan
                    if pilihan_makanan > 0 and pilihan_makanan <= 5:                                                            # Jika pilihan makanan ada dalam pilihan
                        if jumlah_makanan <= 10 and jumlah_makanan > 0:                                                         # Jika stok masih ada
                            if makanan[pilihan_makanan][3] == 0:                                                                # Jika stok habis
                                cek_habis = True
                                while cek_habis == True:                                                                        # Loop jika stok habis
                                    print(f"{makanan[pilihan_makanan][1]} habis.")                                              # Tampilkan makanan habis
                                    cek_ganti = input("Apakah mau ganti produk? (Y/N): ")                                       # Ganti produk
                                    if cek_ganti == "Y" or cek_ganti == "y":                                                    # Jika cek_ganti = Y atay cek_ganti = y
                                        cek_habis = False                                                                       # Hentikan loop ganti makanan
                                        ulang_produk = False                                                                    # Hentikan loop makanan untuk masuk ke menu utama
                                        ulang_beli = False                                                                      # Hentikan loop pembelian
                                    elif cek_ganti == "N" or cek_ganti == "n":                                                  # Jika tidak ganti menu
                                        print(f"Kembalian anda: {saldo}")                                                       # Tampilkan kembalian
                                        print("Terima kasih, semoga hari anda menyenangkan!")
                                        cek_habis = False                                                                       # Hentikan semua loop
                                        ulang_pilih = False
                                        ulang_produk = False
                                        ulang_beli = False
                                        ulang_program = False
                                    else:                                                                                       # Jika menginput hal lain, hentikan selama 3 detik, kemudian ulangi loop
                                        print("Invalid Syntax")
                                        time.sleep(3)
                                cek_habis = False                                                                               # Keluar dari loop pengecekhabisan
                            else:                                                                                               # Jika stok produk masih ada
                                cek_habis = False                                                                               # Keluar dari loop pengecekhabisan
                                harga_makanan = jumlah_makanan * makanan[pilihan_makanan][2]                                    # Hitung total harga
                                if pilihan_makanan > 0 and pilihan_makanan <= 5:                                                # Jika pilihan produk masih dalam range
                                    ulang_beli = True
                                    while ulang_beli == True:                                                                   # Lakukan looping pembelian
                                        if saldo < harga_makanan:                                                               # Jika saldo kurang dari harga
                                            os.system("cls")
                                            print("=====================DARMAJI VENDING MACHINE===================")
                                            print("Jumlah saldo:", saldo)                                                       # Tampilkan jumlah saldo
                                            print(tabulate(makanan, headers="firstrow", tablefmt="fancy_grid"))                 # Tampilkan tabel menu
                                            print("Saldo anda tidak cukup!")                                                    # Cetak saldo tidak cukup
                                            tambahan = int(input("Silahkan tambahkan saldo anda: "))                            # Masukkan saldo tambahan
                                            saldo += tambahan                                                                   # Tambahkan saldo awal dengan tambahan saldo
                                            ulang_beli = False                                                                  # Hentikan loop pembelian
                                        else:                                                                                   # Jika saldo cukup
                                            saldo -= harga_makanan                                                              # Kurangi saldo dengan harga yang perlu dibayar
                                            print()
                                            print("===============Makanan Keluar===============")
                                            print(str(jumlah_makanan)+"X", makanan[pilihan_makanan][1])                         # Tampilkan jumlah dan nama produk yang dibeli    
                                            print(f"Harga: {harga_makanan}")                                                    # Tampilkan harga yang perlu dibayar
                                            print(f"Sisa Saldo: {saldo}")                                                       # Tampilkan sisa saldo
                                            print("================Terima Kasih================")
                                            makanan[pilihan_makanan][3] -= jumlah_makanan                                       # Kurangi stok produk yang dibeli
                                            print()
                                            ulang_program = True
                                            while ulang_program == True:                                                        # Loop pembelian
                                                lagi = input("Apakah anda mau beli yang lain? (Y/N): ")                         # Masukkan mau beli lagi atau tidak
                                                if lagi == "Y" or lagi == "y":                                                  # Jika ya
                                                    ulang_program = False                                                       # Hentikan semua loop kecuali loop untuk memilih menu, agak bisa kembali ke menu awal
                                                    ulang_produk = False
                                                    ulang_beli = False
                                                elif lagi == "N" or lagi == "n":                                                # Jika tidak mau beli lagi
                                                    print(f"Kembalian anda: {saldo}")                                           # Tampilkan kembalian
                                                    print("Terima kasih, semoga hari anda menyenangkan!")
                                                    ulang_program = False                                                       # Hentikan seluruh loop
                                                    ulang_produk = False
                                                    ulang_pilih = False
                                                    ulang_beli = False
                                                else:                                                                           # Jika user menginput hal lain, ulangi loop "lagi"
                                                    print("Invalid Syntax")
                                                    time.sleep("")
                                            ulang_program = False                                                               # Hentikan loop pengulangan program
                                    ulang_beli = False                                                                          # Hentikan loop pengulangan pembelian
                        else:                                                                                                   # Jika user salah memilih pilihan
                            print(f"Stok {makanan[pilihan_makanan][1]} kurang dari {jumlah_makanan}, silahkan input ulang.")          
                            time.sleep(3)
                    else:                                                                                                       # Jika user salah menginput pilihan
                        print(f"Pilihan anda tidak ada di menu")
                        time.sleep(3)


        # Menu minuman
        elif pilihan == "2" or pilihan == "Minuman" or pilihan == "minuman":                                                    # Jika pilihan = "2" atau "Minuman" atau "minuman"
            ulang_produk = True
            while ulang_produk == True:                                                                                         # Loop pembelian minuman
                cek_habis = True
                while cek_habis == True:                                                                                        # Loop untuk cek habis
                    os.system("cls")
                    print("=====================DARMAJI VENDING MACHINE===================")
                    print("Jumlah saldo:", saldo)                                                                               # Tampilkan saldo
                    print(tabulate(minuman, headers="firstrow", tablefmt="fancy_grid"))                                         # Tampilkan menu
                    pilihan_minuman = int(input("Masukkan nomor produk yang anda inginkan: "))                                  # Masukkan pilihan produk
                    jumlah_minuman = int(input("Jumlah produk yang hendak anda beli: "))                                        # Masukkan jumlah produk yang hendak dibeli
                    if pilihan_minuman > 0 and pilihan_minuman <= 5:                                                            # Jika pilihan masih dalam range pilihan produk
                        if jumlah_minuman <= 10 and jumlah_minuman > 0:                                                         # Jika jumlah minuman yang dimasukkan masih dalam range stok produk
                            if minuman[pilihan_minuman][3] == 0:                                                                # Jika stok produk habis
                                cek_habis = True
                                while cek_habis == True:                                                                        # Loop untuk mengecek habis atau tidaknya stok
                                    print(f"{minuman[pilihan_minuman][1]} habis.")                                              # Cetak produk habis
                                    cek_ganti = input("Apakah mau ganti produk? (Y/N): ")                                       # Masukkan pilihan ganti menu atau tidak
                                    if cek_ganti == "Y" or cek_ganti == "y":                                                    # Jika ya
                                        cek_habis = False                                                                       # Hentikan semua loop kecuali loop untuk memilih menu, agar bisa kembali ke main menu
                                        ulang_produk = False
                                        ulang_beli = False
                                    elif cek_ganti == "N" or cek_ganti == "n":                                                  # Jika tidak
                                        print(f"Kembalian anda: {saldo}")                                                       # Cetak kembalian
                                        print("Terima kasih, semoga hari anda menyenangkan!")  
                                        cek_habis = False                                                                       # Matikan semua loop
                                        ulang_pilih = False
                                        ulang_produk = False
                                        ulang_beli = False
                                        ulang_program = False
                                    else:                                                                                       # Jika pilihan ganti selain ya dan tidak
                                        print("Invalid Syntax")
                                        time.sleep(3)
                                cek_habis = False                                                                               # Keluar dari loop cek habis
                            else:
                                cek_habis = False                                                                               # Keluar dari loop cek habis
                                harga_minuman = jumlah_minuman * minuman[pilihan_minuman][2]                                    # Hitung harga total yang perlu dibayar
                                if pilihan_minuman > 0 and pilihan_minuman <= 5:                                                # Jika input pilihan masih dalam range
                                    ulang_beli = True
                                    while ulang_beli == True:                                                                   # Loop pengulangan beli
                                        if saldo < harga_minuman:                                                               # Jika sisa saldo kurang dari
                                            os.system("cls")                                                                    # Clear screen
                                            print("=====================DARMAJI VENDING MACHINE===================")
                                            print("Jumlah saldo:", saldo)                                                       # Tampilkan jumlah saldo
                                            print(tabulate(minuman, headers="firstrow", tablefmt="fancy_grid"))                 # Tampilkan produk
                                            print("Saldo anda tidak cukup!")                                                    # Cetak saldo tidak cukup
                                            tambahan = int(input("Silahkan tambahkan saldo anda: "))                            # Masukkan saldo tambahan
                                            saldo += tambahan                                                                   # Tambahkan saldo awal dengan saldo tambahan
                                            ulang_beli = False                                                                  # Hentikan loop penambahan saldo
                                        else:                                                                                   # Jika saldo cukup
                                            saldo -= harga_minuman                                                              # Kurangi saldo dengan total harga produk
                                            print()
                                            print("===============Minuman Keluar===============")
                                            print(str(jumlah_minuman)+"X", minuman[pilihan_minuman][1])                         # Cetak nama dan banyak produk yang dibeli
                                            print(f"Harga: {harga_minuman}")                                                    # Tampilkan harga produk
                                            print(f"Sisa Saldo: {saldo}")                                                       # Tampilkan sisa saldo
                                            print("================Terima Kasih================")
                                            minuman[pilihan_minuman][3] -= jumlah_minuman                                       # Kurangi jumlah stok produk dengan jumlah yang dibeli sebelumnya
                                            print()
                                            ulang_program = True
                                            while ulang_program == True:                                                        # Loop pembelian kembali
                                                lagi = input("Apakah anda mau beli yang lain? (Y/N): ")                         # Input mau beli lagi atau tidak
                                                if lagi == "Y" or lagi == "y":                                                  # Jika ya
                                                    ulang_program = False                                                       # Hentikan seluruh loop kecuali loop main menu agar bisa langsung kembali ke main menu
                                                    ulang_produk = False
                                                    ulang_beli = False
                                                elif lagi == "N" or lagi == "n":                                                # Jika tidak
                                                    print(f"Kembalian anda: {saldo}")
                                                    print("Terima kasih, semoga hari anda menyenangkan!")
                                                    ulang_program = False                                                       # Hentikan seluruh loop dan program selesai
                                                    ulang_produk = False
                                                    ulang_pilih = False
                                                    ulang_beli = False
                                                else:                                                                           # Jika input user tidak valid
                                                    print("Invalid Syntax")
                                                    time.sleep(3)
                                            ulang_program = False
                                    ulang_beli = False
                        else:                                                                                                   # Jika input user tidak valid            
                            print(f"Stok {minuman[pilihan_minuman][1]} kurang dari {jumlah_minuman}, silahkan input ulang.")     
                            time.sleep(3)                                                                                       
                    else:                                                                                                       # Jika input user tidak valid
                        print("Pilihan anda tidak ada di menu.")                                                                
                        time.sleep(3)                                                                                           
        else:                                                                                                                   # Jika input user tidak valid
            print("Invalid Syntax")                                                                                             
            time.sleep(3)                                                                                                       
ulang_program = False                                                                                                           # Hentikan loop