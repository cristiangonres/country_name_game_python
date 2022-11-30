country_in_list = []
country_in = ""

def eliminar_tildes(li):
    li = li.replace('á', 'a')
    li = li.replace('é', 'e')
    li = li.replace('í', 'i')
    li = li.replace('ó', 'o')
    li = li.replace('ú', 'u')
    return li

def load_countries():
    country_list = []
    data = open('countries.txt','r')
    data.readline()
    for li in data:
        country_list.append(eliminar_tildes (li.lower().strip()))
    country_list = set(country_list)    
    data.close()
    return country_list

def points(country_in, country_list):
    point = 0
    country_in = set( country_in )
    print("Tus países introducidos:")
    print(country_in) 
    for countrin in country_in:
        for countrli in country_list:
            if countrin == countrli:
                point += 1
    return print(f'Tu puntuación es de {point} puntos')
                



country_in = eliminar_tildes(input("Introduzca nombre de país en castellano separados por coma: ").lower().strip())
country_in = sorted(country_in.split(","))


points(country_in, load_countries())
            
