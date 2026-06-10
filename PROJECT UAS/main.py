from marketplace import Marketplace
from product import Product
from user import Admin, Customer

def main():
    
    # Inisialisasi Sistem
    tokopedia_kw = Marketplace()

    # Membuat Akun Pengguna
    admin_toko = Admin("superadmin", "admin123")
    pembeli_budhi = Customer("budhi_s", "rahasia123")

    print("=== SIMULASI 1: OTENTIKASI (POLYMORPHISM) ===")
    # Login Admin
    if tokopedia_kw.authenticate_user(admin_toko, "admin123"):
        print("\n=== SIMULASI 2: MANAJEMEN PRODUK (ADMIN) ===")
        p1 = Product("P001", "Laptop ASUS ROG", 15000000)
        p2 = Product("P002", "Mouse Wireless Logi", 250000)
        p3 = Product("P003", "Keyboard Mechanical", 750000)
        
        tokopedia_kw.add_product(p1)
        tokopedia_kw.add_product(p2)
        tokopedia_kw.add_product(p3)
        
        tokopedia_kw.delete_product("P003") # Hapus produk keyboard

    # Login Customer
    if tokopedia_kw.authenticate_user(pembeli_budhi, "rahasia123"):
        print("\n=== SIMULASI 3: TRANSAKSI BELANJA (CUSTOMER) ===")
        tokopedia_kw.view_products() # Lihat produk yang tersedia
        
        # Tambah ke keranjang
        tokopedia_kw.add_to_cart(pembeli_budhi, "P001")
        tokopedia_kw.add_to_cart(pembeli_budhi, "P002")
        
        # Checkout pesanan
        pesanan_budhi = tokopedia_kw.checkout(pembeli_budhi)
        
        if pesanan_budhi:
            print("\n=== SIMULASI 4: PENGELOLAAN STATUS PESANAN ===")
            pesanan_budhi.display_invoice() # Status bawaan: Pending
            
            # Update status pesanan ke Diproses
            pesanan_budhi.update_status("Diproses")
            pesanan_budhi.display_invoice()
            
            # Update status pesanan ke Selesai
            pesanan_budhi.update_status("Selesai")
            pesanan_budhi.display_invoice()

if __name__ == "__main__":
    main()
