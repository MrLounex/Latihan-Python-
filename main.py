kondisi_berhenti = 9999

while True:
    start = int(input("Masukkan bilangan awal: "))
    end = int(input("Masukkan bilangan akhir:"))
    if start == kondisi_berhenti or end == kondisi_berhenti:
        break

    if start < 0 or end < 0:
        print(
            "Bilangan negatif ditemukan. Apakah Anda ingin mengabaikan bilangan negatif? (y/n):"
        )
        pilihan = input()
        if pilihan.lower() == "y":
            if start < 0:
                start = 0
            if end < 0:
                end = 0
        elif pilihan.lower() == "n":
            continue

    counter_bilangan_genap = 0
    counter_bilangan_ganjil = 0
    total_bilangan_genap = 0
    total_bilangan_ganjil = 0
    bilangan_ganjil_terbesar = 0
    bilangan_ganjil_terkecil = 0
    bilangan_genap_terbesar = 0
    bilangan_genap_terkecil = 0
    counter_bilangan_prima = 0

    # Menampilkan List Bilangan Genap
    print("List Bilangan Genap:")
    # 0 1 2 3 4 5 6 7 8 9 10
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
            counter_bilangan_genap = counter_bilangan_genap + 1
            total_bilangan_genap = total_bilangan_genap + i

        if i % 2 == 0 and i == end :
            bilangan_genap_terbesar = bilangan_genap_terbesar + i
        
        if i % 2 == 0 and i + 1 == end :
            bilangan_genap_terbesar = bilangan_genap_terbesar + i

        if i % 2 == 0 and i == start :
            bilangan_genap_terkecil = bilangan_genap_terkecil + i

        if i % 2 == 0 and i - 1 == start :
            bilangan_genap_terkecil = bilangan_genap_terkecil + i


    print("\n")

    # Menampilkan List Bilangan Ganjil
    print("List Bilangan Ganjil:")
    # 0 1 2 3 4 5 6 7 8 9 10
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")
            counter_bilangan_ganjil = counter_bilangan_ganjil + 1
            total_bilangan_ganjil = total_bilangan_ganjil + i

        if i % 2 != 0 and i == end :
            bilangan_ganjil_terbesar = bilangan_ganjil_terbesar + i
        
        if i % 2 != 0 and i + 1 == end :
            bilangan_ganjil_terbesar = bilangan_ganjil_terbesar + i

        if i % 2 != 0 and i == start:
            bilangan_ganjil_terkecil = bilangan_ganjil_terkecil + i

        if i % 2 != 0 and i - 1 == start :
            bilangan_ganjil_terkecil = bilangan_ganjil_terkecil + i
    print("\n")

    # Menampilkan Bilangan Prima
    print("List bilangan Prima : ")
    for i in range(start, end + 1):
        if i > 1:
            cek_prima = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    cek_prima = False
                    break
            if cek_prima:
                print(i, end=" ")
                counter_bilangan_prima += 1
    print('\n')

    # Menampilkan Bilangan Terbalik 
    print("Urutan Bilangan Terbalik adalah :", )
    for i in range(0, end) :
        print(end - i, end = " ")
    print("\n")


    print("Jumlah Bilangan Genap adalah :" + str(counter_bilangan_genap))
    print("Jumlah Bilangan Ganjil adalah:" + str(counter_bilangan_ganjil))
    print("Total Jumlah Bilangan Genap adalah :" + str(total_bilangan_genap))
    print("Total Jumlah Bilangan Ganjil adalah:" + str(total_bilangan_ganjil))
    print(
    "Rata-Rata Bilangan Genap adalah:"
        + str(total_bilangan_genap / counter_bilangan_genap)
    )
    print(
        "Rata-Rata Bilangan Ganjil adalah:"
        + str(total_bilangan_ganjil / counter_bilangan_ganjil)
    )

    print("HASIL".center(40, "="))

    print("Jumlah bilangan prima adalah :" + str(counter_bilangan_prima))
    print("Bilangan Ganjil terbesar adalah :", str(bilangan_ganjil_terbesar))
    print("Bilangan Ganjil Terkecil adalah :", str(bilangan_ganjil_terkecil))
    print("Bilangan Genap terbesar adalah :", str(bilangan_genap_terbesar))
    print("Bilangan Genap Terkecil adalah :", str(bilangan_genap_terkecil))

    print("\n")

if start > end:
    print(
    "Error: Bilangan awal lebih besar dari bilangan akhir. Masukkan nilai yang benar."
    )



# SOAL:
# Bilangan prima: [2, 3, 5, 7]
# Jumlah bilangan prima: 4
# Bilangan ganjil terbesar: 9
# Bilangan ganjil terkecil: 1
# Bilangan genap terbesar: 10
# Bilangan genap terkecil: 2
# Urutan bilangan dalam rentang (terbalik): [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
