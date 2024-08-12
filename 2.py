import os
os.system("cls")
def eng_qimmat_mahsulotlar(son, mahsulotlar):
  eng_qimmatlar = []
  mahsulotlar.sort(key=lambda x: x['narx'], reverse=True)
  for mahsulot in mahsulotlar:
    if mahsulot['narx'] <= son and len(eng_qimmatlar) < 2:  
      eng_qimmatlar.append(mahsulot)
      son -= mahsulot['narx']
  return eng_qimmatlar

mahsulotlar = [
    {"nom": "non", "narx": 100},
    {"nom": "vino", "narx": 138},
    {"nom": "go'sht", "narx": 15},
    {"nom": "suv", "narx": 1},
]
pul = 500
eng_qimmat = eng_qimmat_mahsulotlar(pul, mahsulotlar)

if eng_qimmat:
  print("Eng qimmat mahsulotlar:", eng_qimmat)
else:
  print("Pul miqdoriga mos mahsulot topilmadi.")
