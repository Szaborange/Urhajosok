import csv


def maxkereso(d):
    haromhonap = []
    szazalekok = []
    ossz = sum(d)
    honapok = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember",
               "Október", "November", "December"]
    for a in range(3):
        maxim = max(d)
        haromhonap.append(honapok[d.index(maxim)])
        d[d.index(maxim)] = 0
        szazalekok.append(maxim / ossz * 100)

    return haromhonap, szazalekok


def main():
    print("Ez a program egy űrhajósokról szóló csv fájl segítségével meghatározza a 3 leggyakoribb születési hónapot "
          "(százalékos aránnyal is) az űrhajósok körében.")
    with open("astronauts.csv", "r") as csv_file:
        adatok = csv.reader(csv_file)

        datumok = []
        for sor in adatok:
            if sor[4] != "Birth Date":
                datumok.append(int(sor[4].split("/")[0]))

        darab = []
        for i in range(1, 13):
            darab.append(datumok.count(i))

        tuplee = maxkereso(darab)
        for e in range(3):
            print(f"A(z) {e+1}. leggyakoribb születési hónap a(z) {tuplee[0][e]}, {tuplee[1][e]:.1f}%-kal.")


main()
