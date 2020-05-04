def numberToWords(number):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }.get(number, "")


def multiplesOfTen(number):
    localWord = "" if number < 20 else "-" + numberToWords(number % 10)
    tens = number if number < 20 else number//10
    return {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "ninteen",
        2: "twenty" + localWord,
        3: "thirty" + localWord,
        4: "fourty" + localWord,
        5: "fifty" + localWord,
        6: "sixty" + localWord,
        7: "seventy" + localWord,
        8: "eightty" + localWord,
        9: "ninety" + localWord,
    }.get(tens, "")


def denominationToWords(number):
    return {
        1: "thousand",
        2: "million",
        3: "billion",
        4: "trillion",
        5: "quadrillion",
        6: "quintillion",
        7: "sextillion",
        8: "septillion",
        9: "octillion"
    }.get(number, "")


def hundredsWord(number, denomCounter=0):
    quotient = number % 1000
    tenth = multiplesOfTen(quotient % 100) if (quotient %
                                               100) > 9 else numberToWords(quotient % 100)
    word = (numberToWords(quotient // 100) +
            " hundred ") if quotient > 99 else ""
    word += (("and " if denomCounter == 0 else "") +
             tenth) if tenth != "" else ""
    return (hundredsWord(number // 1000, (denomCounter + 1)) + " " if number//1000 > 0 else "") + word + " " + (denominationToWords(denomCounter) if quotient > 0 else "")


print("*"*20)
print(hundredsWord(2912345675))
print("*"*20)
print(hundredsWord(10956501))
print("*"*20)
print(hundredsWord(1000000000))
print("*"*20)
print(hundredsWord(100))
print("*"*20)
print(hundredsWord(101))
