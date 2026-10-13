def hitung_subtotal(harga, jumlah):
    return harga * jumlah


def hitung_total(daftar_belanja):
    total = 0

    for item in daftar_belanja:
        total += hitung_subtotal(
            item["harga"],
            item["jumlah"]
        )

    return total


def hitung_kembalian(uang_bayar, total_belanja):
    return uang_bayar - total_belanja


def main():
    print("=== KASIR SEDERHANA ===")
    daftar_belanja = []

    while True:
        nama = input(
            "Nama barang (ketik selesai untuk berhenti): "
        )

        if nama.lower() == "selesai":
            break

        try:
            harga = int(input("Harga barang: Rp"))
            jumlah = int(input("Jumlah barang: "))

            if harga < 0 or jumlah <= 0:
                print("Harga atau jumlah tidak valid!")
                continue

        except ValueError:
            print("Masukkan angka yang benar!")
            continue

        daftar_belanja.append({
            "nama": nama,
            "harga": harga,
            "jumlah": jumlah
        })

        print("Barang berhasil ditambahkan!")

    if len(daftar_belanja) == 0:
        print("Belum ada barang yang dibeli.")
        return

    total = hitung_total(daftar_belanja)

    print("\n=== STRUK BELANJA ===")

    for item in daftar_belanja:
        print(
            f'{item["nama"]}: '
            f'Rp{item["harga"]:,} x {item["jumlah"]}'
        )

    print(f"Total belanja: Rp{total:,}")

    try:
        bayar = int(input("Uang pembayaran: Rp"))
    except ValueError:
        print("Pembayaran harus berupa angka!")
        return

    kembalian = hitung_kembalian(bayar, total)

    if bayar < total:
        print(f"Uang pembayaran kurang Rp{total - bayar:,}")
    else:
        print(f"Kembalian: Rp{kembalian:,}")


if __name__ == "__main__":
    main()