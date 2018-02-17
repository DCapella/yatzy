from dice import *
from hands import *
from scoresheets import *
import os

def sep(num):
    print('-'*12)
    print('TEST {} START'.format(num))
    print('-'*12)

sep(1)
d = Die()
print('d = Die():\n' + str(d.value))

sep(2)
d6 = Die(sides=6)
print('d6 = Die(sides=6):\n' + str(d6.value))

sep(3)
d6 = D6()
print('d6 = D6():\n' + str(d6.value))

sep(4)
d6 = D6()
print('int(d6)\n' + str(int(d6)))

sep(5)
print(
d6 < 2,
d6 > 1,
d6 != 4,
d6 == 6
)

sep(6)
d1 = D6()
d2 = D6()

print(int(d1))
print(int(d2))
print(d1 + d2)

sep(7)
hand = Hand(size=5, die_class=D6)
print(hand)
print(len(hand))
print(hand[0].value)

sep(8)
yh = YatzyHand()
print(yh)

sep(9)
hand = YatzyHand()
three = D6(value=3)
four = D6(value=4)
one = D6(value=1)
hand[:] = [one, three, three, four, four]
print(YatzyScoresheet().score_one_pair(hand))

input('...')
os.system('clear')
print('END OF TESTS')
