import tkinter as tk
from tkinter import messagebox

# =========================
# FUNGSI-FUNGSI TUGAS
# =========================

def HitungTotalAlatTulis(kode_alat, jumlah):
    harga_alat = {
        "pensil": 2000,
        "pulpen": 3000,
        "penghapus": 1500
    }

    return harga_alat.get(kode_alat.lower(), 0) * jumlah


def HitungTotalBuku(kode_buku, jumlah):
    harga_buku = {
        "buku_tulis": 5000,
        "buku_gambar": 6000
    }

    return harga_buku.get(kode_buku.lower(), 0) * jumlah


def HitungDiskon(total):
    if total >= 75000:
        return total * 0.15
    return 0


def HitungPajak(total_setelah_diskon):
    return total_setelah_diskon * 0.03


def TampilkanDetail(item, jumlah, harga, total):
    return f"{item.title()} x {jumlah} = Rp {total:,.0f}"


# =========================
# DATA PESANAN
# =========================

pesanan = []


# =========================
# EVENT GUI
# =========================

def tambah_pesanan():
    item = entry_item.get().lower().strip()

    try:
        jumlah = int(entry_jumlah.get())
    except ValueError:
        messagebox.showerror("Error", "Jumlah harus berupa angka!")
        return

    daftar_harga = {
        "pensil": 2000,
        "pulpen": 3000,
        "penghapus": 1500,
        "buku_tulis": 5000,
        "buku_gambar": 6000
    }

    if item not in daftar_harga:
        messagebox.showerror("Error", "Item tidak ditemukan!")
        return

    pesanan.append((item, jumlah))

    subtotal = daftar_harga[item] * jumlah

    listbox.insert(
        tk.END,
        TampilkanDetail(item, jumlah, daftar_harga[item], subtotal)
    )

    entry_item.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)


def hitung_total():
    total = 0

    harga_alat = {
        "pensil",
        "pulpen",
        "penghapus"
    }

    for item, jumlah in pesanan:

        if item in harga_alat:
            subtotal = HitungTotalAlatTulis(item, jumlah)
        else:
            subtotal = HitungTotalBuku(item, jumlah)

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
        f"---------------------------\n"
        f"TOTAL BAYAR  : Rp {total_bayar:,.0f}"
    )


def reset():
    pesanan.clear()
    listbox.delete(0, tk.END)
    hasil.config(text="")


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Toko Buku Sekolah")
root.geometry("500x500")

judul = tk.Label(
    root,
    text="=== TOKO BUKU SEKOLAH ===",
    font=("Arial", 14, "bold")
)
judul.pack(pady=10)

info = tk.Label(
    root,
    text=(
        "Pensil = 2000\n"
        "Pulpen = 3000\n"
        "Penghapus = 1500\n"
        "Buku_Tulis = 5000\n"
        "Buku_Gambar = 6000"
    )
)
info.pack()

tk.Label(root, text="Nama Item").pack()

entry_item = tk.Entry(root)
entry_item.pack()

tk.Label(root, text="Jumlah").pack()

entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

tk.Button(
    root,
    text="Tambah Pesanan",
    command=tambah_pesanan
).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

tk.Button(
    root,
    text="Hitung Total",
    command=hitung_total
).pack(pady=5)

tk.Button(
    root,
    text="Reset",
    command=reset
).pack(pady=5)

hasil = tk.Label(
    root,
    text="",
    justify="left",
    font=("Courier New", 10)
)
hasil.pack(pady=10)

root.mainloop()