name= input("adınızı girin:")
print("adam asmaca oyununa hoşgeldin "+ name)
print("10 canınız var !")
kelime="yapayzeka"
tahmin=""
gizli="---------"
can=10
while can>0 :
    kalanharf=0
    for karakter in kelime:
        if karakter in tahmin:
            print(karakter)
        else:
            print("-")
            kalanharf+=1
    if kalanharf==0:
        print("Kelimeyi buldunuz.Tebrikler!")
        break
    tahmin_harf=input("harf tahmin edin")
    tahmin+=tahmin_harf
    if tahmin_harf not in kelime:
        can-=1
        print(f"kalan can sayısı: {can}")
        if(can==0):
            print("oyun bitti")