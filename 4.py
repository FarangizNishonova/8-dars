import os
os.system("cls")
def klaviatura_belgilari(fayl_nomi):
    chap_qol = set('qwertyuiopQWERTYUIOP')
    ong_qol = set('asdfghjklzxcvbnmASDFGHJKLZXCVBNM')
    chap_qol_soni = 0
    ong_qol_soni = 0
    try:
        with open(fayl_nomi, 'r') as f:
            matn = f.read()
            for belgi in matn:
                if belgi in chap_qol:
                    chap_qol_soni += 1
                elif belgi in ong_qol:
                    ong_qol_soni += 1
    except FileNotFoundError:
        print(f"Fayl '{fayl_nomi}' topilmadi.")
        return [0, 0]
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return [0, 0]

    return [chap_qol_soni, ong_qol_soni]
fayl_nomi = "matn.txt"  
natija = klaviatura_belgilari(fayl_nomi)
print("Chap qo'l belgilar soni:", natija[0])
print("O'ng qo'l belgilar soni:", natija[1])
