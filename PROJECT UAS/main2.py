from marketplace import Marketplace
from product import Product
from user import Admin, Customer

def main():
    marketplace = Marketplace()
    
    users_db = {
        "admin1": Admin("admin1", "admin123")
    }

    marketplace.add_product(Product("P001", "Laptop ASUS ROG", 15000000))
    marketplace.add_product(Product("P002", "Mouse Wireless Logi", 250000))

    while True:
        print("\n=====================================")
        print("    SELAMAT DATANG DI MARKETPLACE    ")
        print("=====================================")
        print("1. Login Akun")
        print("2. Daftar Akun Baru (Customer)")
        print("3. Keluar Aplikasi")
        pilihan_utama = input("Pilih menu (1-3): ")

        # --- MENU 1: LOGIN ---
        if pilihan_utama == "1":
            print("\n--- MENU LOGIN ---")
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")

            if username in users_db:
                user_obj = users_db[username]
                
                if marketplace.authenticate_user(user_obj, password):
                    
                    # === ROLE: ADMIN ===
                    if user_obj.role == "Admin":
                        while True:
                            print(f"\n=== MENU UTAMA ADMIN ({user_obj.username}) ===")
                            print("1. Tambah Produk Baru")
                            print("2. Hapus Produk")
                            print("3. Lihat Semua Produk")
                            print("4. Logout")
                            pilihan_admin = input("Pilih menu (1-4): ")

                            if pilihan_admin == "1":
                                p_id = input("Masukkan ID Produk (ex: P003): ")
                                p_name = input("Masukkan Nama Produk: ")
                                p_price = int(input("Masukkan Harga Produk (Angka): "))
                                marketplace.add_product(Product(p_id, p_name, p_price))
                            elif pilihan_admin == "2":
                                p_id = input("Masukkan ID Produk yang ingin dihapus: ")
                                marketplace.delete_product(p_id)
                            elif pilihan_admin == "3":
                                marketplace.view_products()
                            elif pilihan_admin == "4":
                                print("[INFO] Admin berhasil logout.")
                                break
                            else:
                                print("[ERROR] Pilihan tidak valid.")

                    # === ROLE: CUSTOMER ===
                    elif user_obj.role == "Customer":
                        while True:
                            print(f"\n=== MENU UTAMA CUSTOMER ({user_obj.username}) ===")
                            print("1. Lihat Produk Marketplace")
                            print("2. Tambah Produk ke Keranjang")
                            print("3. Checkout Keranjang & Buat Pesanan")
                            print("4. Logout")
                            pilihan_cust = input("Pilih menu (1-4): ")

                            if pilihan_cust == "1":
                                marketplace.view_products()
                            
                            elif pilihan_cust == "2":
                                marketplace.view_products()
                                p_id = input("\nMasukkan ID Produk yang ingin dibeli: ")
                                marketplace.add_to_cart(user_obj, p_id)
                            
                            elif pilihan_cust == "3":
                                pesanan = marketplace.checkout(user_obj)
                                if pesanan:
                                    pesanan.display_invoice()
    
                                    input("\nTekan Enter untuk memproses pesanan...")
                                    pesanan.update_status("Diproses")
                                    pesanan.display_invoice()
    
                                    print("\nApakah Anda ingin membatalkan pesanan ini?")
                                    pembatalan = input("Ketik 'CANCEL' untuk membatalkan, atau tekan Enter untuk melanjutkan: ")
                                    
                                    if pembatalan.upper() == "CANCEL":
                                        if pesanan.cancel_order(): 
                                            pesanan.display_invoice()
                                            continue # Kembali ke menu utama customer, lewati proses "Selesai"
                                    
                                    # Jika tidak mengetik CANCEL, lanjut ke status Selesai
                                    input("\nTekan Enter untuk menyelesaikan pesanan...")
                                    pesanan.update_status("Selesai")
                                    pesanan.display_invoice()
                            
                            elif pilihan_cust == "4":
                                print("[INFO] Customer berhasil logout.")
                                break
                            else:
                                print("[ERROR] Pilihan tidak valid.")
            else:
                print("\n[GAGAL] Username tidak terdaftar di sistem!")

        # --- MENU 2: DAFTAR AKUN BARU (Kini Sejajar dengan Menu 1) ---
        elif pilihan_utama == "2":
            print("\n--- DAFTAR AKUN BARU ---")
            new_username = input("Buat Username Baru: ")
            
            if new_username in users_db:
                print("[GAGAL] Username sudah digunakan! Silakan cari nama lain.")
            else:
                new_password = input("Buat Password Baru: ")
                users_db[new_username] = Customer(new_username, new_password)
                print(f"[SUKSES] Akun Customer '{new_username}' berhasil didaftarkan!")

        # --- MENU 3: KELUAR (Kini Sejajar dengan Menu 1) ---
        elif pilihan_utama == "3":
            print("\nTerima kasih telah menggunakan sistem marketplace ini!")
            break
        
        else:
            print("[ERROR] Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
