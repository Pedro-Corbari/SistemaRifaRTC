import sqlite3

banco = sqlite3.connect("numeros", check_same_thread=False)

cursor = banco.cursor()


# cursor.execute(f"UPDATE numeros SET comprador=NULL, telefone=NULL, vendedor=NULL")
# banco.commit()
# cursor.execute(f"DELETE FROM numeros")
# banco.commit()



# for i in range(200):
#     print(i+1)
#     cursor.execute(f"INSERT INTO numeros VALUES ({i+1}, NULL, NULL, NULL)")
#     banco.commit()


abc = cursor.execute("SELECT * FROM numeros")

for i in abc:
    print(i)