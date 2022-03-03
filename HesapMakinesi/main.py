def toplama(num1,num2):
    print (num1+num2)
def cikarma(num1,num2):
    print (num1-num2)
def carpma(num1,num2):
   print (num1*num2)
def bolme(num1,num2):
    print (num1/num2)
while(True):
    sayi1=int(input("sayi giriniz:"))
    sayi2=int(input("sayi giriniz:"))
    islem=input("işlem seçiniz: + - * /")
    if islem == "+":
        toplama(sayi1,sayi2)
    elif islem == "-":
        cikarma(sayi1,sayi2)
    elif islem == "*":
        carpma(sayi1,sayi2)
    elif islem== "/":
        bolme(sayi1,sayi2)
    else:
        print("yanlış işlem yaptınız")