import math
from decimal import Decimal

def binToHex(num):
    if not num:
        return ""
    return hex(int(num, 2))[2:].upper()

def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1

def fman(number):
    return Decimal(number).scaleb(-fexp(number)).normalize()

decValue = input("Enter decimal value: ")
Nsig = int(input("Enter bits before decimal: "))
Ndec = int(input("Enter bits after decimal: "))

wholeDecNum = decValue
neg = False
if decValue[0] == "-":
    neg = True
    decValue = float(decValue[1:])
else:
    decValue = float(decValue)

intValue = int(decValue)
fracValue = decValue % 1

binaryDecimal = ""
for _ in range(Ndec):
    fracValue *= 2
    if fracValue >= 1:
        binaryDecimal += "1"
        fracValue -= 1
    else:
        binaryDecimal += "0"

binaryWhole = ""
for _ in range(Nsig):
    intValue /= 2
    if intValue % 1 == 0.5:
        binaryWhole = "1" + binaryWhole
        intValue -= 0.5
    else:
        binaryWhole = "0" + binaryWhole

if neg:
    binaryWholeComp = ""
    for i in range(Nsig):
        if binaryWhole[i] == "0":
            binaryWholeComp += "1"
        else:
            binaryWholeComp += "0"

    binaryDecimalComp = ""
    for i in range(Ndec):
        if binaryDecimal[i] == "0":
            binaryDecimalComp += "1"
        else:
            binaryDecimalComp += "0"

    zeroIndex = 0
    zeroFound = False
    for i in range(Ndec-1,-1,-1):
        if binaryDecimalComp[i] == "0":
            zeroIndex = i
            zeroFound = True
            break
    
    finalWhole = ""
    finalDecimal = ""
    if not zeroFound:
        for i in range(Nsig-1,-1,-1):
            if binaryWholeComp[i] == "0":
                zeroIndex = i
                break

        for i in range(Nsig):
            if i > zeroIndex:
                finalWhole += "0"
            elif i == zeroIndex:
                finalWhole += "1"
            else:
                finalWhole += binaryWholeComp[i] 

        for i in range(Ndec):
            finalDecimal += "0"

    else:
        finalWhole = binaryWholeComp
        for i in range(Ndec):
            if i > zeroIndex:
                finalDecimal += "0"
            elif i == zeroIndex:
                finalDecimal += "1"
            else:
                finalDecimal += binaryDecimalComp[i]

if neg:
    finalNumBin = finalWhole + "." + finalDecimal
    finalNumHex = binToHex(finalWhole) + "." + binToHex(finalDecimal)
else:
    finalNumBin = binaryWhole + "." + binaryDecimal
    finalNumHex = binToHex(binaryWhole) + "." + binToHex(binaryDecimal)

print(f"Decimal Value: {decValue}")
print(f"Binary Value: {finalNumBin}")
print(f"Hex Value: {finalNumHex}")

if neg:
    sign = "1"
else:
    sign = "0"
frexp = math.frexp(float(wholeDecNum))

def mantissa(num):
    mantissaBin = finalNumBin[:finalNumBin.find("1")+1] + "." + finalNumBin[finalNumBin.find("1")+2:]
    # print(mantissaBin)
    exponent = mantissaBin.rfind('.') - mantissaBin.find('.')
    mantissaBin = mantissaBin[:mantissaBin.rfind(".")] + mantissaBin[mantissaBin.rfind(".")+1:]
    # mantissa = bin(mantissaBin).replace("0b","")
    return (mantissa, exponent)

print(f"Sign Mantissa Exponent: {sign} {mantissa(finalNumBin)[0]} {mantissa(finalNumBin)[1]}")
# print(f"Sign Mantissa Exponent: {sign} {fman(wholeDecNum)} {fexp(wholeDecNum)}")
