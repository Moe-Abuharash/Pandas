import pandas as pd


produce_dictionary = {'Potatoes': [0.86, 12219, 10508],
                      'Okra': [2.26, 12960, 29290],
                      'Fava beans': [2.69, 11703, 31480],
                      'Watermelon': [0.66, 11485, 7580],
                      'Garlic': [1.19, 12512, 14889],
                      'Parsnips': [2.27, 11270, 25584],
                      'Asparagus': [2.49, 12848, 31991],
                      'Avocados': [3.23, 12369, 39953],
                      'Celery': [3.07, 12334, 37866],
                      'Spinach': [4.12, 11740, 48367],
                      'Cucumber': [1.07, 11994, 12834],
                      'Apricots': [3.71, 11762, 43637],
                      'Ginger': [5.13, 11915, 61126],
                      'Corn': [1.07, 11702, 12522],
                      'Grapefruit': [0.76, 11707, 8897],
                      'Eggplant': [2.32, 11843, 27477],
                      'Green cabbage': [0.8, 11611, 9289],
                      'Yellow peppers': [2.87, 12160, 34899],
                      'Grapes': [2.63, 12294, 32333],
                      'Cherries': [9.5, 12384, 117653],
                      'Apples': [1.88, 12397, 23307],
                      'Green beans': [2.52, 11483, 28938],
                      'Tomatoes': [3.16, 12016, 37969],
                      'Red onion': [0.78, 12549, 9788],
                      'Strawberries': [4.4, 11692, 51446],
                      'Papaya': [1.34, 11775, 15779],
                      'Butternut squash': [1.28, 11495, 14713],
                      'Bananas': [0.86, 12629, 10861],
                      'Lettuce': [1.88, 11891, 22355],
                      'Carrots': [1.26, 12204, 15377],
                      'Daikon': [1.4, 12146, 17004],
                      'Lime': [1.06, 11934, 12650],
                      'Green peppers': [1.89, 11981, 22645],
                      'Beets': [1.51, 12255, 18506],
                      'Coconuts': [1.18, 11840, 13972],
                      'Orange': [1.09, 11180, 12187],
                      'Lemon': [1.29, 12382, 15974],
                      'Brussels sprouts': [1.65, 11947, 19713],
                      'Kale': [5.02, 12293, 61711],
                      'Bok choy': [1.42, 11565, 16422]}


produce = pd.DataFrame(produce_dictionary)
produce.index = ['Cost Per Pound', 'Quantity Sold', 'Total Sale']
print(produce.T)


print('-------------QUESTION 1----------------------')
max = produce.loc['Total Sale'].idxmax(), produce.loc['Total Sale'].max()
min = produce.loc['Total Sale'].idxmin(), produce.loc['Total Sale'].min()
print(max)
print(min)


print('-------------QUESTION 2----------------------')
a = produce.loc[['Quantity Sold', 'Total Sale'], ['Orange', 'Beets']]
print(a.T)

print('-------------QUESTION 3----------------------')

b = produce.loc[['Total Sale'], 'Apples':'Lettuce']
print(b.T)


print('-------------QUESTION 4----------------------')

at_1 = produce.at['Quantity Sold', 'Apricots'] = 11955
at_2 = produce.at['Total Sale', 'Apricots'] = 44353.05

d = produce.loc[['Quantity Sold', 'Total Sale'], ['Apricots']]
print(d.T)

print('-------------QUESTION 5----------------------')

avg_qty = produce.loc['Quantity Sold'].mean()
print(avg_qty)

print('-------------QUESTION 6----------------------')


check_qty = produce[(produce > 11500) & (produce < 12000)]
print(check_qty.T)


print('-------------QUESTION 7----------------------')

print(check_qty.loc['Total Sale'].sum())

#check_qty = produce.loc['Total Sale'].sum()
# print(check_qty)
