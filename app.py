print("Bienvenido al horóscopo")
print("########################")
user_input= ""

def menu():
    print("Selecciona el número correspondiente a tu signo")
    print("1","Aquarius")
    print("2","Aries")
    print("3","Cancer")
    print("4","Capricornus")
    print("5","Gemini")
    print("6","Leo")
    print("7","Libra")
    print("8","Pisces")
    print("9","Sagittarius")
    print("10","Scorpio")
    print("11","Taurus")
    print("12","Virgo")
    print("0","Salir")
    print("color de la suerte")

user_input = ""

def read_file(app):
        file = open("signs/"+ app,"r", encodings="UTF-8")
        for line in file:
            print(line)

while user_input != "exit":
   menu()
   user_input = input()
   if user_input == "1":
      read_file("Aquarius.txt")
   elif user_input == "2":
      read_file("Aries.txt")
   elif user_input == "3":
      read_file("Cancer.txt")
   elif user_input == "4":
      read_file("Capricornus.txt")
   elif user_input == "5":
      read_file("Gemini.txt")
   elif user_input == "6":
      read_file("Leo.txt")
   elif user_input == "7":
      read_file("Libra.txt") 
   elif user_input == "8":
      read_file("Pisces.txt")
   elif user_input == "9":
      read_file("Sagittarius.txt")
   elif user_input == "10":
      read_file("Scorpio.txt")
   elif user_input == "11":
      read_file("Taurus.txt")
   elif user_input == "12":
      read_file("Virgo.txt")


   elif user_input == "0":
      print("########################")    
      print("Hasta la proxima")
      print("########################")
      exit()

   else:
      print("########################")
      print("opción incorrecta")
      print("########################")
