class Order:    
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer  # Interaksi antar objek (User-Customer)
        self.items = list(items)  # Interaksi antar objek (Product)
        self.status = "Pending"

    def update_status(self, new_status):
        # Tambahkan "Dibatalkan" ke dalam list valid_status agar sistem menerimanya
        valid_status = ["Pending", "Diproses", "Selesai", "Dibatalkan"]
        if new_status in valid_status:
            self.status = new_status
            print(f"[INFO] Status Pesanan #{self.order_id} diperbarui menjadi: {self.status}")
        else:
            print("[ERROR] Status tidak valid!")

    # === TAMBAHKAN FUNGSI BARU DI SINI ===
    def cancel_order(self):
        """
        Fungsi untuk membatalkan pesanan. 
        Pesanan hanya bisa dibatalkan jika statusnya masih 'Pending' atau 'Diproses'.
        """
        if self.status == "Pending" or self.status == "Diproses":
            self.status = "Dibatalkan"
            print(f"[SUKSES] Pesanan #{self.order_id} berhasil dibatalkan.")
            return True
        else:
            print(f"[GAGAL] Pesanan #{self.order_id} tidak bisa dibatalkan karena sudah '{self.status}'.")
            return False

    def display_invoice(self):
        print(f"\n=== NOTA PESANAN #{self.order_id} ===")
        print(f"Pelanggan : {self.customer.username}")
        print(f"Status    : {self.status}")
        print("Daftar Produk:")
        total = 0
        for item in self.items:
            print(f" - {item.name} (Rp{item.price:,})")
            total += item.price
        print(f"Total Bayar: Rp{total:,}")
        print("=============================")
