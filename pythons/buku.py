import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# DATA HARGA
# =========================

harga_alat = {
    "pensil": 2000,
    "pulpen": 3000,
    "penghapus": 1500
}

harga_buku = {
    "buku_tulis": 5000,
    "buku_gambar": 6000
}

# =========================
# FUNGSI TUGAS
# =========================

def HitungTotalAlatTulis(kode_alat, jumlah):
    return harga_alat.get(kode_alat, 0) * jumlah


def HitungTotalBuku(kode_buku, jumlah):
    return harga_buku.get(kode_buku, 0) * jumlah


def HitungDiskon(total):
    if total >= 75000:
        return total * 0.15
    return 0


def HitungPajak(total_setelah_diskon):
    return total_setelah_diskon * 0.03


def TampilkanDetail(item, jumlah, harga, total):
    return f"{item} x {jumlah} = Rp {total:,.0f}"


# =========================
# DATA PESANAN
# =========================

pesanan = []


# =========================
# EVENT
# =========================

def tambah_pesanan():
    item_tampil = combo_item.get()

    item = item_tampil.lower().replace(" ", "_")

    try:
        jumlah = int(entry_jumlah.get())

        if jumlah <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Jumlah harus berupa angka positif!"
        )
        return

    if item in harga_alat:
        harga = harga_alat[item]

    elif item in harga_buku:
        harga = harga_buku[item]

    else:
        messagebox.showerror(
            "Error",
            "Item tidak ditemukan!"
        )
        return

    subtotal = harga * jumlah

    pesanan.append((item, jumlah))

    listbox.insert(
        tk.END,
        f"{item_tampil} x {jumlah} = Rp {subtotal:,.0f}"
    )

    entry_jumlah.delete(0, tk.END)


def hitung_total():

    if not pesanan:
        messagebox.showwarning(
            "Peringatan",
            "Belum ada pesanan!"
        )
        return

    total = 0

    for item, jumlah in pesanan:

        if item in harga_alat:
            subtotal = HitungTotalAlatTulis(
                item,
                jumlah
            )
        else:
            subtotal = HitungTotalBuku(
                item,
                jumlah
            )

        total += subtotal

    diskon = HitungDiskon(total)

    total_setelah_diskon = total - diskon

    pajak = HitungPajak(total_setelah_diskon)

    total_bayar = total_setelah_diskon + pajak

    hasil.config(
        text=
        f"Total        : Rp {total:,.0f}\n"
        f"Diskon       : Rp {diskon:,.0f}\n"
        f"Pajak 3%     : Rp {pajak:,.0f}\n"
        f"-----------------------------\n"
        f"TOTAL BAYAR  : Rp {total_bayar:,.0f}"
    )


def reset():
    pesanan.clear()

    listbox.delete(0, tk.END)

    hasil.config(text="")

    entry_jumlah.delete(0, tk.END)

    combo_item.current(0)


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Toko Buku Sekolah")
root.geometry("600x650")

judul = tk.Label(
    root,
    text="=== TOKO BUKU SEKOLAH ===",
    font=("Arial", 16, "bold")
)
judul.pack(pady=10)

info = tk.Label(
    root,
    text=
    "Pensil = Rp 2.000\n"
    "Pulpen = Rp 3.000\n"
    "Penghapus = Rp 1.500\n"
    "Buku Tulis = Rp 5.000\n"
    "Buku Gambar = Rp 6.000",
    justify="left"
)
info.pack(pady=5)

# Dropdown Item
tk.Label(
    root,
    text="Pilih Item"
).pack()

combo_item = ttk.Combobox(
    root,
    state="readonly",
    width=30,
    values=[
        "Pensil",
        "Pulpen",
        "Penghapus",
        "Buku Tulis",
        "Buku Gambar"
    ]
)

combo_item.pack(pady=5)
combo_item.current(0)

# Jumlah
tk.Label(
    root,
    text="Jumlah"
).pack()

entry_jumlah = tk.Entry(
    root,
    width=30
)

entry_jumlah.pack(pady=5)

# Tombol tambah
tk.Button(
    root,
    text="Tambah Pesanan",
    command=tambah_pesanan,
    width=25
).pack(pady=10)

# Daftar pesanan
listbox = tk.Listbox(
    root,
    width=60,
    height=12
)

listbox.pack(pady=10)

# Tombol hitung
tk.Button(
    root,
    text="Hitung Total",
    command=hitung_total,
    width=25
).pack(pady=5)

# Tombol reset
tk.Button(
    root,
    text="Reset",
    command=reset,
    width=25
).pack(pady=5)

# Hasil
hasil = tk.Label(
    root,
    text="",
    justify="left",
    font=("Courier New", 11)
)

hasil.pack(pady=15)

root.mainloop()