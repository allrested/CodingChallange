**3. Balanced Bracket (Score: 50)**
**Sampe 1**:
**Input**: { [ ( ) ] }
**Output**: YES
**Penjelasan**: Setiap braket seimbang, antara braket buka dan braket tutup.
opening : { }
opening : [ ]
opening : ( }

**Sampel 2**:
**Input**: { [ ( ] ) }
**Output**: NO
**Penjelasan**: String { [ ( ] ) } tidak seimbang untuk karakter yang diapit oleh { dan } yaitu [ ( ] ).

**Sampel 3**:
**Input**: { ( ( [ ] ) [ ] ) [ ] }
**Output**: YES
**Penjelasan**: Setiap braket seimbang, antara braket buka dan braket tutup, meskipun struktur braket tidak beraturan.

**Aturan**:
1. Tanda braket yang diperbolehkan sebagai berikut: ( , ) , { , } , atau [ , ]. 
2. Bracket bisa dipisahkan **dengan** atau **tanpa whitespace**.
3. Periksa tanda kurung yang memiliki kecocokan antara braket buka dan braket tutup dengan mengembalikan nilai string **YES** atau **NO**.

**Soal**:
1. Buat fungsi untuk menemukan **Balanced Bracket** dengan **kompleksitas paling rendah**!
2. Berapa **ukuran kompleksitas** kodinganmu? Jelaskan **detail kompleksitas** jawaban No.3, cantumkan di README Repo! 