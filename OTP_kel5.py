import tkinter as tk
from tkinter import messagebox
import binascii
import hashlib

# Set untuk menyimpan hash dari kunci yang pernah digunakan
used_keys = set()

def hash_key(key):
    """Hash kunci agar tidak disimpan mentah."""
    return hashlib.sha256(key.encode()).hexdigest()

def xor_encrypt_decrypt(text, key):
    """XOR antara dua string (plaintext dan key)"""
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))

def encrypt():
    plaintext = entry_plain.get()
    key = entry_key.get()

    if len(plaintext) != len(key):
        messagebox.showerror("Error", "Panjang plaintext dan key harus sama.")
        return

    key_hash = hash_key(key)
    if key_hash in used_keys:
        messagebox.showerror("Error", "Kunci ini sudah pernah digunakan. OTP hanya boleh dipakai sekali.")
        return

    ciphertext = xor_encrypt_decrypt(plaintext, key)
    ciphertext_hex = binascii.hexlify(ciphertext.encode()).decode()
    entry_cipher.delete(0, tk.END)
    entry_cipher.insert(0, ciphertext_hex)

    used_keys.add(key_hash)
    list_used_keys.insert(tk.END, f"{key} (hash: {key_hash[:10]}...)")

def decrypt():
    cipher_hex = entry_cipher.get()
    key = entry_key.get()

    try:
        cipher_bytes = binascii.unhexlify(cipher_hex)
        cipher = cipher_bytes.decode()
    except:
        messagebox.showerror("Error", "Format ciphertext tidak valid.")
        return

    if len(cipher) != len(key):
        messagebox.showerror("Error", "Panjang ciphertext dan key harus sama.")
        return

    plaintext = xor_encrypt_decrypt(cipher, key)
    entry_decrypt.delete(0, tk.END)
    entry_decrypt.insert(0, plaintext)

def reset():
    entry_plain.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_cipher.delete(0, tk.END)
    entry_decrypt.delete(0, tk.END)
    entry_fake_key.delete(0, tk.END)
    entry_fake_decrypt.delete(0, tk.END)

def attack_attempt():
    cipher_hex = entry_cipher.get()
    fake_key = entry_fake_key.get()

    try:
        cipher_bytes = binascii.unhexlify(cipher_hex)
        cipher = cipher_bytes.decode()
    except:
        messagebox.showerror("Error", "Format ciphertext tidak valid.")
        return

    if len(cipher) != len(fake_key):
        messagebox.showerror("Error", "Panjang fake key harus sama dengan ciphertext.")
        return

    wrong_plaintext = xor_encrypt_decrypt(cipher, fake_key)
    entry_fake_decrypt.delete(0, tk.END)
    entry_fake_decrypt.insert(0, wrong_plaintext)

# GUI setup
root = tk.Tk()
root.title("Advanced One-Time Pad Encryption")

# Input fields
tk.Label(root, text="Plaintext").grid(row=0, column=0)
entry_plain = tk.Entry(root, width=40)
entry_plain.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Key").grid(row=1, column=0)
entry_key = tk.Entry(root, width=40)
entry_key.grid(row=1, column=1, padx=10, pady=5)

btn_encrypt = tk.Button(root, text="Enkripsi", command=encrypt)
btn_encrypt.grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(root, text="Ciphertext (Hex)").grid(row=3, column=0)
entry_cipher = tk.Entry(root, width=40)
entry_cipher.grid(row=3, column=1, padx=10, pady=5)

btn_decrypt = tk.Button(root, text="Dekripsi (Key Asli)", command=decrypt)
btn_decrypt.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Plaintext Terdekripsi").grid(row=5, column=0)
entry_decrypt = tk.Entry(root, width=40)
entry_decrypt.grid(row=5, column=1, padx=10, pady=5)

# Attack Simulation
tk.Label(root, text="Fake Key (untuk serangan)").grid(row=6, column=0)
entry_fake_key = tk.Entry(root, width=40)
entry_fake_key.grid(row=6, column=1, padx=10, pady=5)

btn_attack = tk.Button(root, text="Coba Dekripsi Pakai Fake Key", command=attack_attempt)
btn_attack.grid(row=7, column=0, columnspan=2, pady=5)

tk.Label(root, text="Hasil Dekripsi Palsu").grid(row=8, column=0)
entry_fake_decrypt = tk.Entry(root, width=40)
entry_fake_decrypt.grid(row=8, column=1, padx=10, pady=5)

# Key history
tk.Label(root, text="Riwayat Kunci yang Pernah Digunakan").grid(row=9, column=0, pady=10)
list_used_keys = tk.Listbox(root, width=60)
list_used_keys.grid(row=9, column=1, padx=10)

# Reset Button
tk.Button(root, text="Reset", command=reset).grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()