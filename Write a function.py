def is_leap(year):
    leap = False
    if year%4:
        return False
    elif year%100:
        return True
    elif year%400:
        return False
    else:
        return True
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
