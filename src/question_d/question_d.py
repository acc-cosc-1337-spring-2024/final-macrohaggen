#write functions here, don't add input('') statements here!
import textwrap
def create_multiplication_table():
    listMaster = []
    i=1
    while i != 6:
        j=1
        while j !=11:
            listMaster.append(i*j)
            j+=1
        i+=1
    return listMaster
def display_multiplication_table(listo):
    lista = listo.copy()
    liste = []
    while len(lista) >= 10:
        liste.append(lista[0:0+10])
        del lista[0:0+10]
    stro = ''.join(str(liste[0]).replace(",",' ').replace("[",'').replace("]",''))
    stra = ''.join(str(liste[1]).replace(",",'').replace("[",'').replace("]",''))
    stri = ''.join(str(liste[2]).replace(",",'').replace("[",'').replace("]",''))
    stru = ''.join(str(liste[3]).replace(",",'').replace("[",'').replace("]",''))
    stry = ''.join(str(liste[4]).replace(",",'').replace("[",'').replace("]",''))
    stre = stro + '\n' + stra + '\n' + stri + '\n' + stru + '\n' + stry
    return stre
     