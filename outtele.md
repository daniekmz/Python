# Telegram Auto Cleanup

Script Python untuk otomatis keluar dari semua channel dan grup Telegram, serta menghapus riwayat obrolan dengan semua kontak.

## ⚠️ Peringatan

**HATI-HATI!** Script ini akan:
- Keluar dari SEMUA channel dan grup yang Anda ikuti
- Menghapus SEMUA riwayat obrolan dengan kontak
- **Tindakan ini TIDAK DAPAT DIBATALKAN**

Pastikan Anda benar-benar yakin sebelum menjalankan script ini!

## Persyaratan

- Python 3.7 atau lebih baru
- Library Telethon
- API ID dan API Hash dari Telegram

## Instalasi

1. **Clone atau download script ini**
   ```bash
   git clone <repository-url>
   cd telegram-cleanup
   ```

2. **Install library yang diperlukan**
   ```bash
   pip install telethon
   ```

3. **Dapatkan API ID dan API Hash**
   - Kunjungi [my.telegram.org](https://my.telegram.org)
   - Login dengan akun Telegram Anda
   - Buat aplikasi baru di bagian "API Development Tools"
   - Catat API ID dan API Hash yang diberikan

## Konfigurasi

1. **Edit file `outtele.py`**
   ```python
   # Ganti dengan data Anda
   api_id = 'your_api_id_here'        # Ganti dengan API ID Anda
   api_hash = 'your_api_hash_here'    # Ganti dengan API Hash Anda
   phone_number = '+62xxxxxxxxxxxx'   # Ganti dengan nomor telepon Anda
   ```

2. **Format nomor telepon**
   - Gunakan format internasional dengan kode negara
   - Contoh: `+628123456789` untuk nomor Indonesia

## Cara Penggunaan

1. **Jalankan script**
   ```bash
   python outtele.py
   ```

2. **Proses autentikasi**
   - Script akan meminta kode verifikasi yang dikirim ke Telegram Anda
   - Masukkan kode verifikasi tersebut
   - Jika diminta, masukkan juga password two-factor authentication (jika aktif)

3. **Script akan otomatis**
   - Keluar dari semua channel
   - Keluar dari semua grup
   - Menghapus riwayat obrolan dengan semua kontak

## Fitur Script

- **Keluar dari Channel**: Otomatis leave dari semua channel yang diikuti
- **Keluar dari Grup**: Otomatis leave dari semua grup yang diikuti  
- **Hapus Riwayat Chat**: Menghapus semua riwayat obrolan (channel, grup, dan personal chat)
- **Error Handling**: Menangani error dan melanjutkan proses meski ada kesalahan
- **Logging**: Menampilkan status setiap tindakan yang dilakukan

## File yang Dibuat

Script akan membuat file `session_name.session` yang berisi informasi sesi login. File ini akan otomatis dibuat saat pertama kali login.

## Troubleshooting

### Error "Phone number unoccupied"
- Pastikan nomor telepon sudah terdaftar di Telegram
- Periksa format nomor telepon (gunakan kode negara)

### Error "API ID/Hash invalid"
- Periksa kembali API ID dan API Hash
- Pastikan tidak ada spasi atau karakter tambahan

### Error koneksi
- Periksa koneksi internet
- Script memiliki retry otomatis untuk koneksi yang tidak stabil

### Script berhenti di tengah jalan
- Script akan melanjutkan dari dialog berikutnya
- Restart script jika diperlukan

## Keamanan

- **Jangan bagikan** API ID dan API Hash kepada orang lain
- **Jangan commit** file konfigurasi dengan data asli ke repository publik
- File session berisi informasi login, jaga kerahasiaannya

## Batasan

- Script akan memproses semua dialog secara berurutan
- Beberapa channel/grup mungkin memiliki pembatasan untuk leave
- Riwayat yang sudah dihapus tidak dapat dikembalikan

## Lisensi

Script ini disediakan "sebagaimana adanya" tanpa jaminan apapun. Gunakan dengan risiko Anda sendiri.

## Kontribusi

Jika Anda menemukan bug atau ingin menambahkan fitur, silakan buat issue atau pull request.

---

**Catatan**: Pastikan Anda memahami konsekuensi dari menjalankan script ini sebelum menggunakannya!
