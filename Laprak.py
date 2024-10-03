produk_toko = {
    "Mainan": 20000,
    "Obat": 10000,
    "Snack": 15000,
    "Minuman": 15000
}
keranjang_belanja = {}
def tambah_ke_keranjang():
    nama_produk = input("Masukkan nama produk: ")
    if nama_produk in produk_toko:
        jumlah = int(input(f"Masukkan jumlah {nama_produk}: "))
        if nama_produk in keranjang_belanja:
            keranjang_belanja[nama_produk] += jumlah
        else:
            keranjang_belanja[nama_produk] = jumlah
        print(f"{jumlah} {nama_produk} telah dimasukan ke list keranjang.")
    else:
        print("Produk tidak ada di toko ini.")

def hitung_total_harga():
    total_harga = 0
    for produk, jumlah in keranjang_belanja.items():
        total_harga += produk_toko[produk] * jumlah
    return total_harga

class Toko:
    def tampilkan_keranjang(self):
        if keranjang_belanja:
            print("Produk dalam keranjang belanja Anda:")
            for produk, jumlah in keranjang_belanja.items():
                print(f"{produk} - Jumlah: {jumlah}, Harga satuan: {produk_toko[produk]}")
        else:
            print("Keranjang belanja Anda kosong.")

class Checkout:
    def lakukan_checkout(self):
        if keranjang_belanja:
            total = hitung_total_harga()
            print(f"Total Belanja: Rp {total}")
            return total
        else:
            print("Keranjang belanja kosong.")
            return 0

def main():
    toko = Toko()
    checkout_obj = Checkout()
    
    while True:
        print("\n1. Tambah Produk \n2. Tampilkan Keranjang \n3. Bayar\n4. Keluar")
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            tambah_ke_keranjang()
        elif pilihan == '2':
            toko.tampilkan_keranjang()
        elif pilihan == '3':
            checkout_obj.lakukan_checkout()
        elif pilihan == '4':
            print("Terima kasih sudah berbelanja")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()