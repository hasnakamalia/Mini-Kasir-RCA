import unittest
from kasir import hitung_subtotal, hitung_total, hitung_kembalian


class TestKasir(unittest.TestCase):

    # Pengujian defect 1: subtotal
    def test_subtotal(self):
        hasil = hitung_subtotal(10000, 3)
        self.assertEqual(hasil, 30000)

    # Pengujian defect 2: total belanja
    def test_total_belanja(self):
        daftar_belanja = [
            {"nama": "Buku", "harga": 10000, "jumlah": 2},
            {"nama": "Pensil", "harga": 2000, "jumlah": 3}
        ]
        hasil = hitung_total(daftar_belanja)
        self.assertEqual(hasil, 26000)

    # Pengujian defect 3: kembalian
    def test_kembalian(self):
        hasil = hitung_kembalian(20000, 30000)
        self.assertEqual(hasil, -10000)


if __name__ == "__main__":
    unittest.main()