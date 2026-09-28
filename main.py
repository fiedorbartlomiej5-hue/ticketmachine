# Import bibliotek 
import json
import time 

# stałe 
PROMPT = "Twój wybór:"
ERROR_MSG = "Niepoprawny wybór, spróbuj ponownie."

#1. Wczytaj dane z pliku princes.json i zapisz je do zmiennej  jako słownik/dictionary
with open("./princes.json", "r", encoding="utf-8") as jf: 
    princes = json.load(f)

#2. Utwórz pusty koszyk jako listę
cart = []
end = False

while not end:
    # 3. Wyświetl użytkownikowi menu główne 
    print("""Wybierz jedną z opcji:\n1 - dodaj bilet\n2 - pokaż koszyk\n3 - zapłać\n4 - zakończ program")

    # 4. Pobierz jeden znak od użytkownika
    option = input(PROMPT)[0]

    match option:
        case "1":
            ticket = {}
            while True:
                # 5.1. Wyświetl typ biletu
                print("Wybierz typ biletu:\nn - normalny\nu - ulgowy")

                # 6.1. Pobierz jeden znak od użytkownika
                ticket1 = input(PROMPT)[0]

                # 7.1. Na podstawie wyboru określ rodzaj biletu i zapisz go do słownika ticket pod kluczem "discount"
                if ticket1 == "n":
                    ticket["discount"] = "normalny"
                    break
                elif ticket1 == "u":
                    ticket["discount"] = "ulgowy"
                    break 
                elif ticket1 == "p":
                    break
                elif ticket1 == "k":
                    exit()
                else:
                    print(ERROR_MSG)
            if not ticket:
                continue

            cont = True
            while True:
                # 8.1 Wyświetl rodzaj biletu
                print("Wybierz typ biletu:\no - okresowy\nc - czasowy\nj - jednorazowy")
                # 9.1 Pobierz jeden znak od użytkownika
                ticket2 = input(PROMPT)[0]

                if ticket2 == "o":
                    ticket["type"] = "okresowy"
                    while True:
                        # 10.1.1 Wyświetl dostępne opcje z pliku JSON
                        print("Wybierz okres ważności biletu:\n1 - półroczny\n2 - miesięczny\n3 - tygodniowy\n4 - jednodniowy")
                        # 11.1.1 Pobierz jeden znak od użytkownika
                        ticket3 = input(PROMPT)[0]
                        match ticket3:
                            case "1":
                                ticket["validity"] = "półroczny"
                                break
                            case "2":
                                ticket["validity"] = "miesięczny"
                                break
                            case "3":
                                ticket["validity"] = "tygodniowy"
                                break
                            case "4":
                                ticket["validity"] = "jednodniowy"
                                break
                            case "p":
                                cont = False
                                break
                            case "k":
                                exit()
                            case _:
                                print(ERROR_MSG)
                    if not cont:
                        break
                    break

                elif ticket2 == "c":
                    ticket["type"] = "czasowy"
                    while True:
                        # 10.1.2 Wyświetl dostępne opcje z pliku JSON
                        print("Wybierz czas ważności biletu:\n1 - 60 minut\n2 - 30 minut\n3 - 10 minut")
                        # 11.1.2 Pobierz jeden znak od użytkownika
                        ticket3 = input(PROMPT)[0]
                        match ticket3:
                            case "1": 
                                ticket["validity"] = "60 minut"
                                break
                            case "2": 
                                ticket["validity"] = "30 minut"
                                break
                            case "3": 
                                ticket["validity"] = "10 minut"
                                break
                            case "p":
                                cont = False
                                break
                            case "k":
                                exit()
                            case _:
                                print(ERROR_MSG)
                    if not cont:
                        break
                    break
                elif ticket2 == "j":
                    ticket["type"] = "jednorazowy"
                    while True:
                        # 10.1.3 Wyświetl dostępne opcje z pliku JSON
                        print("Wybierz czas ważności biletu:\n1 - miejski\n2 - aglomeracyjny")
                        # 11.1.3 Pobierz jeden znak od użytkownika
                        ticket3 = input(PROMPT)[0]
                        match ticket3:
                            case "1": 
                                ticket["validity"] = "miejski"
                                break
                            case "2": 
                                ticket["validity"] = "aglomeracyjny"
                                break
                            case "p":
                                cont = False
                                break
                            case "k":
                                exit()
                            case _:
                                print(ERROR_MSG)
                    if not cont:
                        break
                    break
                elif ticket2 == "p":
                    cont = False
                    break
                elif ticket2 == "k":
                    exit()
                else:
                    print(ERROR_MSG)
            if not cont:
                continue

            # 12.1 Na podstawie wyboru odczytaj cenę z cennika


