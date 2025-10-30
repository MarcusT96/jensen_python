def menu(cars):
    while True:
        print("1) Lista  2) Starta  3) Accelerera  4) Underhåll  0) Avsluta")
        choice = input("> ")

        if choice == "1":
            for i, c in enumerate(cars, 1):
                print(i, c.get_status())

        elif choice == "2":
            try:
                i = int(input("Bilnummer: ")) - 1
                print(cars[i].start_engine())
            except ValueError:
                print("Ogiltig inmatning. Ange ett heltal.")
            except IndexError:
                print(f"Numret finns inte. Välj 1–{len(cars)}.")

        elif choice == "3":
            try:
                i = int(input("Bilnummer: ")) - 1
                inc = int(input("Öka hastighet: "))
                print(cars[i].accelerate(inc))
            except ValueError:
                print("Ogiltig inmatning. Ange ett heltal.")
            except IndexError:
                print(f"Numret finns inte. Välj 1–{len(cars)}.")

        elif choice == "4":
            try:
                i = int(input("Bilnummer: ")) - 1
                if not cars[i].parts_needing_maintenance:
                    print("Inga delar i underhållslistan.")
                    continue
                print("Delar:", cars[i].parts_needing_maintenance)
                idx = int(input("Vilken del (1-baserat)? "))
                print(cars[i].perform_maintenance_on_part_by_index(idx))
            except ValueError:
                print("Ogiltig inmatning. Ange ett heltal.")
            except IndexError:
                print(f"Numret finns inte. Välj 1–{len(cars)}.")

        elif choice == "0":
            break
        else:
            print("Okänt val.")
