#nalogi
print("Сумма заказа:")
summa = float(input())
chaevix = summa * 0.18
nalog = summa * 0.20

print("Налог:", format(nalog, '.2f'),"\nЧаевые:", format(chaevix, '.2f'), "\nИтог:", format(chaevix+nalog, '.2f'))