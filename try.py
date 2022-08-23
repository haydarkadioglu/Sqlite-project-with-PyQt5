import sqlite

print("Kaydetmek istediğniz kitabı girin...")
nam = input("ismi: ")
writer = input("yazarı: ")
no = int(input("numarası: "))

sqlite.addbook(nam, writer, no)
print("başarıyla eklendi")