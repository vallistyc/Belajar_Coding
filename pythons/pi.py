# FLOWCHART MERMAID
# flowchart TD
#     A([Mulai]) --> B[Set pi = 3, iterasi = 0, tanda = 1]
#     B --> C[Hitung suku Nilakantha]
#     C --> D[Update pi sekarang]
#     D --> E{Iterasi kelipatan 2?}
#     E -- Ya --> F[Tampilkan estimasi pi]
#     E -- Tidak --> G[Hitung selisih pi sekarang dan sebelumnya]
#     F --> G
#     G --> H{Selisih < toleransi dan iterasi >= 10 dan suku terakhir < toleransi?}
#     H -- Tidak --> C
#     H -- Ya --> I[Tampilkan hasil konvergen]
#     I --> J([Selesai])


TOLERANSI = 0.0000001
MIN_ITERASI = 10


def hitungSukuNilakantha(iterasi):
    penyebut = 2 * iterasi
    suku = 4 / (penyebut * (penyebut + 1) * (penyebut + 2))

    if iterasi % 2 == 0:
        suku = -suku

    return suku


def sudahKonvergen(selisih, iterasi, sukuTerakhir):
    return (
        selisih < TOLERANSI
        and iterasi >= MIN_ITERASI
        and abs(sukuTerakhir) < TOLERANSI
    )


def hitungPiNilakantha():
    pi = 3
    piSebelumnya = pi
    iterasi = 0

    while True:
        iterasi += 1
        sukuTerakhir = hitungSukuNilakantha(iterasi)
        pi += sukuTerakhir

        if iterasi % 2 == 0:
            print(f"Iterasi {iterasi}: pi ~= {pi:.6f}")

        selisih = abs(pi - piSebelumnya)

        if sudahKonvergen(selisih, iterasi, sukuTerakhir):
            print(f"Konvergen setelah {iterasi} iterasi: pi ~= {pi:.6f}")
            break

        piSebelumnya = pi


def main():
    hitungPiNilakantha()


main()
