import math

def main():
    print("program menghitung keliling lingkaran")
    r = float(input("Masukkan nilai jari-jari :"))
    Keliling = 2 * math.pi * r
    print(f"Keliling lingkaran: {Keliling}")
if __name__== "__main__":
    main()