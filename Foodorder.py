#kedai makan
#loop order makanann
import time

print ("selamat datang ke kedai makan rahman")

#makanan yang ada
menu_mkn = {'Nasi': 5, 'Ayam': 7,'Daging': 8, 'Ikan': 9}
menu_minum = {'Sirap': 1, 'Oren': 2, 'Teh': 8}

# dia = list(menu_mkn)
# print(dia)

# saya = menu_mkn.get('nasi')
# print(saya)

# for i,j in menu_mkn.items():
#     print(i +": " + str(j))
    
time.sleep(0.5)
print("nak dine in ke take away?. tekan numbor kalau nak dine in dan huruf kalau take away")
jwpn1 = input().strip()

def tmenu_mkn():
    print(f"sini ada {len(menu_mkn)} jenis makanan")
    print("menu makan".center(20,"-"))
    for i,j in menu_mkn.items():
        print(f"{i}: ".ljust(10) + f"RM{str(j)}".rjust(10))

def tmenu_minum():
    print(f"sini ada {len(menu_minum)} jenis minuman")
    print("menu minuman".center(20,"-"))
    for i,j in menu_minum.items():
         print(f"{i}: ".ljust(10) + f"RM{str(j)}".rjust(10))

def order_mkn():
    o_mkn = [],[]
    while True:
        tnya_1 = input("nak makan apa?, kalau tanak type keluar: ").capitalize().strip()
        if tnya_1 in menu_mkn:
            if tnya_1 in o_mkn[0]:
                while True:
                    tnya1 = input("berapa banyak: ").strip()
                    if tnya1.isdecimal() == False:
                        print("boleh letak nombor je.")
                    else:
                        break
                tambah_mknn = o_mkn[0].index(tnya_1)
                hasil_t = int(o_mkn[1][tambah_mknn]) + int(tnya1)
                o_mkn[1][tambah_mknn] = str(hasil_t)
            elif tnya_1 not in o_mkn[0]:
                o_mkn[0].append(tnya_1)
                while True:
                    tnya1 = input("berapa banyak: ").strip()
                    if tnya1.isdecimal() == False:
                        print("boleh letak nombor je.")
                    else:
                        break
                o_mkn[1].append(tnya1)
            nak_lagi1 = input("kalau tanak type no, kalau nak type je pape: ").lower()
            if nak_lagi1 == "no":
                break
            else:
                continue
        elif tnya_1 == "keluar".capitalize():
            break
        else:
            print("maaf makanan yang anda order tiada dalam menu".capitalize())
            
    return o_mkn

def order_minum():
    o_minum = [],[]
    while True:
        tnya_2 = input("nak minum apa?, kalau tanak type keluar: ").capitalize().strip()
        if tnya_2 in menu_minum:
            if tnya_2 in o_minum[0]:
                while True:
                    tnya2 = input("berapa banyak: ").strip()
                    if tnya2.isdecimal() == False:
                        print("boleh letak nombor je.")
                    else:
                        break
                tambah_minuman = o_minum[0].index(tnya_2)
                hasil_t = int(o_minum[1][tambah_minuman]) + int(tnya2)
                o_minum[1][tambah_minuman] = str(hasil_t)
            elif tnya_2 not in o_minum[0]:
                o_minum[0].append(tnya_2)
                while True:
                    tnya2 = input("nak berapa: ").strip()
                    if tnya2.isdecimal() == False:
                        print("boleh letak nombor je")
                    else:
                        break
                o_minum[1].append(tnya2)
            nak_lagi2 = input("kalau tanak type no, kalau nak type je pape: ").lower()
            if nak_lagi2 == "no":
                break
            else:
                continue
        elif tnya_2 == "keluar".capitalize():
            break
        else:
            print("maaf minuman yang anda order tiada dalam menu".capitalize())
    return o_minum

