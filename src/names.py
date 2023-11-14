import csv
from typing import NamedTuple, List

NameFreq = NamedTuple("NameFreq",[("year",int),("name",str),("frequency", int),("gender",str)])


#EXCERCISE 1    
def read_names_freq(filename:str) -> List[NameFreq]:
    with open(filename, encoding=True) as file:
        archivo = csv.reader(file)
        next(archivo)
        lista = [NameFreq(int(year),name,int(frequency),gender) for year,name,frequency,gender in archivo]
        return lista

#EXCERCISE 2


