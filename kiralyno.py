# lehetséges e 8 kiráynnőt lehelyezni a sakktáblán úgy hogy nem ütik egymást?

def megoldas_kereso(n):

    # sor ellenőrzés balra
    def biztonsagos(tabla,sor,oszlop):
        for i in range(oszlop):
            if tabla[sor][i] == 1:
                return False
            
    #bal felső átló
        i = sor
        j = oszlop
        while i >= 0 and j >= 0:
            if tabla[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i = sor
        j = oszlop
        while i<n and j >= 0:
            if tabla[i][j] == 1:
                
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def megoldas_seged(tabla, oszlop, megoldasok):

        #alapfeltétel, egy kilépési feltétel ami megállítja a rekurziót

        if oszlop >= n:
            megoldas = []
            for i in range(n):
                for j in range(n):
                    if tabla[i][j] == 1:
                        megoldas.append(j)

            megoldasok.append(megoldas)
            return
        
        # proóbáljuk letenni a kiráynőt
        for i in range(n):
            if biztonsagos(tabla, i, oszlop):
                tabla[i][oszlop] = 1

                #rekurzió hívás a következő oszlopra
                megoldas_seged(tabla,oszlop+1,megoldasok)
                #levesszük a kiránynőt ha nem jó helyen van
                tabla[i][oszlop] = 0

    megoldasok = []
    tabla = [[0]*n for _ in range(n)]
    megoldas_seged(tabla, 0, megoldasok)

    return megoldasok

def kirajzolni(megoldasok):
    rajz = []

    for i in range(meret):
        rajz_sor = []
        for j in range(meret):
            if j == megoldasok[i]:
                rajz_sor.append("X")
            else: 
                rajz_sor.append(".")
        rajz.append(rajz_sor)

    for __ in range(meret):
        print(rajz[__])


meret = 8
megoldasok = megoldas_kereso(meret)
if megoldasok:
    print(f"Megoldás: {megoldasok[0]}")
    kirajzolni(megoldasok[0])
