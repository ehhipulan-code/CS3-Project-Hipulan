1. Create a zodiacSectionLN.py file. This file will contain your solutions to the
requirements below:
a. Ask the user to enter a year of birth. The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.
Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900
d. Otherwise determine the chinese zodiac sign based on the following starting from 1900. Note: A zodiac sign will recur after each 12 years.
i. Rat (凤/Shū)
ii. Ox (牛/Niu)
IIL Tiger (虎/Hū)
IV. Rabbit (兔/Tù)
V. Dragon (龙 /Lóng)
We. Snake (蛇/Shé)
vii. Horse (马/Mã)
viii.
Goat (羊/ Yáng)
IX. Monkey (猴/Hóu)
X Rooster (鸡/ Jī)
xi. Dog (狗/Gõu)
xii.
Pig (猪/Zhū)
e. CONSIDER only the year of birth.
Example input and output:
Enter your birth year:
2000
Your Chinese Zodiac Sign is: Dragon (龙/ Lóng)
2. Test and Run your code before submitting.
3. Document this graded exercise in your Github portfolio and save it in zodiac SectionLN.md. This .md will include the requirements for this coding exercise, your actual code and a screenshot of your output. Update also your README.md file to have the link to your files.
4. Commit your changes in your github account and submit the live code link to your teacher and also your .git repository link.
5. Refer to Annex D for Code Exercise Rubrics for Grading.
















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
























<img width="950" height="557" alt="image" src="https://github.com/user-attachments/assets/c0b2d568-8151-46c0-88cc-aacbec0d9a33" />
