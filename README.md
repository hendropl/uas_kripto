# uas_kripto
# Advanced One-Time Pad Encryption

## 📋 Deskripsi Proyek

Aplikasi GUI berbasis Python yang mengimplementasikan algoritma kriptografi **One-Time Pad (OTP)** untuk keperluan pembelajaran dan eksperimen keamanan informasi. Aplikasi ini mendemonstrasikan prinsip kerja OTP, validasi penggunaan kunci, dan simulasi serangan dengan kunci palsu.
## 📖 Latar Belakang

Di era digital yang penuh dengan ancaman keamanan informasi, kebutuhan akan algoritma enkripsi yang mampu memberikan *keamanan sempurna (perfect secrecy)* menjadi semakin penting. Salah satu algoritma yang memenuhi kriteria tersebut adalah *One-Time Pad (OTP), yang secara teori tidak dapat dipecahkan apabila syarat penggunaannya dipatuhi dengan ketat: kunci harus benar-benar acak, panjang kunci harus sama dengan panjang pesan, dan **kunci hanya boleh digunakan sekali*.

Namun, implementasi OTP di dunia nyata jarang digunakan karena distribusi dan manajemen kunci yang rumit. Oleh karena itu, proyek ini hadir untuk mensimulasikan bagaimana OTP bekerja dalam sebuah *aplikasi GUI berbasis Python*, yang dilengkapi dengan sistem validasi penggunaan kunci, serta simulasi serangan dengan kunci palsu. Aplikasi ini bertujuan untuk menjadi media pembelajaran interaktif yang membantu mahasiswa dan praktisi memahami bagaimana algoritma OTP bekerja, serta risiko yang terjadi jika prinsip-prinsip dasarnya dilanggar.

---

## ❓ Rumusan Masalah

1. Bagaimana prinsip kerja algoritma One-Time Pad (OTP) dapat diimplementasikan dalam sebuah aplikasi GUI berbasis Python?
2. Bagaimana sistem aplikasi dapat mencegah penggunaan ulang kunci dan menunjukkan dampaknya jika dilanggar?
3. Bagaimana simulasi serangan dengan kunci palsu dapat digunakan untuk mengilustrasikan kelemahan OTP jika prinsip dasar tidak diterapkan dengan benar?

---

## 🎯 Tujuan Proyek

* Mengembangkan aplikasi GUI berbasis Python yang mampu melakukan enkripsi dan dekripsi menggunakan algoritma One-Time Pad.
* Mengimplementasikan sistem deteksi penggunaan ulang kunci untuk menjaga prinsip perfect secrecy OTP.
* Menyediakan fitur simulasi serangan dengan kunci palsu sebagai pembelajaran risiko keamanan.
* Memberikan media pembelajaran interaktif untuk memahami konsep kriptografi dasar, khususnya OTP.

## 🎯 Tujuan

1. **Implementasi OTP**: Membangun aplikasi GUI yang dapat melakukan enkripsi dan dekripsi menggunakan algoritma One-Time Pad
2. **Validasi Kunci**: Mengimplementasikan sistem deteksi penggunaan ulang kunci untuk menjaga prinsip OTP
3. **Simulasi Serangan**: Menyediakan fitur simulasi serangan dengan kunci palsu untuk pembelajaran keamanan
4. **Media Pembelajaran**: Memberikan alat bantu interaktif untuk memahami konsep kriptografi dasar

## 🔧 Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python 3
- **GUI Framework**: Tkinter
- **Kriptografi**: XOR Operation, SHA-256 Hashing
- **Modul**: `binascii`, `hashlib`, `tkinter.messagebox`
- **Platform**: Windows/Linux/MacOS

## ⚡ Fitur Utama

### 1. **Mode Enkripsi**
- Input plaintext dan kunci dengan panjang yang sama
- Operasi XOR antara plaintext dan kunci
- Output ciphertext dalam format heksadesimal
- Validasi panjang input otomatis

### 2. **Mode Dekripsi**
- Input ciphertext (hex) dan kunci yang sesuai
- Konversi hex ke plaintext asli
- Validasi format dan panjang input

### 3. **Simulasi Serangan**
- Percobaan dekripsi dengan kunci palsu (fake key)
- Menunjukkan hasil plaintext yang tidak valid
- Demonstrasi keamanan OTP

### 4. **Validasi Kunci**
- Sistem hash SHA-256 untuk tracking kunci
- Pencegahan penggunaan ulang kunci (reuse prevention)
- Riwayat kunci yang pernah digunakan


## 📖 Cara Penggunaan

### 1. **Enkripsi Pesan**
1. Masukkan **Plaintext** (contoh: "HELLO")
2. Masukkan **Key** dengan panjang sama (contoh: "XMCKL")
3. Klik tombol **"Enkripsi"**
4. Ciphertext akan muncul dalam format hex

