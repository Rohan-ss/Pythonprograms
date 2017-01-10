# Program to convert Temp
class Conversion:
    def far(self,temp):
        # calculate fahrenheit
        fahrenheit = (temp * 1.8) + 32
        print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit ' %(temp,fahrenheit))

    def cal(self,temp):
        #Calculate Celsius
        celsius = (temp - 32)*5/9
        print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius ' %(temp,celsius))

def main():
    obj = Conversion()
    temp = float(input("Emter Temprature :"))
    print("Conversion...")
    ch = input("To fahrenheit Press F \nTo Celsius press C ")
    if ch == 'C':
        obj.cal(temp)
    elif ch == 'F':
        obj.far(temp)
main()




