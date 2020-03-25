MAX_LOKER = 0
jumlah_loker = 0
no_loker = 0
data_loker = []

def isKuotaFull(jumlah_loker, MAX_LOKER):
    return jumlah_loker == MAX_LOKER

while True:
    command = input().split()
    type_input = command[0]

    if type_input == 'init':
        MAX_LOKER = int(command[1])
    
    if type_input == 'input':
        if not isKuotaFull(jumlah_loker, MAX_LOKER):
            no_loker = len(data_loker) + 1
            jumlah_loker += 1

            tipe_identitas = command[1]
            nomor_identitas = int(command[2])
            data = [no_loker, tipe_identitas, nomor_identitas]
            data_loker.append(data)

            print(f"Kartu identitas tersimpan di loker nomor {no_loker}")
        else:
            print("Maaf loker sudah penuh.")

    if type_input == 'exit':
        break

