import os
os.system("cls")
def raqamlarni_sanash(son):
  raqamlar_soni = {}
  while son > 0:
    raqam = son % 10
    if raqam in raqamlar_soni:
      raqamlar_soni[raqam] += 1
    else:
      raqamlar_soni[raqam] = 1
    son //= 10
  sorted_raqamlar_soni = dict(sorted(raqamlar_soni.items()))
  return sorted_raqamlar_soni
son = int(input("son kiriting: "))
hisob = raqamlarni_sanash(son)
for raqam, soni in hisob.items():
  print(f"{raqam} dan {soni} ta")
