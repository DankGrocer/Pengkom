import time
import os

#data waktu untuk jenis makanan (dalam detik)
popcorn = 180       #3 menit
defrost = 540       #9 menit
instant = 180       #3 menit
vegetables = 120    #2 menit
quickstart = 30     #30 detik

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def Mode():
    clear()
    print("Status Microwave: ON")
    mode = str(input("Pilih mode masukan yang akan dipilih(otomatis/manual): "))
    if mode=="otomatis":
        Pilihan()
    elif mode=="manual":
        waktu = int(input("Masukkan waktu: "))
        Timer(waktu)

def Pilihan():
        clear()
        print('''Status Microwave: ON

Jenis Makanan:
1 : Popcorn
2 : Defrost
3 : Instant Food
4 : Vegetables

Option lain:
5 : Quickstart

        ''')
        jenis = int(input("Pilih opsi(1/2/3/4/5): "))
        if jenis==1:
            Timer(popcorn)
        elif jenis==2:
            Timer(defrost)
        elif jenis==3:
            Timer(instant)
        elif jenis==4:
            Timer(vegetables)
        elif jenis==5:
            Timer(quickstart)
        else:
            clear()
            print("Tidak ada jenis makanan tersebut, ulangi.")
            Pilihan()

def Timer(waktu):
    clear()
    print("Status Microwave = ON")
    uin = waktu
    when_to_stop = abs(int(uin))
    print("Timer: ")
    while when_to_stop > -1:
        m, s = divmod(when_to_stop, 60)
        time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
        print(time_left + "\r", end="")
        time.sleep(1)
        when_to_stop -= 1
    print()
    Standby()

def Standby():
    clear()
    print("Status Microwave = ON")
    print("Makanan selesai dihangatkan!")
    print("Apakah anda akan menghangatkan lagi? (Y/N)")
    jawaban = str(input())
    if jawaban=="Y":
        Pilihan()
    else:
        print("Microwave akan dimatikan...")
        time.sleep(5)
        Power()

def Power():
    clear()
    print("Status Microwave: OFF")
    print("Silahkan tekan apapun untuk menyalakannya.")
    input()
    Mode()

Power()