def harga_mknn(mkn_d1, mkn_d2):
    harga_all_mknn = 0
    for k, n in zip(mkn_d1, mkn_d2):
        print(f"{k}:".ljust(10) + "RM" + f"{int(menu_mkn[k])*int(n)}".rjust(3))
        harga_all_mknn += int(menu_mkn[k])*int(n)
        
    return harga_all_mknn
        
def harga_minuman(minum_d1, minum_d2):
    harga_all_minuman = 0
    for y, z in zip(minum_d1, minum_d2):
        print(f"{y}:".ljust(10) + "RM" + f"{int(menu_minum[y])*int(z)}".rjust(3))
        harga_all_minuman += int(menu_minum[y])*int(z)
        
    return harga_all_minuman
    
if jwpn1.isalpha() == True or jwpn1.isdecimal() == True:
    tmenu_mkn()
    mknn_diorder = order_mkn()
    tmenu_minum()
    minuman_diorder = order_minum()
    j_oder = len(mknn_diorder[0]) # berapa type mknn order
    k_oder = len(minuman_diorder[0]) #berapa type minuman order
    
    mkn_d1 = mknn_diorder[0] #apa mknn dah order 
    mkn_d2 = mknn_diorder[1] #berapa mknn dah order each
    minum_d1 = minuman_diorder[0] #apa minuman dah order 
    minum_d2 = minuman_diorder[1] #berapa minuman dah order each
    time.sleep(1)
    
    if j_oder == 0 and k_oder > 0:
        print("Minumnan diorder adalah: ")
        for x,y in zip(minum_d1,minum_d2):
            print(x.ljust(7,"."), y.rjust(3,"."))
            
        # print("Anda tidak order makanan, minuman yang diorder adalah " + ", ".join(minuman_diorder[0]) + " sebanyak " + ", ".join(minuman_diorder[1]))
        print("jumlah bayaran setiap item".capitalize())
        
    elif k_oder == 0 and j_oder > 0:
        print("Makanan diorder adalah: ")
        for v,w in zip(mkn_d1,mkn_d2):
            print(v.ljust(7,"."), w.rjust(3,"."))
            
        # print("Makanan yang telah diorder adalah " + ", ".join(mknn_diorder[0])+ " sebanyak " + ", ".join(mknn_diorder[1]) + " dan anda tidak order minuman.")
        print("jumlah bayaran setiap item".capitalize())
    elif j_oder == 0 and k_oder == 0:
        print("Anda tidak order apa apa")
    else:
        print("Makanan dan minuman diorder adalah: ")
        # for v,w,t,u in zip(mkn_d1,mkn_d2,minum_d1,minum_d2):
        #     print(v.ljust(7,"."), w.rjust(3,"."), t.ljust(7,"."), u.rjust(3,"."))
        for v,w in zip(mkn_d1,mkn_d2):
            print(v.ljust(7,"."), w.rjust(3,"."))
            
        for x,y in zip(minum_d1,minum_d2):
            print(x.ljust(7,"."), y.rjust(3,"."))
        # print("Makanan yang telah diorder adalah " + ", ".join(mknn_diorder[0]) + " sebanyak " + ", ".join(mknn_diorder[1]) + " dan minuman diorder adalah " + ", ".join(minuman_diorder[0]) + " sebanyak " + ", ".join(minuman_diorder[1]))
        print("jumlah bayaran setiap item".capitalize())
    
    h_mknn = harga_mknn(mkn_d1, mkn_d2)
    h_minuman = harga_minuman(minum_d1, minum_d2)
    harga_all = h_mknn + h_minuman
    time.sleep(2)
    print(f"Harga yang perlu dibayar adalah sebanyak RM{harga_all} ")
    
    time.sleep(1)
    if jwpn1.isalpha() == True:
        print("Ini adalah makanan take away yang anda pesan")
    elif jwpn1.isdecimal() == True:
        print("Makanan yang telah tersedia adalah untuk makan di kedai rahman")
else:
    print("Sila keluar dari kedai rahman")