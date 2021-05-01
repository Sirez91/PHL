from dataForEvaluation import *#diffAided, diffAidedOldDesign, diffUnAided, diffUnAidedOldDesign, errorsPostTestAided, errorsPostTestUnAided, errorsTest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_box_plot_data(labels, bp):
    rows_list = []

    for i in range(len(labels)):
        dict1 = {}
        dict1['label'] = labels[i]
        dict1['lower_whisker'] = bp['whiskers'][i*2].get_ydata()[1]
        dict1['lower_quartile'] = bp['boxes'][i].get_ydata()[1]
        dict1['median'] = bp['medians'][i].get_ydata()[1]
        dict1['upper_quartile'] = bp['boxes'][i].get_ydata()[2]
        dict1['upper_whisker'] = bp['whiskers'][(i*2)+1].get_ydata()[1]
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)

# Fehlerdiff unaided
my_dict = {'Donchev Alt': diffUnAidedOldOldDesign, 'Donchev Neu': diffUnAidedOldDesign, 'Aktueller Handschuh': diffUnAided}

fig1, ax1 = plt.subplots()
ax1.set_title('Fehlerdifferenz vor Orientierungshilfe')
bp1 = ax1.boxplot(my_dict.values())
ax1.set_xticklabels(my_dict.keys())

# Fehlerdiff aided
my_dict2 = {'Donchev Alt': diffAidedOldOldDesign, 'Donchev Neu': diffAidedOldDesign, 'Verbessertes Design': diffAided}

fig2, ax2 = plt.subplots()
ax2.set_title('Fehlerdifferenz nach Orientierungshilfe')
bp2 = ax2.boxplot(my_dict2.values())
ax2.set_xticklabels(my_dict2.keys())

# Anzahl Fehler test
my_dict3 = {'Donchev Neu': errorsTestOldDesign, 'Verbessertes Design': errorsTest}

fig3, ax3 = plt.subplots()
ax3.set_title('Fehleranzahl vor der passiven Phase')
bp3 = ax3.boxplot(my_dict3.values())
ax3.set_xticklabels(my_dict3.keys())

# Anzahl Fehler unaided
my_dict4 = {'Donchev Neu': errorsPostTestUnAidedoldDesign, 'Verbessertes Design': errorsPostTestUnAided}

fig4, ax4 = plt.subplots()
ax4.set_title('Fehleranzahl vor Orientierungshilfe')
bp4 = ax4.boxplot(my_dict4.values())
ax4.set_xticklabels(my_dict4.keys())

# Anzahl Fehler aided
my_dict5 = {'Donchev Neu': errorsPostTestAidedoldDesign, 'Verbessertes Design': errorsPostTestAided}

fig5, ax5 = plt.subplots()
ax5.set_title('Fehleranzahl nach Orientierungshilfe')
bp5 = ax5.boxplot(my_dict5.values())
ax5.set_xticklabels(my_dict5.keys())

print(get_box_plot_data(['Donchev Alt','Donchev Neu','Verbessertes Design'], bp1))
print(get_box_plot_data(['Donchev Alt','Donchev Neu','Verbessertes Design'], bp2))
print(get_box_plot_data(['Donchev Neu','Verbessertes Design'], bp3))
print(get_box_plot_data(['Donchev Neu','Verbessertes Design'], bp4))
print(get_box_plot_data(['Donchev Neu','Verbessertes Design'], bp5))

# Designs
my_dict6 = {'A': design1,'B': design2,'C': design3,'D': design4}

fig6, ax6 = plt.subplots()
bp6 = ax6.boxplot(my_dict6.values())
ax6.set_xticklabels(my_dict6.keys())
plt.show()