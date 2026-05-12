def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


check = 2020

result = is_year_leap(check)

print("год", + check, ":", result)
