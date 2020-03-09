
def divisible(year, condition):
    return True if (year % condition == 0) else False


def is_leap_year(year: int) -> bool:

    leap = False

    div_by_4 = divisible(year, 4)
    div_by_100 = divisible(year, 100)
    div_by_400 = divisible(year, 400)

    if div_by_4 and not div_by_100:
        leap = True
    elif div_by_4 and div_by_100 and div_by_400:
        leap = True

    return leap
