nume_fisier=input("Nume fisier:")
with open(nume_fisier,'r') as fisier:
    ok=True
    numere = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lastword=''
    cuvant=''
    for caracter in fisier.read():
        #nu luam in considerare semnele de punctuatie
        if  caracter in {'.',',','?','!',',',':','<','>'}:
            continue
        #filtram numerele;nu o sa le afiseze
        if caracter in numere:
            continue
        #verificam spatiile si daca sunt mai multe nu le luam in considerare
        if caracter==' ':
            if (not ok) :
                continue
            #daca intalnim primul spatiu, afisam cuvantul si marcam faptul ca sirul s-a terminat in spatiu
            else:
                print(cuvant,end=' ')
                ok=False
                cuvant=''
                continue
        #inceputul unui cuvant nou, putem avea din nou spatii
        ok=True
        cuvant+=caracter.upper()
#afisam ultimul cuvant citit
if(cuvant):
    print(cuvant)