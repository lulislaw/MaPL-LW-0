print("Кол-во бутылок <= 1 литра:")         #Вывод
a = float(input())                          #Ввод в формате float
print("Кол-во бутылок > 1 литра:")          #Вывод
b = float(input())                          #Ввод в формате float

s = a*0.10 + b*0.25                         #рассчет
print("Summa = $", format(s, '.2f'))        #Вывод
