MAX_LOKER = 0
jumlah_loker = 0
no_loker = 0
data_loker = []

def isKuotaFull(jumlah_loker, MAX_LOKER):
    return jumlah_loker == MAX_LOKER

def show_data(data_loker):
    header = "No Loker      Tipe Identitas        Nomor Identitas"
    print(header)
    for data in data_loker:
        nomor, tipe_id, nomor_id = data
        row = f"{nomor}             {tipe_id}                   {nomor_id}"
        print(row)

def find_loker(data_loker, nomor):
    for data in data_loker:
        if nomor == int(data[2]):
            return int(data[0])
    return -1

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

    if type_input == 'status':
        show_data(data_loker)

    if type_input == 'leave':
        jumlah_loker -= 1
        index = int(command[1]) - 1
        data_loker.remove(data_loker[index])
        print(f"Loker nomor {index + 1} berhasil dikosongkan.")

    if type_input == 'find':
        lokasi_loker = find_loker(data_loker, int(command[1]))
        if lokasi_loker > 0:
            print(f"Kartu identitas tersimpan di loker nomor {lokasi_loker}")
        else:
            print(f"Kartu identitas tidak ditemukan")

    if type_input == 'exit':
        break

