# GITS HITOPIA

Detail kompleksitas pada function "isBalanced" pada soal nomor 3:
Fungsi "isBalanced" menggunakan stack untuk memeriksa kecocokan antara tanda kurung buka dan tutup. Pada setiap iterasi, jika karakter tersebut merupakan tanda buka, maka karakter akan ditambahkan ke dalam stack. Jika karakter merupakan tanda tutup, maka akan dilakukan pemeriksaan kecocokan dengan tanda buka terakhir yang ada di stack. Jika tidak cocok atau stack kosong, maka output adalah "NO". Setelah iterasi selesai, jika stack tidak kosong, maka output adalah "NO". Jika stack kosong, maka output adalah "YES".
- Kompleksitas waktu: O(n) di mana n adalah panjang string input, karena setiap karakter diproses satu per satu.
- Kompleksitas ruang: O(n) di mana n adalah panjang string input, karena stack dapat mencapai panjang n