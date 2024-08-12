import os
os.system("cls")
def boshdagi_nollar_soni(son):
  nol_soni = 0
  for i in range(len(son)):
    if son[i] == '0':
      nol_soni += 1
    else:
      break  
  return nol_soni
son = input("son kiriting:")
nol_soni = boshdagi_nollar_soni(son)
print(f"{son} sonining boshida {nol_soni} ta nol bor.")
