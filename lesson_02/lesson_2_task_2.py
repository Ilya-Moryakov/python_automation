def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


check = 1500

result = is_year_leap(check)

print("год", check, ":", result)
