# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:25:17 2019

@author: FATMANUR
"""

import os,math,time
stringVeri=""
gelenKarakter=""
sozlugum={}
sayac=0
emptyString=""


def SozlukOlustur(sozlugum):
    global sayac
    for i in range(len(stringVeri)): #her bir karakter için kontrol yapıyorum.
        if stringVeri[i] in sozlugum.values(): #eğer karakter sözlüğüm içinde var ise
            print(stringVeri[i] +" Zaten Sözlükte Mevcut!")
        else:
            sozlugum[sayac]=stringVeri[i] #karakter sözlükte yoksa sözlüğe ekliyorum.
            sayac+=1
           
def SozlukteBul(Aranacak):
    for key,value in sozlugum.items(): # sözlüğün itemları içinde key,value değerlerine bak!
        if value==Aranacak:
            return key
        
    
        
def LZW():
    global emptyString,gelenKarakter,sayac #sayacı kullanma nedenim sayacın son değerinden itibaren ekleme yapabilmek için kullanıyorum.
    yeniSayac=0 #başka bir sayaca da ihtiyacım var.
    while yeniSayac< len(stringVeri): #yani okunacak veri oldukça dönmek için
        gelenKarakter=stringVeri[yeniSayac] #gelen karakteri okuyorum, yani girilen stringin yeniSayac'ındaki indexi.
        
        if emptyString+gelenKarakter in sozlugum.values(): #boşstring+gelenkrakter değerim sözlüğün valueları içinde var ise
            emptyString+=gelenKarakter # bunları birleştir.
            yeniSayac+=1
        else:
            key=SozlukteBul(emptyString)
            print(str(key)+" ("+sozlugum[key]+")")
            sozlugum[sayac] = emptyString + gelenKarakter
            emptyString = gelenKarakter # artık boşstring yeni bir karaktere dönüşüyor.
            sayac+=1
            yeniSayac+=1
    key=SozlukteBul(emptyString)
    print(str(key)+" ("+sozlugum[key]+")")

def getSize(dosyaAdi):
    st = os.stat(dosyaAdi)
    return st.st_size

def veriGonder(path):
    with open(path) as f:
       veri=f.read().replace('\n', '')
       return veri
           
path="metin1.txt"
stringVeri=veriGonder(path)
print(stringVeri)
baslangic=time.time()
SozlukOlustur(sozlugum)
LZW()
bitis=time.time()-baslangic
#a=math.ceil(bitis)
print(sozlugum)
boyut1=getSize('metin1.txt')
boyut2=getSize('sonuc.txt')
#print(str(boyut1)+ "  bayt ")
print("Sıkıştırmadan önce  "+str(boyut1)+" tane karakter kullanılıyor tanımlamak için.")
print(str(boyut1*8)+"bayt kullanmamız gerekir")
sonrakiDosya=open('sonuc.txt','w')
sonrakiDosya.write(str(sozlugum.keys()))
sonrakiDosya.close()
#print("Sıkıştırıldıktan sonra"str(boyut2)+ "  bayt ")
#print("Ama  "+str(boyut2)+" tane karakter kullanılıyor tanımlamak için.")
print("Sıkıştırma Süresi: "+str(bitis) +"  saniye")

