from names import *

def main():
    names_freq = read_names_freq("./data/frecuencias_nombres.csv")
    print(f"we have {len(names_freq)} names frequency")
    print(f"First name and year {names_freq[0]}")

    male_freqs = filter_gender(names_freq, "Hombre")
    print(f"Hay una frecuencia de {len(male_freqs)} nombres")
    name_woman = get_names(names_freq, "Mujer")
    print(f"Hay {len(name_woman)}")
    names_top=got_top_n_year(names_freq,2014,15)
    print(f"{names_top}")
    print(f"Names that converges are {got_common_names(names_freq)}")
    print(f"The compound names are {get_compound_names(names_freq)}")
    most_common_names_per_year(names_freq)
    print(get_year_frequencies(names_freq, "HUGO"))
if __name__ == "__main__":
    main()