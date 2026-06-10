def month_to_season(n):
    if n in [12, 1, 2]:
        return "Зима"
    if n in [3, 4, 5]:
        return "Весна"
    if n in [6, 7, 8]:
        return "Лето"
    if n in [9, 10, 11]:
        return "Осень"


print(month_to_season())
