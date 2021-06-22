import math

def sayi_al(sonlandir,sinir,mesaj): #lno numaralirini 0 veya eksi rakam girinceye kadar aliyor
    hatali_giris = True
    while hatali_giris:
        try:
            veri = int(input(mesaj))
            if veri >= sinir:
                return veri
            if veri in range(sonlandir+1,sinir):
                print('Lütfen belirtilen aralikta veri girişi yaparak tekrar deneyin: ')
            if veri == sonlandir:
                return  0
        except ValueError:
            print('Lütfen sayısal veri girerek tekrar deneyin: ')

def buyutme(isim): #oyuncu isimlerini turk alfabesini uygun buyutuyor
    oyuncu_ismi = isim.replace('i', 'İ').replace('ı', 'I')
    isimler = oyuncu_ismi.upper()
    return isimler

def girdileri_al(): #oyuncu bilgilerini kullanicidan aliyor
    oyuncular = []
    lisans_no = []
    LNo = int(input('Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz): '))
    while LNo > 0:
        oyuncu_verileri = [0, 0, 0, 0]
        while LNo in lisans_no:
            LNo = int(input('Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz): '))
        if LNo > 0:
            lisans_no.append(LNo)
            isim = buyutme(input('Oyuncunun adini-soyadini giriniz:'))
            ELO = sayi_al(0,1000,'Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0): ')
            UKD = sayi_al(0,1000,'Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0): ')
            oyuncu_verileri.append(isim)
            oyuncu_verileri[0] += LNo
            oyuncu_verileri[1] += ELO
            oyuncu_verileri[2] += UKD
            oyuncular.append(oyuncu_verileri)
        print(' ')
    return oyuncular

def baslangic_listeyi_yazdir(oyuncular): # oyuncularin verilen kurallara gore dogru siraliyib baslangic liste yazdiriyor
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ "
    oyuncu_siralama = sorted(oyuncular, key=lambda word: (-word[1], -word[2],[alfabe.find(c) for c in word[4]],word[0]))

    print('BSNo       LNo         Ad-Soyad                   ELO         UKD')
    print('----       -----       --------------------       ------      ------')
    for no in range (len(oyuncular)):
        print("{:>4}".format(no+1),end = '')
        oyuncu_siralama[no].append(no+1)
        print("{:>12}".format(oyuncu_siralama[no][0]),'     ',"{:<27}".format(oyuncu_siralama[no][4]),
              "{:>5}".format(oyuncu_siralama[no][1]),"{:>11}".format(oyuncu_siralama[no][2]))

    return oyuncu_siralama

def sinirlari_ayarla(min,max,mesaj): #istedigimiz mesaj ve sinirlar gondererek dogru aralik girinceye kadar veri girisi istiyor
    veri = int(input(mesaj))
    while veri not in range (min,max+1):
        veri = int(input('Lutfen belirtilen aralikta sayi giriniz '+ '('+ str(min)+'-' + str(max)+'): '))

    return veri

def tur_sayi_ve_renk_belirleme(oyuncu_say): # ilk turdaki ilk rengi ve tur sayini kurallara uygun aliyor
    min_deger = math.ceil(math.log(oyuncu_say,2))
    max_deger = oyuncu_say-1
    tur_say = sinirlari_ayarla(min_deger,max_deger,'Turnuvadakı tur sayısını giriniz '+'('+ str(min_deger)+'-'+str(max_deger)+'): ')
    renk = input('Baslanğıc sıralamasına gore ilk oyuncunun ilk turdaki rengini giriniz (b/s): ')
    while renk not in ['b','s']:
        renk = str(input('Lütfen doğru rengi giriniz (b/s): '))

    return tur_say,renk

def index_bulma(my_list,x): #istedigimiz 2 boyutlu listede verilen elemanin liste indexini buluyor
    for i in my_list:
        if x in i:
            while i.index(x) == 0:
                return my_list.index(i)

