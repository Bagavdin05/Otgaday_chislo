from colorama import init
from colorama import Fore, Back, Style
import random
init()

while True:

     print(Fore.CYAN)

     chislo1 = int(input("\nОтгадайте число от 1 до 5: "))

     rand = (random.randint(1, 5))

     if rand == chislo1:
         print(Fore.GREEN)
         print("Правильно!")
         input()

     else:
         print(Fore.RED)
         chislo2 = int(input("\nНепрaвильно, попробуйте ещё раз!: "))

         if rand == chislo2:
             print(Fore.GREEN)
             print("Правильно!")
             input()

         else:
             print(Fore.RED)
             print("Непрaвильно!")
             print(f"Было загадно число: {rand}")