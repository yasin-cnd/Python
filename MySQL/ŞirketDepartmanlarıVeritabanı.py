from re import I
from tokenize import cookie_re
import mysql.connector
from datetime import datetime
from sqlalchemy import values

#MySQL de açılan veritabanı ve tabloların içeriği
#create database şirketveritabanı;
#create table insankaynakları/üretim/araştırma_geliştirme/muhasebevefinans/satışvepazarlama/yönetim/bilişim (
#   id int(5) unsigned primary key not null auto_increment,
#   isim varchar(50),
#   soyisim varchar(50),
#   görev varchar(90),
#   age int  ); 

connection=mysql.connector.connect(host="localhost",user="root",password="",database="şirketveritabanı")
cursor = connection.cursor()
devam = 'E'
departmanseçiniz=input("işlem yapmak istediğiniz departmanı seçiniz insankaynakları(1)/üretim(2)/araştırma_geliştirme(3)/muhasebevefinans(4)/satışvepazarlama(5)/yönetim(6)/bilişim(7): ")
def ekle():
    while True:
        id=input("id girniz")
        isim =input("İsim girin :")
        soyisim =input("Soyisim girin :")
        görev =input("görev/pozisyon girin :")
        yaş =input("yaşı giriniz :")
        cinsiyet =input("cinsiyet girin  'Erkek' ya da 'Kadın':")
        if departmanseçiniz=="üretim" or departmanseçiniz=="2":
            sql = "INSERT INTO  üretim values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="insankaynakları" or departmanseçiniz=="1":   
            sql = "INSERT INTO  insankaynakları values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="araştırma_geliştirme" or departmanseçiniz=="3":  
            sql = "INSERT INTO  araştırma_geliştirme values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="bilişim" or departmanseçiniz=="7":       
            sql = "INSERT INTO  bilişim values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="muhasebevefinans" or departmanseçiniz=="4":  
            sql = "INSERT INTO muhasebevefinans values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="satışvepazarlama" or departmanseçiniz=="5":    
            sql = "INSERT INTO  satışvepazarlama values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)

        elif departmanseçiniz=="yönetim" or departmanseçiniz=="6":   
            sql = "INSERT INTO  yönetim values('{}','{}','{}','{}','{}',{})".format(id,isim,soyisim,görev,yaş,cinsiyet)
        while True:
            cursor.execute(sql)
            connection.commit()   
            print("[+] Veri Eklendi")
            break
        break

def güncelle(id,isim,soyisim):
    while True:
        connection=mysql.connector.connect(host="localhost", user="root",password="",database="şirketveritabanı")
        cursor=connection.cursor()
        if departmanseçiniz=="bilişim" or departmanseçiniz=="7":
            sql="update bilişim set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="insankaynakları" or departmanseçiniz=="1":
            sql="update insankaynakları set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="araştırma_geliştirme" or departmanseçiniz=="3":
            sql="update araştırma_geliştirme set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="üretim" or departmanseçiniz=="2":
            sql="update üretim set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="muhasebevefinans" or departmanseçiniz=="4":
            sql="update muhasebevefinans set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="satışvepazarlama" or departmanseçiniz=="5":
            sql="update satışvepazarlama set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)
        elif departmanseçiniz=="yönetim" or departmanseçiniz=="6":
            sql="update yönetim set isim=%s,soyisim=%s where id=%s "
            values=(isim,soyisim,id)
            cursor.execute(sql,values)

        while True:
                try:
                    connection.commit()
                    print(f"{cursor.rowcount} tane kayıt güncellendi .")   
                except mysql.connection.Error as err:
                    print("hata:",err)  
                finally:
                    connection.close()
                    print("dtabase bağlantısı kapandı.")
                break
        break

