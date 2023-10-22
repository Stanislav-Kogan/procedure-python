salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
k_increase = increase + 1 # Множитель увеличения расходов
money_required = 0 # Количетсво недостающих денег

for _ in range(months):
    money_required += spend - salary
    spend *= k_increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_required, 2))