def puan_ver(oyuncu_siralama,tur_sonuclari,tur): # her turdan sonra oyunculara puan veriyor
    for masa_no in range (len(oyuncu_siralama)//2):
        print(tur+1,'.turda', masa_no+1,'. masada oynanan ',end='')
        islem_no = sinirlari_ayarla(0,5,'macin sonucunu giriniz (0-5): ')

        puan_verildi = True
        for i in range (len(oyuncu_siralama)):

            if len(tur_sonuclari[oyuncu_siralama[i][0]]) <= (tur * 4 + 2) and puan_verildi:

                if islem_no == 0:
                    oyuncu_siralama[i][3] += 0.5
                    tur_sonuclari[oyuncu_siralama[i][0]].extend((0.5, 'beraber'))
                    tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4*tur]].extend((0.5,'beraber'))

                    index = index_bulma(oyuncu_siralama,tur_sonuclari[oyuncu_siralama[i][0]][4 * tur])
                    oyuncu_siralama[index][3] += 0.5
                elif islem_no == 1:
                    if tur_sonuclari[oyuncu_siralama[i][0]][4 * tur + 1] == 'b':
                        oyuncu_siralama[i][3] += 1
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((1, 'k'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((0, 'e'))
                    else:
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((0, 'e'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((1, 'k'))
                        index = index_bulma(oyuncu_siralama, tur_sonuclari[oyuncu_siralama[i][0]][4 * tur])
                        oyuncu_siralama[index][3] += 1
                elif islem_no == 2:
                    if tur_sonuclari[oyuncu_siralama[i][0]][4 * tur + 1] == 's':
                        oyuncu_siralama[i][3] += 1
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((1, 'k'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((0, 'e'))
                    else:
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((0, 'e'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((1, 'k'))
                        index = index_bulma(oyuncu_siralama, tur_sonuclari[oyuncu_siralama[i][0]][4 * tur])
                        oyuncu_siralama[index][3] += 1

                elif islem_no == 3:
                    if tur_sonuclari[oyuncu_siralama[i][0]][4 * tur + 1] == 's':
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((0, 'gelmedi'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((1, 'tur atladi'))
                        index = index_bulma(oyuncu_siralama, tur_sonuclari[oyuncu_siralama[i][0]][4 * tur])
                        oyuncu_siralama[index][3] += 1
                    else:
                        oyuncu_siralama[i][3] += 1
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((1, 'tur atladi'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((0, 'gelmedi'))

                elif islem_no == 4:
                    if tur_sonuclari[oyuncu_siralama[i][0]][4 * tur + 1] == 'b':
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((0, 'gelmedi'))
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((1, 'tur atladi'))
                        index = index_bulma(oyuncu_siralama, tur_sonuclari[oyuncu_siralama[i][0]][4 * tur])
                        oyuncu_siralama[index][3] += 1
                    else:
                        oyuncu_siralama[i][3] += 1
                        tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((0, 'gelmedi'))
                        tur_sonuclari[oyuncu_siralama[i][0]].extend((1, 'tur atladi'))
                else:
                    tur_sonuclari[oyuncu_siralama[i][0]].extend((0, 'gelmedi'))
                    tur_sonuclari[tur_sonuclari[oyuncu_siralama[i][0]][4 * tur]].extend((0, 'gelmedi'))
                puan_verildi = False

    return tur_sonuclari,oyuncu_siralama

def birinci_eslesme(oyuncu_siralama,baslangic_renk,tur_sonuclari): # birinci turun eslesmesini yapiyor
    for sira in range (0,len(oyuncu_siralama),2):
        try:
            tur_sonuclari[oyuncu_siralama[sira][0]].extend((oyuncu_siralama[sira+1][0],baslangic_renk))
            tur_sonuclari[oyuncu_siralama[sira+1][0]].extend((oyuncu_siralama[sira][0],renk_sec(baslangic_renk)))
        except  IndexError:
            tur_sonuclari[oyuncu_siralama[len(oyuncu_siralama)-1][0]].extend(('BYE','-',1,'bye gecti'))

    return tur_sonuclari

def bye_bulma(oyuncu_siralama,tur_sonuclari): #her turdan once kurallara uygun sekilde bye eleman buluyor
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ "
    oyuncu_listesi = sorted(oyuncu_siralama,key=lambda word: (-word[3],-word[1], -word[2], [alfabe.find(c) for c in word[4]], word[0]))
    if len(oyuncu_listesi) % 2 != 0:
        BYE = False
        while BYE == False:
            for list in oyuncu_listesi[::-1]:
                if 'BYE' in tur_sonuclari[list[0]] or 'tur atladi' in tur_sonuclari[list[0]]:
                    BYE = False
                else:
                    BYE = True
                    tur_sonuclari[list[0]].extend(('BYE','-',1,'bye gecti'))
                    bye_oyuncu = oyuncu_listesi.pop(oyuncu_listesi.index(list))
                    return oyuncu_listesi,bye_oyuncu,tur_sonuclari, BYE
    else:
        bye_oyuncu = [0,0,0,0]
        BYE = False
        return oyuncu_listesi,bye_oyuncu,tur_sonuclari, BYE

def renk_sec(reng): #verilen rengin eksi olan rengi geri donduruyor
    if reng:
        if reng == 's':
            rakip_renk = 'b'
            return rakip_renk

        elif reng == 'b':
            rakip_renk = 's'
            return rakip_renk

def renk_ayarlama(oyuncu_siralama,tur_sonuclari): #renk kurallarini eslesme zamani ayarliyor
    if tur_sonuclari[oyuncu_siralama[0]][::-1][2] == 'b' or tur_sonuclari[oyuncu_siralama[0]][::-1][2] == 's':

        if len(tur_sonuclari[oyuncu_siralama[0]]) <=4:
            if tur_sonuclari[oyuncu_siralama[0]][1] == 's':
                return 'b'
            else:
                return 's'

        elif len(tur_sonuclari[oyuncu_siralama[0]])>4:

            if tur_sonuclari[oyuncu_siralama[0]][::-1][2] != tur_sonuclari[oyuncu_siralama[0]][::-1][6]:
                data = renk_sec(tur_sonuclari[oyuncu_siralama[0]][::-1][2])
                if abs(tur_sonuclari[oyuncu_siralama[0]].count('s') - tur_sonuclari[oyuncu_siralama[0]].count('b')) >= 2:
                    data = tur_sonuclari[oyuncu_siralama[0]][::-1][2]

                return data
            else:
                data = renk_sec(tur_sonuclari[oyuncu_siralama[0]][::-1][2])
                return  data

def eslestir(oyuncu_siralama, tur_sonuclari,tur_sayi,bye_oyuncu,BYE): #her turda oyunculari eslestiriyor
    for no in range(len(oyuncu_siralama) - 1):
        max_puan = oyuncu_siralama[no][3]
        j_bool = True
        renk_no = renk_ayarlama(oyuncu_siralama[no], tur_sonuclari)
        if len(tur_sonuclari[oyuncu_siralama[no][0]]) <= (tur_sayi+1) * 4:
            renk_degisme = False
            renk_degisme_no = False
            renkler_degisti_j = False
            renkler_degisti_no = False
            max_puan_degisti = False
            renk_no_degistir = False#bu fonksiyonda no olan herbirsey rakibi aranan oyuncudur
            renk_j_degistir = False #bu fonksiyonda j olan herkes rakip olacak oyuncudur
            count = 1
            while j_bool:

                for j in range(no + 1, len(oyuncu_siralama)):
                    if oyuncu_siralama[j][0] not in tur_sonuclari[oyuncu_siralama[no][0]]:

                        renk_j = renk_ayarlama(oyuncu_siralama[j], tur_sonuclari)
                        if renk_j_degistir:
                            renk_j = renk_sec(renk_j)
                            renkler_degisti_j = True
                            if len(tur_sonuclari[oyuncu_siralama[j][0]]) > 4 and len(tur_sonuclari[oyuncu_siralama[j][0]]) <= (tur_sayi+1) * 4:
                                if tur_sonuclari[oyuncu_siralama[j][0]][::-1][2] == tur_sonuclari[oyuncu_siralama[j][0]][::-1][6]:
                                    renk_j = renk_ayarlama(oyuncu_siralama[j],tur_sonuclari)

                        if renk_no_degistir:
                            renkler_degisti_no = True
                            if len(tur_sonuclari[oyuncu_siralama[no][0]]) > 4 and len(tur_sonuclari[oyuncu_siralama[j][0]]) <= (tur_sayi+1) * 4:
                                if tur_sonuclari[oyuncu_siralama[no][0]][::-1][2] == tur_sonuclari[oyuncu_siralama[no][0]][::-1][6]:
                                    renk_no = renk_ayarlama(oyuncu_siralama[no],tur_sonuclari)

                        if max_puan_degisti:
                            renk_no = renk_ayarlama(oyuncu_siralama[no], tur_sonuclari)

                        if oyuncu_siralama[j][3] == max_puan:
                            if len(tur_sonuclari[oyuncu_siralama[j][0]]) <= (tur_sayi+1) * 4:

                                    if renk_no and renk_j:
                                        if (renk_no == "s" and renk_j == 'b') or renk_no == "b" and renk_j == 's':
                                            tur_sonuclari[oyuncu_siralama[no][0]].extend((oyuncu_siralama[j][0], renk_no))
                                            tur_sonuclari[oyuncu_siralama[j][0]].extend((oyuncu_siralama[no][0], renk_j))
                                            j_bool = False
                                            renk_degisme = True
                                            renk_degisme_no = True
                                            break
                                    else:
                                        if renk_no:
                                            renk_j = renk_sec(renk_no)
                                        else:
                                            renk_no = renk_sec(renk_j)
                                        tur_sonuclari[oyuncu_siralama[no][0]].extend((oyuncu_siralama[j][0], renk_no))
                                        tur_sonuclari[oyuncu_siralama[j][0]].extend((oyuncu_siralama[no][0], renk_j))
                                        j_bool = False
                                        renk_degisme = True
                                        renk_degisme_no = True
                                        break

                if count == 1:
                    if renk_degisme == False:
                        renk_j_degistir = True

                if count == 2:
                    if renkler_degisti_j and not renk_degisme_no:
                        renk_no = renk_sec(renk_no)
                        renk_j_degistir = True
                        renk_no_degistir = True

                if count == 3:
                    if renkler_degisti_j and renkler_degisti_no and max_puan != 0:
                        max_puan_degisti = True
                        max_puan -= 0.5
                        renk_j_degistir = False
                        renk_no_degistir = False
                        count +=1
                        count = 0
                count +=1

    if BYE:
        oyuncu_siralama.append(bye_oyuncu)
    return tur_sonuclari,oyuncu_siralama


def eslesme_listesi_yazdir(oyuncu_siralama,tur_sonuclari,tur): #her turdan sonra eslesme listesi yazdiriyor
    print('\n',tur+1,". Tur Eşleştirme Listesi:")
    print('            Beyazlar               Siyahlar')
    print('MNo     BSNo    LNo     Puan  - Puan     LNo    BSNo')
    print('---     -----   ----    -----   -----    ----   -----')
    masa_no = 1
    a = []
    for list in oyuncu_siralama:
        if list[0] not in a:
            if tur_sonuclari[list[0]][4 * tur] != 'BYE':
                no = oyuncu_siralama[index_bulma(oyuncu_siralama, tur_sonuclari[list[0]][4 * tur])]
                if tur_sonuclari[list[0]][4*tur +1] == 'b':
                    print("{:>3}".format(masa_no),"{:>9}".format(list[5]), "{:>6}".format(list[0]), "{:>7.2f}".format(list[3]),"{:^2}".format('-'),"{:>4.2f}".format(no[3]),"{:>7}".format(no[0]),"{:>7}".format(no[5]))

                elif tur_sonuclari[list[0]][4*tur +1] == 's':
                    print("{:>3}".format(masa_no),"{:>9}".format(no[5]),"{:>6}".format(no[0]),"{:>7.2f}".format(no[3]),"{:^2}".format('-'),"{:>4.2f}".format(list[3]), "{:>7}".format(list[0]), "{:>7}".format(list[5]))
            else:
                print("{:>3}".format(masa_no),"{:>9}".format(list[5]), "{:>6}".format(list[0]), "{:>7.2f}".format(list[3]),"{:^2}".format('-'),    'BYE')

            masa_no += 1
        a.extend((list[0], tur_sonuclari[list[0]][4 * tur]))


def bh1_bh2_ve_gs(tur_sonuclari,oyuncu_siralama,tur_sayi): #esitlik bozma icin bh1 bh2 ve galibiyyet sayilarini buluyor
    BH1 = []
    galibiyet = []
    bh1_listesi = []
    bh2_listesi = []
    for i in tur_sonuclari:
        galibiyet.append(tur_sonuclari[i].count('k') + tur_sonuclari[i].count('tur atladi'))
        bh1 = []
        for tur in range(tur_sayi):
            puan = 0
            if tur_sonuclari[i][4 * tur+3] in ['e','k','beraber']:
                index = index_bulma(oyuncu_siralama,tur_sonuclari[i][4 * tur])
                puan = oyuncu_siralama[index][3]

            else:
                if tur != 0:
                    for a in range (tur):
                        puan += tur_sonuclari[i][4 * a +2]
                    puan += 0.5* (tur_sayi-1-tur)
                else:
                    puan = 0.5* (tur_sayi - 1)
            bh1.append(puan)
        BH1.append(bh1)

    for sira in range (len(BH1)):
        BH1[sira].remove(min(BH1[sira]))
        bh1_listesi.append(sum(BH1[sira]))
        BH1[sira].remove(min(BH1[sira]))
        bh2_listesi.append(sum(BH1[sira]))

    return bh1_listesi,bh2_listesi,galibiyet

def sonneborn_berger(oyuncu_siralama,tur_sonuclari,tur_sayi): #esitlik bozma icin sonneborn berger kuralini uyguluyor
    SB =[]
    sb_listesi =[]
    # tur_sayi = 5
    for i in tur_sonuclari:
        sb = []
        for tur in range (tur_sayi):
            bal = 0
            if tur_sonuclari[i][4*tur +3] in ['k','beraber']:
                index = index_bulma(oyuncu_siralama, tur_sonuclari[i][4 * tur])
                bal = oyuncu_siralama[index][3]

                if tur_sonuclari[i][4*tur +3] == 'beraber':
                    bal /= 2
            elif tur_sonuclari[i][4 * tur + 3] == 'tur atladi' or tur_sonuclari[i][4 * tur + 3] == 'bye gecti':
                if tur != 0:
                    for a in range(tur):
                        bal += tur_sonuclari[i][4 * a + 2]
                    bal += 0.5 * (tur_sayi - 1 - tur)
                else:
                    bal = 0.5 * (tur_sayi - 1)
            else:
                bal = 0
            sb.append(bal)
        SB.append(sb)
    for sira in range(len(SB)):
        sb_listesi.append(sum(SB[sira]))
    return sb_listesi

def listeye_ekle(bh1_listesi,bh2_listesi,berger,galibiyet,oyuncu_siralama,tur_sonuclari): #tum listeleri oyuncu bilgileri olan listeye ekliyor
    puan = 0
    for key in tur_sonuclari.keys():
        index = index_bulma(oyuncu_siralama,key)
        oyuncu_siralama[index].append(bh1_listesi[puan])
        oyuncu_siralama[index].append(bh2_listesi[puan])
        oyuncu_siralama[index].append(berger[puan])
        oyuncu_siralama[index].append(galibiyet[puan])
        puan +=1

    return oyuncu_siralama

def nihai_liste_yazdir(oyuncu_siralama):
    oyuncular = sorted(oyuncu_siralama, key=lambda word: (-word[3],-word[6],-word[7],-word[8])) #nihai listeyi yazdiriyor
    print('\nNihai Sıralama Listesi:')
    print('SNo  BSNo  LNo      Ad-Soyad               ELO      UKD      Puan     BH-1     BH-2     SB     GS')
    print('---  ----  -----    --------------------   -----    -----    -----    -----    -----    -----  ---')
    sno =1
    for list in oyuncular:
        print("{:>3}".format(sno),"{:>5}".format(list[5]),"{:>6}".format(list[0]),'  ',"{:<20}".format(list[4]),"{:>7}".format(list[1]),"{:>8}".format(list[2]),"{:>8.2f}".format(list[3]),"{:>8.2f}".format(list[6]),"{:>8.2f}".format(list[7]),"{:>8.2f}".format(list[8]),"{:>4}".format(list[9]))
        list.append(sno)
        sno += 1
    return oyuncular

def capraz_listeyi_yazdir(oyuncu_siralama,tur_sonuclari,tur_sayi): #capraz listeyi yazdiriyor
    son_oyuncu_listesi = sorted(oyuncu_siralama, key=lambda word: (word[5]))  # o biri olculer tesir eliyirmi?
    print('\nÇapraz Tablo:')
    print('BSNo  SNo  LNo      Ad-Soyad               ELO    UKD',end='    ')
    for tur in range (tur_sayi):
        print(tur+1,'.TUR',end ='  ')
    print('  Puan    BH-1     BH-2    SB    GS')
    print('----  ---  -----    --------------------   -----  ----- ',end = ' ')
    for tur in range (tur_sayi):
        print('-------',end= ' ')
    print('  -----   ------   -----   ----- ---')
    for liste in son_oyuncu_listesi:
        print("{:>4}".format(liste[5]),"{:>4}".format(liste[10]),"{:>6}".format(liste[0]),'  ',"{:<20}".format(liste[4]),
              "{:>7}".format(liste[1]),"{:>6}".format(liste[2]),end = ' ')
        for tur in range (tur_sayi):
            if tur_sonuclari[liste[0]][4*tur+2] == 0.5:
                sayi = chr(189)
            else:
                sayi = tur_sonuclari[liste[0]][4*tur+2]

            if tur_sonuclari[liste[0]][4*tur] != 'BYE':
                sira = index_bulma(son_oyuncu_listesi, tur_sonuclari[liste[0]][4 * tur])

                if tur_sonuclari[liste[0]][4*tur+3] not in ['gelmedi','tur atladi','bye gecti']:
                    print("{:>3}".format(son_oyuncu_listesi[sira][5]),"{:>}".format(tur_sonuclari[liste[0]][4*tur+1]),
                          "{:>}".format(sayi),end = ' ')

                elif tur_sonuclari[liste[0]][4*tur+3] == 'gelmedi':
                    print("{:>3}".format(son_oyuncu_listesi[sira][5]),"{:>}".format(tur_sonuclari[liste[0]][4*tur+1]),"{:>}".format('-'),end=' ')
                else:
                    print("{:>3}".format(son_oyuncu_listesi[sira][5]),"{:>}".format(tur_sonuclari[liste[0]][4*tur+1]),"{:>}".format('+'),end=' ')
            else:
                print("{:>3}".format('-'),"{:>}".format('-'),"{:>}".format(1),end=' ')
        print("{:>8.2f}".format(liste[3]),"{:>8.2f}".format(liste[6]),
              "{:>7.2f}".format(liste[7]),"{:>7.2f}".format(liste[8]),"{:>3}".format(liste[9]))

def main(): #tum fonksiyonlar burada cagriliyor
    oyuncular = girdileri_al()
    print('\nBaşlangıç Sıralama Listesi:')
    oyuncu_siralama = baslangic_listeyi_yazdir(oyuncular)
    print()
    tur_sayisi,baslangic_renk = tur_sayi_ve_renk_belirleme(len(oyuncular))
    tur_sonuclari = {}
    for i in range(len(oyuncu_siralama)):
        tur_sonuclari[oyuncu_siralama[i][0]] = tur_sonuclari.get(oyuncu_siralama[i][0], [])
    tur_sonuclari = birinci_eslesme(oyuncu_siralama,baslangic_renk,tur_sonuclari)
    for tur in range (tur_sayisi):
        eslesme_listesi_yazdir(oyuncu_siralama,tur_sonuclari,tur)
        if len(oyuncu_siralama) % 2 != 0:
            oyuncu_siralama[::-1][0][3] +=1

        tur_sonuclari,oyuncu_siralama = puan_ver(oyuncu_siralama,tur_sonuclari,tur)
        # print(tur_sonuclari,oyuncu_siralama)
        if tur == tur_sayisi-1:
            break
        oyuncu_siralama,bye_oyuncu,tur_sonuclari, BYE = bye_bulma(oyuncu_siralama,tur_sonuclari)
        print(oyuncu_siralama,tur_sonuclari)
        tur_sonuclari,oyuncu_siralama = eslestir(oyuncu_siralama,tur_sonuclari,tur,bye_oyuncu,BYE)
        # print(tur_sonuclari,oyuncu_siralama)

    bh1_listesi, bh2_listesi, galibiyet = bh1_bh2_ve_gs(tur_sonuclari, oyuncu_siralama, tur_sayisi)
    berger = sonneborn_berger(oyuncu_siralama,tur_sonuclari,tur_sayisi)
    son_liste = listeye_ekle(bh1_listesi,bh2_listesi,berger,galibiyet,oyuncu_siralama,tur_sonuclari)
    oyuncu_bilgileri = nihai_liste_yazdir(son_liste)
    capraz_listeyi_yazdir(oyuncu_bilgileri,tur_sonuclari,tur_sayisi)

main()