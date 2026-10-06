#Órai feladat: meg kellett kérdezni az AI, hogy az órán készített program esetében
#mi lehet az az eset, amikor a felhasználó megadja az értéke(ket), de mégsem elégedett
#az eredménnyel. Az alábbiak lehetségesek:
# - a bekért érték alapvetően szöveg, nem ártana hibamentesen konvertálni
# - érdemes lenne a kezdeti XP mellett az különböző lények számát, és az értük járó XP-t is bekérni
# - nem derül ki, hogy mi okozta a szintlépést, melyik lény
# - érdemes lenne figyelni és kiírni, hogy hányadik szintre lépett a karakter
# - további információt is lehet(ne) adni: aktuális XP, szerzett XP, következő szintig szükséges XP

import sys

def get_positive_int(prompt_text: str):
    while True:
        szoveg = input(prompt_text + " (-1 => kilépés): ").strip()
        if szoveg == "-1":
            sys.exit()
        if szoveg.isdigit():
            return int(szoveg)
        print("Hibás érték, próbáld újra!")

def get_level(actual_xp):
    xp_by_level = [700, 1200]
    level = 1
    if actual_xp >= xp_by_level[0]:
        level = 2
    if actual_xp >= xp_by_level[1]:
        level = 3
    return level

def check_xp(get_actual_xp, get_xp):
    old_level = get_level(get_actual_xp)
    new_level = get_level(get_actual_xp + get_xp)
    if new_level > old_level:
        print(f"{new_level}. szintre léptél, az új XP-d:", end="")
    else:
        print(f"{get_xp} XP nem volt elég a szint lépésre, aktuális XP-d:", end="")
    print (get_actual_xp + get_xp, "\n")
    return get_actual_xp + get_xp

kezdo_xp = get_positive_int("Add meg a kezdő XP-t")
goblin_xp = get_positive_int("Add meg a goblinokért járó XP-t")
goblin_db = get_positive_int("Add meg a megölt goblinok számát")
ork_xp = get_positive_int("Add meg az orkokért járó XP-t")
ork_db = get_positive_int("Add meg a megölt orkok számát")

print()

aktual_xp = check_xp(0, kezdo_xp)
print("Csata a goblinokkal, db:",goblin_db, "goblin XP/db:",goblin_xp)
aktual_xp = check_xp(aktual_xp, goblin_xp * goblin_db)
print("Csata az orkokkal, db:", ork_db, "ork XP/db:",ork_xp)
aktual_xp = check_xp(aktual_xp, ork_xp * ork_db)
print('A program vége... köszönjük az együttműködést!')
