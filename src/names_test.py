from names import *

def main():
    names_freq = read_names_freq("./data/frecuencias_nombres.csv")
    print(f"we have {len(names_freq)} names frequency")
    print(f"First name and year {names_freq[0]}")

    male_freqs = filter_gender(names_freq, "Hombre")
    print(f"Hay una frecuencia de {len(male_freqs)} nombres")
    name_woman = get_names(names_freq, "Mujer")
    print(f"Hay {len(name_woman)}")


if __name__ == "__main__":
    main()