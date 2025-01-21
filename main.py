"""
Téma rybaření

Aplikace, kde si uživatel může zapisovat své úlovky, Třída ryby s metodami - Vyhledávání podle názvu, seřazení podle velikosti ryb = graficky zobrazit své úlovky
"""
import json
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np


# V procesu 
def registrace(jmeno, heslo):
    with open("prihlasovaci_udaje.txt", "a") as file:
        file.write(f"{jmeno}:{heslo}\n")
    print("Registrace úspěšná!")

def prihlaseni():
    zadane_jmeno = str(input("Zadej své jméno: "))
    zadane_heslo = str(input("Zadej své heslo: "))
    



# Nedokážu se řídit podle diagramu, takže možná bude výsledný program vypadat jinak






List_ulovenych_ryb = []
# Slovnik_ulovenych_ryb = {}

while True:

    otazka = int(input("Vítej ve svém zápisníku ryb, co si přeješ udělat? (1 = Přidat rybu, 2 = Odstanit rybu, 3 = Vyhledat rybu, 4 = Vypsat ryby podle velikosti, 5 = Zobrazit graf) "))

    class Ryba:
        def __init__(self, nazev, velikost):
            self.nazev = nazev
            self.velikost = velikost


        
        def pridat_rybu(self):
            # Otevře soubor ke čtení
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)

            # Vypíše zapsané ryby
            print("Toto jsou tvé aktuálně zapsané ryby")

            # Projde každou hodnotu jsonu
            for ryby in Slovnik_ulovenych_ryb.values():
                # Projde přes hodnotu (Název ryby) k jejím vlatnostem
                for ryba in ryby:
                    print(f"Ryba: {ryba["Název"]}, Velikost: {ryba["Velikost"]}")
            
            # Uživatel zadá parametry ryby
            Nazev_ryby = str(input("Jaký je název ryby? "))
            Velikost_ryby = int(input("Jak byla tato ryba velká?(cm) "))
            Prvni_ryba = Ryba(Nazev_ryby, Velikost_ryby)

            # Opět načtení jsonu
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)
            

            # Do jsonu se přidá Nazev_ryby = prázdnej seznam, pokud tam již není
            if Nazev_ryby not in Slovnik_ulovenych_ryb:
                Slovnik_ulovenych_ryb[Nazev_ryby] = []

                # Do jsonu se do listu Nazev_ryby(ryba) přidá Název a Velikost ryby
                Slovnik_ulovenych_ryb[Nazev_ryby].append({
                    "Název": Nazev_ryby,
                    "Velikost": Velikost_ryby
                })

                # Vepsání nové ryby do souboru
                # Indent = odsazení
                with open("ryby.json", "w") as outfile:
                    json.dump(Slovnik_ulovenych_ryb, outfile, indent=4)

                # Oznámení uživateli o zapsání
                print(f"Ryba s názvem {Nazev_ryby}, která byla {Velikost_ryby} cm velká byla zapsána do tvého deníku.\n")
                
                return Prvni_ryba
            
            # Nesplnění podmínky, že ryba nesmí být už v seznamu
            else:
                print(f"Taková ryba už je zapsána, zkus například {Nazev_ryby}_NějakéČíslo.\n")


        



        def odstranit_rybu(self):
            # Načtení jsonu
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)

            # Vypíše ryby z jsonu
            print("Toto jsou tvé aktuálně zapsané ryby")
            for ryby in Slovnik_ulovenych_ryb.values():
                # ryba = seznam vlastností každé z ryb
                for ryba in ryby:
                    
                    # ze seznamu ryba vezme položku Název a místo ní dá hodnotu názvu (název ryby)
                    print(f"Ryba: {ryba["Název"]}, Velikost: {ryba["Velikost"]}")

            # Uživatel napíše název ryby
            jakou_rybu_odstranit = str(input("Jakou z uvedených ryb chceš odstranit? "))
            if jakou_rybu_odstranit in Slovnik_ulovenych_ryb.keys():
                # Jestliže je jedním z klíčů v jsonu, ryba se odstraní
                del Slovnik_ulovenych_ryb[jakou_rybu_odstranit]
                # Aktualizuje se json
                with open("ryby.json", "w") as outfile:
                    json.dump(Slovnik_ulovenych_ryb, outfile, indent=4)
                print(f"Ryba s názvem {jakou_rybu_odstranit} byla odstraněna z tvého deníku.")
            else:
                # Špatně napsaná ryba/Není jedním z klíčů
                print("Takovou rybu nemáš zapsanou.")
            
        # def info(self

    class Blok:
        def __init__(self, nazev, velikost):
            self.nazev = nazev
            self.velikost = velikost
        
        def Vyhledat_rybu(self):
            # Otevře soubor ke čtení
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)
            vyhledavana_ryba = str(input("Jakou rybu si přeješ vyhledat? "))
            if vyhledavana_ryba in Slovnik_ulovenych_ryb.keys():
                print("Takovou rybu máš už ve svém deníčku.")
            else:
                print("Takovou rybu jsi ještě nechytil.")

        def seradit_ryby(self):
            # Otevře soubor ke čtení
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)
                #Vezme se první věc ze seznamu (value) a vezme se z něj Název ryby, za něj velikost ryby
            ryby = [(hodnota[0]['Název'], hodnota[0]['Velikost']) for hodnota in Slovnik_ulovenych_ryb.values()]
            #Ryby se seřadí od největšího po nejmenší (pomocí reverse=True)
            serazene_ryby = sorted(ryby, key = itemgetter(1), reverse=True)
            print(', '.join(f"{nazev} {velikost} cm" for nazev, velikost in serazene_ryby))

    class Graf:
        def __init__(self, nazev, velikost):
            self.nazev = nazev
            self.velikost = velikost


        def graf(self):
            with open("ryby.json", "r") as openfile:
                Slovnik_ulovenych_ryb = json.load(openfile)

            # Vezme první (a jedinou) položku v seznamu v jsonu a z hodnoty "Velikost" vezme číslo
            Velikosti_ryb_list = [(hodnota[0]["Velikost"]) for hodnota in Slovnik_ulovenych_ryb.values()]
            # Vezme první (a jedinou) položku v seznamu v jsonu a z hodnoty "Název" vezme název ryby
            Nazvy_ryb_list = [(hodnota[0]["Název"]) for hodnota in Slovnik_ulovenych_ryb.values()]

            #Sloupcový graf
            plt.bar(Nazvy_ryb_list, Velikosti_ryb_list)
            plt.show()

        

    Pridana_ryba = Ryba("Nazev ryby", 0)
    Hledana_ryba = Blok("Nazev ryby", 0)
    Velikosti_ryb = Blok("Nazev ryby", 0)
    Zobrazit_graf = Graf("Nazev ryby", 0)

    # prvni_ryba_instance = Pridana_ryba.pridat_rybu()
    if otazka == 1:
        prvni_ryba_instance = Pridana_ryba.pridat_rybu()
    if otazka == 2:
        prvni_ryba_instance = Pridana_ryba.odstranit_rybu()
    if otazka == 3:
        prvni_ryba_instance = Hledana_ryba.Vyhledat_rybu()
    if otazka == 4:
        prvni_ryba_instance = Velikosti_ryb.seradit_ryby()
    if otazka == 5:
        prvni_ryba_instance = Zobrazit_graf.graf()



    
