import pandas as pd
import matplotlib.pyplot as plt
url = "D:/3xi mp laporan/m2/Data Nilai.xlsx"
df=pd.read_excel(url)

while True:
    print('')
    print('---------------------------- Pilih 1 - 9 sesuai kebutuhan ----------------------------')
    print('--------------------------------------------------------------------------------------')
    print('1. Load data excel')
    print('2. Load data dengan kolom (No, Nama, Alamat, Mapel MAT )')
    print('3. Menginformasikan  data nilai (mean, max, min)')
    print('4. Menginformasikan rata-rata nilai per siswa dan memberikan status kelulusan')
    print('5. Memberikan grade nilai mapel MAT (Sangat Kurang, Kurang, Cukup, Baik, Sangat Baik)')
    print('6. Merangking dari mapel yang sudah diberi gradenya (1 mapel di point 5)')
    print('7. Membuat Grafik Batang untuk memvisualkan data nilai rata-rata mapel.')
    print('8. Membuat Sebaran Nilai (Histogram) untuk memvisualkan data nilai salah satu mapel')
    print('9. Keluar')

    pilihan=int(input('Pilihan: '))

    if (pilihan==1):
        print(df)
    elif (pilihan==2):
        print(df[['No', 'Nama', 'Alamat', 'MAT']])

    elif (pilihan==3):
        print('Nilai rata rata setiap mapel')
        print('----------------------------')
        meann=df[['MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika']].mean()
        print(meann)
        print('')

        print('Nilai maksimal setiap mapel')
        print('----------------------------')
        maxx=df[['MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika']].max()
        print(maxx)
        print('')

        print('Nilai minimal setiap mapel')
        print('----------------------------')
        minn=df[['MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika']].min()
        print(minn)
        print('')

    elif (pilihan==4):
        df['Rata']=df[['MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika']].mean(axis=1)
        hasil_rata=df[['No', 'Nama', 'MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika', 'Rata']].round(2)
        print('')

        def cek_status(ket):
            if(ket>=70):
                return("Lulus")
            else:
                return("Tidak Lulus")
        hasil_rata["Status"]=hasil_rata['Rata'].apply(cek_status)
        print(hasil_rata)

    elif (pilihan==5):
        def cek_status(ket):
            if(ket<=50):
                return("Sangat Kurang")
            elif(ket < 70):
                return('Kurang')
            elif(ket < 80):
                return('Cukup')
            elif(ket <= 90):
                return('Baik')
            else:
                return("Sangat Baik")

        MAT=df[['No', 'Nama', 'Alamat', 'MAT']].round(2)
        MAT["Status"]=MAT['MAT'].apply(cek_status)
        print(MAT)

    elif (pilihan==6):
        def cek_status(ket):
            if(ket<=50):
                return("Sangat Kurang")
            elif(ket < 70):
                return('Kurang')
            elif(ket < 80):
                return('Cukup')
            elif(ket <= 90):
                return('Baik')
            else:
                return("Sangat Baik")

        MAT=df[['No', 'Nama', 'Alamat', 'MAT']].round(2)
        MAT["Status"]=MAT['MAT'].apply(cek_status)

        df_sort=MAT.sort_values(['MAT'], ascending=False).head(35)
        print(df_sort)

    elif (pilihan==7):
        mean=df[['MAT', 'Bhs Ing', 'Bhs Ind', 'Informatika']].mean()
        mean.plot(kind='bar', color='skyblue', title='Nilai Rata-Rata Mapel')
        plt.xlabel('Mata Pelajaran')
        plt.ylabel('Rata-rata Nilai')
        plt.show()
        print('Nilai Rata-Rata Mapel')
        print(mean)

    elif (pilihan==8):
        Histogram=df[['MAT']]
        plt.hist(df['MAT'], bins=5, color='pink', edgecolor='pink')
        plt.title('Sebaran Nilai MAT')
        plt.xlabel('Nilai MAT')
        plt.ylabel('Jumlah')
        plt.show()

    elif (pilihan==9):
        print('Terima Kasih! Progam Selesai.')
        break

    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-8.")