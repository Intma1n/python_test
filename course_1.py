import random

print('Hello world')


def calculate_something(a: int, b: str) -> str:
    res = ''

    for i in range(a):
        res += b + ' '

    return res


print(calculate_something(10, 'Something'))
print('''She said "hi" and he responded 'Hello!' ''')
print(random.randrange(1, 3))
my_not_tuple = (100)
my_tuple = (100,)
print(type(my_not_tuple))
print(type(my_tuple))
print([1] * 4)
my_str = 'weofuheiofiyhvwo8ehfqoifehigqugeqof8gifyw'
print(my_str.count('e'))
print('wrg3rg34g34fgtrtw'.index('g'))
my_str_2 = 'ewijfuewifbeibvier'
print(my_str_2.split('i'))
print(my_str_2.split('i'))

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0

for i in range(len(original_str)):
    print(i)
    num_chars += i

print(len(original_str))
print(num_chars)

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

splitted_week_temps = week_temps_f.split(',')

avg_temp = 0

for temp in splitted_week_temps:
    avg_temp += float(temp)

print(avg_temp)
print(len(splitted_week_temps))

print(avg_temp / len(splitted_week_temps))

print('x' not in 'apple')

print('============================')

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a', 'e', 'i', 'o', 'u']

num_vowels = 0

print(s.count('a'))

greeting = 'Hello World'
new_greeting = 'J' + greeting[1:]

print(new_greeting)

my_str_2 = 'orange'
my_str_3 = 'orange'

print(my_str_3 is my_str_2)  # true

my_obj_2 = [1, 2, 3]
my_obj_1 = [1, 2, 3]

print(my_obj_1 is my_obj_2)  # false
print(my_obj_1 == my_obj_2)  # true

my_obj_2 = my_obj_1
print(my_obj_1 == my_obj_2)  # true
print(my_obj_1 is my_obj_2)  # true

my_obj_2[0] = 5
print(my_obj_1)  # [5, 2, 3]

# Cloning

my_obj_3 = [1, 2, 3]
my_obj_4 = [1, 2, 3]

my_obj_4 = my_obj_3[:]

print(my_obj_3)

sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = "---".join(wrds)

print(new_sent)

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

splitted_scores = scores.split(' ')
print(splitted_scores)
sum = 0

for elem in splitted_scores:
    if int(elem) > 90:
        sum += 1

print(sum)

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ''

splitted_org = sent.split(' ')
print(splitted_org)

for elem in splitted_org:
    if elem not in stopwords:
        if splitted_org.index(elem) != len(splitted_org) - 1:
            acro = acro + elem[0].upper() + elem[1].upper() + '. '
        else:
            acro = acro + elem[0].upper() + elem[1].upper()

print(acro)

p_phrase = "was it a car or a cat I saw"
r_phrase = ''

splitted_p_phrase = p_phrase.split()
str_p_phrase = ''.join(splitted_p_phrase).lower()

print(str_p_phrase)

if str_p_phrase == str_p_phrase[::-1]:
    r_phrase = str_p_phrase

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    splitted_item = item.split(', ')
    print(
        'The store has {} {}, each for {:.2f} USD.'.format(splitted_item[1],
                                                           splitted_item[0],
                                                           float(splitted_item[2])))

oplaty = [300.00, 793.56, 650.00, 660.00, 550.00, 501.92, 508.72, 565.00, 730.00, 751.67]
sum = 0

for i in oplaty:
    sum += i

print('=======================')
print('Average chinsh: ', sum / len(oplaty))

print('Сколько остается по-идее:', 7500 - (1200 + 3600 + 600 + 35 + 80))
