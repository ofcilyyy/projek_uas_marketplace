from user import User, Admin, Customer
from product import Product
from order import Order

class Marketplace:
    def __init__(self):
        self.products = []
        self.orders = []
        self.order_counter = 1001

    # 1. Manajemen Produk (Admin)
    def add_product(self, product):
        self.products.append(product)
        print(f"[ADMIN] Produk '{product.name}' berhasil ditambahkan.")

    def delete_product(self, product_id):
        for prod in self.products:
            if prod.product_id == product_id:
                self.products.remove(prod)
                print(f"[ADMIN] Produk ID {product_id} berhasil dihapus.")
                return
        print(f"[ADMIN] Produk ID {product_id} tidak ditemukan.")

    def view_products(self):
        print("\n--- DAFTAR PRODUK MARKETPLACE ---")
        if not self.products:
            print("(Belum ada produk yang tersedia)")
        for prod in self.products:
            print(prod.get_details())

    # 2. Transaksi & Keranjang (Customer)
    def add_to_cart(self, customer, product_id):
        for prod in self.products:
            if prod.product_id == product_id:
                customer.cart.append(prod)
                print(f"[KERANJANG] '{prod.name}' dimasukkan ke keranjang {customer.username}.")
                return
        print("[KERANJANG] Produk tidak ditemukan.")

    def checkout(self, customer):
        if not customer.cart:
            print("[CHECKOUT] Keranjang belanja kosong!")
            return None
        
        new_order = Order(self.order_counter, customer, customer.cart)
        self.orders.append(new_order)
        self.order_counter += 1
        customer.cart.clear() # Kosongkan keranjang setelah checkout
        print("[CHECKOUT] Berhasil membuat pesanan baru!")
        return new_order

    # 3. Penerapan Polymorphism & Subtyping
    def authenticate_user(self, user: User, password_input):
        """
        Polymorphism: Menerima objek bertipe dasar 'User', 
        namun menjalankan method login() spesifik milik Admin atau Customer.
        """
        return user.login(password_input)
    