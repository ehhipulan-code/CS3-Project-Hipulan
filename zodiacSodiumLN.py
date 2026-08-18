def chineseZodiacSign(year):
    return ( year - 1900 )% 12
    
year = (int(input("Enter your year of birth: ")))


if year < 1900:
    print("Year must not be before 1900.")

else:
    zodiac = chineseZodiacSign(year)

    if zodiac == 0:
        print("Your Chinese Zodiac sign is Rat (鼠/Shũ)")
    elif zodiac == 1:
        print("Your Chinese Zodiac sign is Ox (牛/Niú)")
    elif zodiac == 2:
        print("Your Chinese Zodiac sign is Tiger (虎/Hǔ)")
    elif zodiac == 3:
        print("Your Chinese Zodiac sign is Rabbit (兔/Tù)")
    elif zodiac == 4:
        print("Your Chinese Zodiac sign is Dragon (龙/ Lóng)")
    elif zodiac == 5:
        print("Your Chinese Zodiac sign is Snake (蛇/Shé)")
    elif zodiac == 6:
        print("Your Chinese Zodiac sign is Horse (马/ Mã)")
    elif zodiac == 7:
        print("Your Chinese Zodiac sign is Goat (羊/ Yáng)")
    elif zodiac == 8:
        print("Your Chinese Zodiac sign is Monkey (猴/Hóu)")
    elif zodiac == 9:
        print("Your Chinese Zodiac sign is Rooster (鸡/JT)")
    elif zodiac == 10:
        print("Your Chinese Zodiac sign is Dog (狗/Gou)")
    elif zodiac == 11:
        print("Your Chinese Zodiac sign is Pig (猪/Zhū)")
