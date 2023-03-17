#nama = input("Siapa Nama Mu:")
#umur = input("Brapa Umurmu :")
#print ("Hello",nama,"umur kamu adalah", umur,"tahun")

#angka1 = int(input("Maukan Angka Pertama="))
#angka2 = int(input("masukan angka kedua="))

#hasil= angka1+angka2 

#print("Hail Penjumlahan dari",angka1,"+",angka2,"adalah",hasil)

#print("aku ber hasil belajar")

host="localhost"
user="root"
passwd=""
import mysql.connector as mysql

db=mysql.connect(
    host=host,
    user=user,
    passwd=passwd
)
#print(db)

cursor=db.cursor()

#membuat data base 
#cursor.execute("CREATE DATABASE hendra")

#menghapus data base
#cursor.execute("DROP DATABASE test")

#menampilkan data base 
#cursor.execute("SHOW DATABASES")
#data = cursor.fetchall()
#print(data)

cursor = db.cursor()
db.database="hendra"

#membuat tabel pada database 
#cursor.execute('''
#          create table bio(
#          ID INT NOT NULL AUTO_INCREMENT,
#            nama VARCHAR(10) NOT NULL,
#           alamat TEXT NOT NULL,
#           tanggal DATE, 
#           PRIMARY KEY (ID)
#         );
#        ''')

#menghapus tabel pada databases
#cursor.execute("DROP TABLE bio")

#melihat isi tabel 
#cursor.execute("SHOW TABLE bio")
#print(cursor.fetchall())

#menampilkan tabel pada database 
#cursor.execute("SHOW TABLES")
#data= cursor.fetchall()
#print(data)

#MENAMBAH ISI DARI TABEL 
#cursor.execute("INSERT INTO bio (nama,alamat) VALUES('GUNAWAN','karawang')")

#cursor.execute("ALTER TABLE bio DROP tanggal")
#cursor.execute("INSERT INTO bio (nama,alamat) VALUES ('GUGUN', 'KUNINGAN')")
#cursor.execute("UPDATE bio SET nama='gunawan' WHERE id='13'")
#cursor.execute("DELETE FROM bio WHERE nama='GUGUN'")
db.commit()

#MENAMILKAN ISI DARI TABEL 
cursor.execute("SELECT  * FROM bio WHERE nama='Hendra'")
data = cursor.fetchall()
for row in data:
    print(row)

print("Aku BERHASIL")
print("Dan AKU BANGGA")
print("AKU AKU")
print("saiki wes sadar")
print("saiki wes sadar")
print("telalu mayo mergo")

print("mayo")