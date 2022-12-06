def vlsm():
    ip = ""
    db = 0
    mehet = False
    lista = []
    subnetek = []
    magic_number = []
    alhalozatszam = int(input("Hány darab alhálózatunk lesz (egész szám): "))
    # maszk = input("Milyen osztályú az ip cím: (a, b, c): ")
    ipelso = int(input("Add meg az IP-cím első oktetjét: "))
    ipmaso = int(input("Add meg az IP-cím második oktetjét: "))
    ipharm = int(input("Add meg az IP-cím harmadik oktetjét: "))
    ipnegy = 0

    if 0 <= ipelso <= 255:
        ip += str(ipelso) + "."
        if 0 <= ipmaso <= 255:
            ip += str(ipmaso) + "."
            if 0 <= ipharm <= 255:
                ip += str(ipharm) + "."
                ip += str(ipnegy)
                print("Az IP, amit megadtál:")
                print(ip)
            else:
                mehet = True
                print("Nem jó a harmadik oktet.")
        else:
            mehet = True
            print("Nem jó a második oktet.")
    else:
        mehet = True
        print("Nem jó a első oktet.")

    if mehet:
        print("Nem tud lefutni a program!")
    else:
        for i in range(alhalozatszam):
            halozatszam = int(input("Egy adott host száma: "))
            lista.append(halozatszam)
            db += halozatszam
        lista.sort(reverse=True)
        if db >= 255:
            print("Túl sok az alhálózatok száma!")
        else:
            for i in range(len(lista)):
                k = 0
                while not(lista[i]+2 <= 2 ** k):
                    k += 1
                magic_number.append(2**k)
                subnet_maszk = 32 - k
                subnetek.append(f"/{subnet_maszk}")

            for i in range(alhalozatszam):
                if i == 0:
                    ipcim = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(ipnegy)
                    print(f"Az {lista[i]}. NetID: {ipcim}, a subnet maszk {subnetek[i]}, az első valid IP: {ipnegy+1}, az utolsó kiosztható IP: {ipnegy+magic_number[i]-2}, a Broadcast: {ipnegy+magic_number[i]-1}")
                else:
                    ipnegy = ipnegy+magic_number[i-1]
                    ipcim = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(ipnegy)
                    print(
                        f"Az {lista[i]}. NetID: {ipcim}, a subnet maszk {subnetek[i]}, az első valid IP: {ipnegy + 1}, az utolsó kiosztható IP: {ipnegy + magic_number[i] - 2}, a Broadcast: {ipnegy + magic_number[i] - 1}")


def subnetkereses():
    szoveg = ""
    maszk = int(input("Mi az új maszk: "))
    ipelso = int(input("Add meg az IP-cím első oktetjét: "))
    szoveg += str(ipelso) + "."
    ipmaso = int(input("Add meg az IP-cím második oktetjét: "))
    szoveg += str(ipmaso) + "."
    ipharm = int(input("Add meg az IP-cím harmadik oktetjét: "))
    szoveg += str(ipharm) + "."
    ipnegy = int(input("Add meg az IP-cím negyedik oktetjét: "))
    szoveg += str(ipnegy)
    if 0 < ipelso <= 127:
        ssz = 8
        szubnetbitek = maszk - ssz
        alhalozat = 2 ** szubnetbitek
        hostokbitek = 32 - maszk
        hostok = 2 ** hostokbitek - 2
        print("\n" + szoveg)
        print(
            f"\nA subnet bitek száma: {szubnetbitek}\nAz alhálózatok száma: {alhalozat}\nA host bitek száma: {hostokbitek}\nA hostok száma alhálózatonként: {hostok}")

        magic = round(2 ** hostokbitek / 256)
        kezdo = 0
        while not (ipmaso < (kezdo + magic)):
            kezdo = kezdo + magic
        print("\nMagic Number:", magic)
        ipkezdo = str(ipelso) + "." + str(kezdo) + "." + str(0) + "." + str(0)
        elso = kezdo
        elsoip = str(ipelso) + "." + str(elso) + "." + str(0) + "." + str(1)
        utolso = kezdo + magic - 1
        utolsoip = str(ipelso) + "." + str(utolso) + "." + str(255) + "." + str(254)
        broad = kezdo + magic - 1
        broadip = str(ipelso) + "." + str(broad) + "." + str(255) + "." + str(255)
        print(f"NetID: {ipkezdo}\nElső valid IP: {elsoip}\nUtolsó valid IP: {utolsoip}\nBroadcast: {broadip}")

    elif 128 <= ipelso <= 191:
        ssz = 16
        # teljes ip szamot osztunk 256
        szubnetbitek = maszk - ssz
        alhalozat = 2 ** szubnetbitek
        hostokbitek = 32 - maszk
        hostok = 2 ** hostokbitek - 2
        print("\n" + szoveg)
        print(
            f"\nA subnet bitek száma: {szubnetbitek}\nAz alhálózatok száma: {alhalozat}\nA host bitek száma: {hostokbitek}\nA hostok száma alhálózatonként: {hostok}")
        print(hostokbitek)
        magic = round(2 ** hostokbitek / 256)
        kezdo = 0
        while not (ipharm < (kezdo + magic)):
            kezdo = kezdo + magic
        print("\nMagic Number:", magic)
        ipkezdo = str(ipelso) + "." + str(ipmaso) + "." + str(kezdo) + "." + str(0)
        elso = kezdo
        elsoip = str(ipelso) + "." + str(ipmaso) + "." + str(elso) + "." + str(1)
        utolso = kezdo + magic - 1
        utolsoip = str(ipelso) + "." + str(ipmaso) + "." + str(utolso) + "." + str(254)
        broad = kezdo + magic - 1
        broadip = str(ipelso) + "." + str(ipmaso) + "." + str(broad) + "." + str(255)
        print(f"NetID: {ipkezdo}\nElső valid IP: {elsoip}\nUtolsó valid IP: {utolsoip}\nBroadcast: {broadip}")

    elif 192 <= ipelso <= 223:
        ssz = 24
        szubnetbitek = maszk - ssz
        alhalozat = 2 ** szubnetbitek
        hostokbitek = 32 - maszk
        hostok = 2 ** hostokbitek - 2
        print("\n" + szoveg)
        print(
            f"\nA subnet bitek száma: {szubnetbitek}\nAz alhálózatok száma: {alhalozat}\nA host bitek száma: {hostokbitek}\nA hostok száma alhálózatonként: {hostok}")

        magic = 2 ** hostokbitek
        kezdo = 0
        while not (ipnegy < (kezdo + magic)):
            kezdo = kezdo + magic
        print("\nMagic Number:", magic)
        ipkezdo = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(kezdo)
        elso = kezdo + 1
        elsoip = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(elso)
        utolso = kezdo + magic - 2
        utolsoip = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(utolso)
        broad = kezdo + magic - 1
        broadip = str(ipelso) + "." + str(ipmaso) + "." + str(ipharm) + "." + str(broad)

        print(f"NetID: {ipkezdo}\nElső valid IP: {elsoip}\nUtolsó valid IP: {utolsoip}\nBroadcast: {broadip}")

    else:
        print("A megadott első oktetbeni szám se nem a, se nem b, se nem c osztályú.")
