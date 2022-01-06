ticket = int(input("Введите количество билетов\n"))
print(ticket)
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Введите возраст  {i} посетителя:\n"))
    if age <= 17:
        price.append(0)
    elif 17< age <= 24:
        price.append(990)
    elif 24 < age < 100:
        price.append(1390)
    else:
        print("Введен некоректный возраст")
    if ticket > 3:
        print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
    else:
        print("Сумма к оплате: ", sum(price), "рублей")
