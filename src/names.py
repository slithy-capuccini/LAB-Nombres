import csv
from typing import NamedTuple, List, Optional, Set, Tuple, Dict
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

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
    selection=[nq for nq in names if nq.year==year and (g==None or nq.gender==g)]
    selection.sort(key=lambda t:t.frequency, reverse=True)
    return [(nf.name,nf.frequency)for nf in selection][:limit]

#EXERCISE 5
def got_common_names(names: List[NameFreq]) -> Set[str]:
    #returns a set with names used for boy and girls
    names_males=set([i.name for i in names if i.gender=="Hombre"])
    names_converge=set([i.name for i in names if i.gender=="Mujer" and i.name in names_males])
    #names_males.intersection(names_females)
    return names_converge

#EXERCISE 6
def get_compound_names(names:List[NameFreq], g:Optional[str]=None)->Set[str]:
    names_compound=set([i.name for i in names if (len(i.name.split())>1) and (g==None or g==names.gender)])
    return names_compound

#EXERCISE 7

#step 1: create a dictionary {year:list of namedtuples of the year}
#step 2:get the max tuple of each list

def most_common_names_per_year(names:List[NameFreq]):
    llaves=set([i.year for i in names])
    my_dict = {key: list() for key in llaves}
    for i in names:
        my_dict[i.year].append(i.name)
    for i in my_dict.keys():
        my_dict[i]=Counter(my_dict[i]).most_common(1)
    return my_dict

#EXERCISE 8
def get_year_frequencies(names:List[NameFreq], name:str)->List[Tuple[int,int]]:
    d=defaultdict(int)
    for nf in names:
        if nf.name==name:
            d[nf.year]+=nf.frequency

    return sorted(d.items())

#EX 9
def show_evolution_year(names:List[NameFreq], name:str)->None:
    years, frequencies=zip(*get_year_frequencies(names,name))
    plt.plot(years,frequencies)
    plt.title(f"Evolcuion nombre {name}")
    plt.show()

#EX 11 AND EX 12
def get_freqs_by_name(nfs:List[NameFreq])->Dict[str,int]:
    d={}
    names= {e.name for e in nfs}
    for nf in names:
        d[nf]=acumulated_frequency(nfs,name=nf)
    return d

def show_names_freqs(nfs:List[NameFreq], limit:int=10)->None:
    acumulated_frecuencies=sorted(get_freqs_by_name(nfs).items(), key=lambda n:n[1], reverse=True)[:limit]
    names, frequencies = zip(*acumulated_frecuencies)

    plt.bar(names,frequencies)
    plt.xticks(rotation=80)
    plt.title(f"Frequency of the top {limit} most common names")
    plt.show()

def acumulated_frequency(nfs: List[NameFreq],name=str)->int:
    return sum(nf.frequency for nf in nfs if name==nf.name)