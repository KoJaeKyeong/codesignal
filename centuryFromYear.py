def centuryFromYear(year):
    if (year % 100)==0:
        return int(year/100)
    elif (year % 100)>0:
        return int(year/100+1)
