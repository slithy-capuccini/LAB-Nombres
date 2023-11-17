import csv
from typing import NamedTuple, List, Optional, Set

NameFreq = NamedTuple("NameFreq",[("year",int),("name",str),("frequency", int),("gender",str)])


#EXCERCISE 1    
def read_names_freq(filename:str) -> List[NameFreq]:
    with open(filename) as file:
        archivo = csv.reader(file)
        next(archivo)
        lista = [NameFreq(int(year),name,int(frequency),gender) for year,name,frequency,gender in archivo]
        return lista

#EXCERCISE 2
def filter_gender(names: List[NameFreq], g:str) -> List[NameFreq]:
    if g in ["Hombre", "Mujer"]:
        return [s for s in names if s.gender == g]
    

#EXCERCISE 3
def get_names(names: List[NameFreq], g:Optional[str]=None) -> Set[str]:
    return {s.name for s in names if g==None or s.gender==g}
    
#EXERCISE 4
def got_top_n_year(names: List[NameFreq], year: int, limit:int=10, g:Optional[str]=None) -> List[Tuple[str,int]]:
    

