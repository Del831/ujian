def main():
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    nama = input("Masukkan Nama Anda: ")
    npm = input("Masukkan NPM Anda: ")

    with open("MarMaterial.txt", "w", encoding="utf-8") as fileku:
        fileku.write(f'\t\tToko Perkakas\n') 
        fileku.write(f'\tMontlhy summary \n')
        fileku.write(f'Order #1\n')
        fileku.write(f'Monday, 2 Desember 2024\n')
        fileku.write(f'===================================================\n')
        fileku.write(f'QTY item                                   AMT (RP)\n')
        fileku.write(f'===================================================\n')

        for i in range(jumlah_barang):
            nama_barang = input(f"Masukkan Nama Barang{i + 1}:")
            jumlah_barang = int(input(f'Masukan Jumlah barang {i+1}:'))
            harga_barang = int(input(f'Masukkan Harga barang {i+1}:'))
            
            fileku.write(f'{i+1} {jumlah_barang} {nama_barang} {harga_barang * jumlah_barang}\n') 

            
        fileku.write(f'==================================================\n')
        fileku.write(f'Material Count:                    {jumlah_barang}\n')
        fileku.write(f'Total Material:     {harga_barang * jumlah_barang }\n')
        fileku.write(f'==================================================\n')
        fileku.write(f'Card#: PERK12345\n                                  ')
        fileku.write(f'NPM Anda: {npm}\n                                   ')
        fileku.write(f'Nama Anda: {nama}\n                                 ')
        fileku.write(f'                 Thank You                        \n')
        fileku.write(f'          For Using This Program                  \n')

if __name__ == "__main__":
    main()
