year = int(input("Write the year "))
marja = year - 1600
if year > 1600:
    count = (marja // 4) - (marja // 100) + (marja // 400) + 1   # +1 is about 1600
    print(count)
elif year == 1600:
    count = 1
    print(count)
else:
    print("incorrect number")