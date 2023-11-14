from names import *

def main():
    names_freq = read_names_freq("./data/frecuencias_nombres.csv")
    print(f"we have {len(names_freq)} names frequency")
    print(f"First name and year {names_freq[0]}")


if __name__ == "__main__":
    main()