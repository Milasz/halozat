import random


class BColors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def gyakorlas():
    portok = [
        ("File Transfer Protocol (FTP) - Adat", 20),
        ("File Transfer Protocol (FTP) - Vezérlés", 21),
        ("Secure Shell (SSH)", 22),
        ("Telnet", 23),
        ("Simple Mail Transfer Protocol (SMTP)", 25),
        ("Domain Name System (DNS)", 53),
        ("Dynamic Host Configuration Protocol (DHCP) - Kiszolgáló", 67),
        ("Dynamic Host Configuration Protocol - Ügyfél", 68),
        ("Trivial File Transfer Protocol (TFTP)", 69),
        ("Hypertext Transfer Protocol (HTTP)", 80),
        ("Post Office Protocol version 3 (POP3)", 110),
        ("Internet Message Access Protocol (IMAP)", 143),
        ("Simple Network Management Protocol (SNMP)", 161),
        ("Hypertext Transfer Protocol Secure (HTTPS)", 443)
    ]
    random.shuffle(portok)
    helyes = 0
    for (port, szam) in portok:
        print(port, "\nMelyik a porton van?")
        teszt = int(input("Válaszod: "))
        if teszt == szam:
            print(BColors.OKGREEN + "A válaszod helyes!" + BColors.ENDC)
            helyes += 1
        else:
            print(BColors.FAIL + "Nem lett jó a válaszod, a helyes válasz:" + BColors.ENDC, BColors.OKGREEN + str(szam) + BColors.ENDC)

    print("Helyes válaszaid száma:", helyes)
    if helyes < 7:
        print("Ez 1-es lett.")
    elif 7 <= helyes < 8:
        print("Ez 2-es lett.")
    elif 8 <= helyes < 10:
        print("Ez 3-as lett.")
    elif 10 <= helyes < 12:
        print("Ez 4-es lett.")
    elif 12 <= helyes < 15:
        print("Ez 5-ös lett.")
    else:
        print("Ne csaljá vazze!")
