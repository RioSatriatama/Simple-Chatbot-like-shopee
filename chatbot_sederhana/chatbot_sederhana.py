# chatbot_sederhana.py

print("🤖: Halo! Saya adalah asisten layanan pelanggan Shopee. Bagaimana saya bisa membantu Anda hari ini?")

# Daftar pertanyaan dan jawaban (dictionary)
jawaban_pertanyaan = {
    "halo": "Halo! 😊 Ada yang bisa saya bantu?",
    "apa kabar": "Saya baik, terima kasih! Bagaimana dengan Anda?",
    "kabar saya baik": "wah senang sekali mendengar kabar anda baik, Ada yang bisa saya bantu?",
    "bantuan": "Silakan tanya tentang: pesanan, pengembalian, pengiriman, atau pembayaran.",
    "pesanan": "Untuk melihat status pesanan, silakan masukkan nomor pesanan Anda.",
    "pengiriman": "Pengiriman biasanya memakan waktu 1-5 hari kerja tergantung wilayah. Cek status pengiriman di aplikasi Shopee.",
    "pengembalian": "Anda bisa mengajukan pengembalian dalam 7 hari setelah barang diterima. Buka aplikasi > Pesanan > Ajukan pengembalian.",
    "pembayaran": "Kami menerima pembayaran via Dana, OVO, ShopeePay, bank transfer, dan kartu kredit.",
    "terima kasih": "Sama-sama! 😊 Jika butuh bantuan lagi, saya di sini!",
    "sampai jumpa": "Sampai jumpa! Semoga harimu menyenangkan! 🌟"
}

# Loop utama chatbot
while True:
    pertanyaan = input("Anda: ").lower().strip()
    
    if pertanyaan in ["keluar", "exit", "quit", "x"]:
        print("🤖: Terima kasih sudah berbicara dengan saya. Sampai jumpa!")
        break

    # Cari jawaban berdasarkan input user
    found = False
    for kata_kunci, jawaban in jawaban_pertanyaan.items():
        if kata_kunci in pertanyaan:
            print(f"🤖: {jawaban}")
            found = True
            break

    if not found:
        print("🤖: Maaf, saya belum paham pertanyaan Anda. Silakan tanya tentang pesanan, pengiriman, pengembalian, atau pembayaran.")