### 2. **Dekripsi Pesan**
1. Pastikan **Ciphertext (Hex)** sudah terisi
2. Masukkan **Key** yang sama dengan saat enkripsi
3. Klik tombol **"Dekripsi (Key Asli)"**
4. Plaintext asli akan muncul

### 3. **Simulasi Serangan**
1. Masukkan **Fake Key** (kunci palsu)
2. Klik **"Coba Dekripsi Pakai Fake Key"**
3. Lihat hasil dekripsi yang salah/acak

### 4. **Reset**
- Klik tombol **"Reset"** untuk membersihkan semua input

## 🧪 Contoh Pengujian

### Test Case 1: Enkripsi & Dekripsi Valid
```
Input:
- Plaintext: "HELLO"
- Key: "XMCKL"

Output:
- Ciphertext: "10080f0703" (contoh)
- Decrypted: "HELLO" ✅
```

### Test Case 2: Deteksi Reuse Key
```
Input:
- Key yang sudah pernah digunakan

Output:
- Error: "Kunci ini sudah pernah digunakan. OTP hanya boleh dipakai sekali." ⚠️
```

### Test Case 3: Simulasi Serangan
```
Input:
- Ciphertext: "10080f0703"
- Fake Key: "ABCDE"

Output:
- Hasil: "A_JUW" (karakter acak) ❌
```

## 🔒 Prinsip Keamanan OTP

### Syarat Keamanan Sempurna:
1. **Kunci Acak**: Kunci harus benar-benar random
2. **Panjang Sama**: Kunci harus sama panjang dengan plaintext
3. **Sekali Pakai**: Kunci tidak boleh digunakan lebih dari sekali

### Kelebihan:
- ✅ Keamanan teoretis sempurna (perfect secrecy)
- ✅ Tidak dapat dipecahkan secara kriptografis
- ✅ Operasi XOR yang sederhana dan cepat

## 📊 Hasil Pengujian

| No | Skenario | Status | Keterangan |
|----|----------|---------|------------|
| 1 | Enkripsi/Dekripsi Valid | ✅ Berhasil | Plaintext berhasil di-recover |
| 2 | Deteksi Reuse Key | ✅ Berhasil | Sistem menolak kunci bekas |
| 3 | Simulasi Serangan | ✅ Berhasil | Fake key menghasilkan output acak |

## 🎓 Nilai Edukatif

Aplikasi ini memberikan pemahaman tentang:
- **Algoritma Kriptografi Dasar**: Implementasi OTP yang mudah dipahami
- **Keamanan Informasi**: Pentingnya manajemen kunci yang benar
- **Analisis Serangan**: Dampak penggunaan kunci yang salah
- **Trade-off Keamanan**: Keseimbangan antara keamanan dan praktikalitas

## Kesimpulan 
Ciphertext yang dienkripsi menggunakan algoritma One-Time Pad (OTP) tidak dapat
didekripsi secara pasti tanpa mengetahui kunci yang digunakan. Hal ini disebabkan oleh sifat
dasar OTP yang melakukan operasi XOR antara plaintext dan kunci yang benar-benar acak dan
unik untuk setiap pesan. Tanpa mengetahui kunci, ciphertext tersebut dapat dikaitkan dengan
sekitar 281 triliun kemungkinan plaintext berbeda, sehingga tidak ada cara untuk menentukan
mana yang benar. Oleh karena itu, OTP memberikan keamanan yang sempurna (perfect
secrecy) selama kunci digunakan hanya sekali, bersifat acak, dan disimpan secara rahasia. Ini
membuktikan bahwa OTP tidak dapat dipecahkan secara kriptografis melalui analisis ciphertext
saja, sehingga sangat kuat namun sulit digunakan secara praktis karena tantangan dalam
distribusi dan manajemen kunci..
## 👥 Tim Pengembang

**Kelompok 5 - Program Studi Informatika**
- M. Zuhri Al Kauri (G1A023029)
- I Nyoman Dimas Kresna Adryan (G1A023077)
- Mohamad Irvan Ramadhansyah (G1A023089)
- Hendro Paulus L (G1A023091)

**Dosen Pengampu**: Ir. Kurnia Anggraini, S.T., M.T., Ph.D

**Universitas Bengkulu - Fakultas Teknik**
**Semester 4 - Tahun 2025**

## 📚 Referensi

1. Paar, C., & Pelzl, J. (2010). *Understanding Cryptography: A Textbook for Students and Practitioners*
2. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice*
3. Istiqamah, N., & Subiyanto, S. (2016). Sistem keamanan e-voting menggunakan fungsi hash dan algoritma One Time Pad

## 📝 Lisensi

Proyek ini dikembangkan untuk keperluan akademik dan pembelajaran di Universitas Bengkulu.

---

**⚠️ Catatan Penting**: 
Aplikasi ini dirancang untuk tujuan pembelajaran dan eksperimen. Tidak disarankan untuk penggunaan produksi atau sistem yang membutuhkan keamanan tinggi karena keterbatasan dalam implementasi distribusi kunci dan penyimpanan yang aman.
