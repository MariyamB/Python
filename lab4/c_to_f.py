#source code:c_to_f.py
#name: Sai Ratnam Peri


def c_2_f(temp_celsius):
    temp_farenheit = temp_celsius * (9 / 5) + 32
    return(temp_farenheit)

def main():
    temp_celsius = float(input("please enter the temperature in degrees celsius :"))
    farenheit_temp  = c_2_f(temp_celsius)
    print(temp_celsius, "degrees C is equvalent to ", farenheit_temp, " degrees F")

if __name__ == '__main__':
    main()
