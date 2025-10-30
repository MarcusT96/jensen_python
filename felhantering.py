

flagga = True

while flagga:

    try: 
        taljare = int(input("Skriv ett tal: "))
        namnare = int(input("Skriv ett till tal tack: "))
        print(taljare / namnare)
    except ZeroDivisionError:
        print("Kan inte dela med 0")
    except ValueError:
        print("Skriv ett heltal")

    finally:
            flagga = False

    

