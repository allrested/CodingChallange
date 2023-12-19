**2. Highest Palindrome (Score: 30)**
Kamu memiliki string yang merepresentasikan angka '3943' lalu diberikan sebuah variabel k untuk melakukan replacement karakter sejumlah k pada string agar menjadi **bentuk palindrom**. 

**Sampel**:
**Input**:
string: '3943' 
k: 1 
palindrom:
1. '3943'  => '3993'
2. '3943' => '3443'
**Output**: '3993'
**Penjelasan**: Dari bentuk palindrom yang diperoleh maka highest palindrome-nya adalah **'3993'** dikarenakan 3993 > 3443.

**Aturan**:
1. Jika dari sebuah string **tidak ditemukan** bentuk palindrome-nya meski sudah melakukan replacement dan tidak merepresentasikan sebuah angka maka akan mengeluarkan **output -1**.
2. Tidak boleh menggunakan fungsi bawaan/tools untuk pencarian/filter/sort.
3. Tidak boleh menggunakan looping.
4. Hanya diperkenankan menggunakan rekursif.

**Soal**:
Buat fungsi yang digunakan untuk menyelesaikan permasalahan **Highest Palindrome**!