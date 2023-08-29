from django.test import TestCase
from .models import BarangWishlist
from django.urls import reverse

class BarangWishlistModelTest(TestCase):

    def setUp(self):
        self.barang = BarangWishlist.objects.create(
            nama_barang='Test Barang',
            harga_barang=100,
            deskripsi='Test Deskripsi'
        )

    def test_nama_barang_max_length(self):
        max_length = self.barang._meta.get_field('nama_barang').max_length
        self.assertEqual(max_length, 50)

    def test_harga_barang_positive(self):
        self.assertGreaterEqual(self.barang.harga_barang, 0)

    def test_deskripsi_max_length(self):
        max_length = self.barang._meta.get_field('deskripsi').max_length
        self.assertIsNone(max_length)  # TextField doesn't have a max_length

    # Add more tests as needed