def ara():
    while True:
        isim = input( "aramak istediğiniz kişinin ismini tek tırnak içinde giriniz :")
        if departmanseçiniz=="bilişim" or departmanseçiniz=="7":
            cursor.execute("select * from bilişim where isim ="+isim)
            data = cursor.fetchone()
        elif departmanseçiniz=="insankaynakları" or departmanseçiniz=="1":
            cursor.execute("select * from insankaynakları where isim ="+isim)
            data = cursor.fetchone()
        elif departmanseçiniz=="araştırma_geliştirme" or departmanseçiniz=="3":
            cursor.execute("select * from araştırma_geliştirme where isim ="+isim)
            data = cursor.fetchone()
        elif  departmanseçiniz=="üretim" or departmanseçiniz=="2":
            cursor.execute("select * from üretim where isim ="+isim)
            data = cursor.fetchone()
        elif  departmanseçiniz=="yönetim" or departmanseçiniz=="6":
            cursor.execute("select * from yönetim where isim ="+isim)
            data = cursor.fetchone()       
        elif departmanseçiniz=="satışvepazarlama" or departmanseçiniz=="5":
            cursor.execute("select * from satışvepazarlama where isim ="+isim)
            data = cursor.fetchone()
        elif departmanseçiniz=="muhasebevefinans" or departmanseçiniz=="4":
            cursor.execute("select * from muhasebevefinans where isim ="+isim)
            data = cursor.fetchone()

        while True:
            if data != None :   
                print("id :",data[0])
                print("isim :",data[1])
                print("Soyisim :",data[2])
                print("görev/pozisyon :",data[3])
                print("yaş : ",data[4])
                print("cinsiyet : ",data[5])
            break
        break

def listele():
   while True:
        if departmanseçiniz=="bilişim" or departmanseçiniz=="7":
            cursor.execute("select * from bilişim") 
            data = cursor.fetchall()
        elif departmanseçiniz=="insankaynakları" or departmanseçiniz=="1":
            cursor.execute("select * from insankaynakları") 
            data = cursor.fetchall()
        elif departmanseçiniz=="araştırma_geliştirme" or departmanseçiniz=="3":
            cursor.execute("select * from araştırma_geliştirme") 
            data = cursor.fetchall()
        elif departmanseçiniz=="üretim" or departmanseçiniz=="2":
            cursor.execute("select * from üretim") 
            data = cursor.fetchall()
        elif departmanseçiniz=="yönetim" or departmanseçiniz=="6":
            cursor.execute("select * from yönetim") 
            data = cursor.fetchall()
        elif departmanseçiniz=="satışvepazarlama" or departmanseçiniz=="5":
            cursor.execute("select * from satışvepazarlama") 
            data = cursor.fetchall()
        elif departmanseçiniz=="muhasebevefinans" or departmanseçiniz=="4":
            cursor.execute("select * from muhasebevefinans") 
            data = cursor.fetchall()

        while True:
            print("{:<4} {:<15} {:<15} {:<15} {:<15} {:<15} ".format("id","isim","Soyisim","görev","yaş","cinsiyet"))
            for   satir  in data:
                print("{:<4} {:<15} {:<15}  {:<15} {:<15} {:<15}".format(satir[0],satir[1],satir[2],satir[3],satir[4],satir[5]))     
            break
        break

def sil():
    while True:
        isim = input( "silmek istediğiniz kişinin ismini tek tırnak içinde giriniz :")
        if departmanseçiniz=="bilişim" or departmanseçiniz=="7" :
            cursor.execute("delete from bilişim where isim ="+isim)        
        elif departmanseçiniz=="insankaynakları" or departmanseçiniz=="1":
            cursor.execute("delete from insankaynakları where isim ="+isim)       
        elif departmanseçiniz=="araştırma_geliştirme" or departmanseçiniz=="3":
            cursor.execute("delete from araştırma_geliştirme where isim ="+isim)       
        elif departmanseçiniz=="üretim" or departmanseçiniz=="2":
            cursor.execute("delete from üretim where isim ="+isim)
        elif departmanseçiniz=="yönetim" or departmanseçiniz=="6":
            cursor.execute("delete from yönetim where isim ="+isim)
        elif departmanseçiniz=="satışvepazarlama" or departmanseçiniz=="5":
            cursor.execute("delete from satışvepazarlama where isim ="+isim)
        elif departmanseçiniz=="muhasebevefinans" or departmanseçiniz=="4":
            cursor.execute("delete from muhasebevefinans where isim ="+isim)
        while True:
            connection.commit()
            print("veri silindi")
            break
        break

while devam in ('E','e'):
    print("*************************")
    print("MySQL Veritabanı İşlemleri")
    print("(1) Tüm Kayıtları Listele")
    print("(2) veri Ekle")       
    print("(3) veri Ara")
    print("(4) veri Güncelle")
    print("(5) veri Sil")
    secim = input("Seçim Yapınız :")
    if secim=="5":
        sil()  
    if secim =="2":
        ekle()
    if secim=="4":
        güncelle(3,'isim','soyisim')
    if secim=="3":
        ara()
    if secim=="1":
        listele()
    devam = input("Devam etmek için (E/e) tuşuna basın ya da çıkmak için ENTER ı tuşlayınnız :")

print("Programdan Çıktınız")
print(datetime.now()) 