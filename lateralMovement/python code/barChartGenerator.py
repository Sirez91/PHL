import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from dataForEvaluation import *

### Score + Fehlerdiff
labels = ['1', '2', '4', '5', '6', '7', '8', '9', '10', '11']
score = score_divided_by_1000
errorDiffUnAided = diffUnAided
errorDiffAided = diffAided

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 2*(width/3), score, width*(2/3), label='Score')
rects2 = ax.bar(x, errorDiffUnAided, width*(2/3), label='Fehlerdifferenz ohne Hilfe')
rects3 = ax.bar(x + 2*(width/3), errorDiffAided, width*(2/3), label='Fehlerdifferenz mit Hilfe')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Fehlerunterschied / Score in tausend Punkten')
ax.set_xlabel('Probanden-Id')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

### Piano Touch

labels2 = ['1', '2', '3', '4']

x2 = np.arange(len(labels2))  # the label locations
width2 = 0.35  # the width of the bars

fig2, ax2 = plt.subplots()
rects2_1 = ax2.bar(x2 - width/2, pianoTouch_not_stimulted, width2, label='ohne taktile Stimulation')
rects2_2 = ax2.bar(x2 + width/2, pianoTouch_stimulted, width2, label='mit taktiler Stimulation')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_ylabel('Fehler')
ax2.set_xlabel('Probanden-Id')
ax2.set_xticks(x2)
ax2.set_xticklabels(labels2)
ax2.legend()

ax2.bar_label(rects2_1, padding=3)
ax2.bar_label(rects2_2, padding=3)

fig2.tight_layout()

### MMT1

labels3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

x3 = np.arange(len(labels3))  # the label locations
width3 = 0.35  # the width of the bars

fig3, ax3 = plt.subplots()
rects3_1 = ax3.bar(x3 - width/2, MMT_reductionNonTactile, width3, label='ohne taktile Stimulation')
rects3_2 = ax3.bar(x3 + width/2, MMT_redutionTactile, width3, label='mit taktiler Stimulation')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax3.set_ylabel('Reduktion der Fehleranzahl')
ax3.set_xlabel('Probanden-Id')
ax3.set_xticks(x3)
ax3.set_xticklabels(labels3)
ax3.legend()

ax3.bar_label(rects3_1, padding=3)
ax3.bar_label(rects3_2, padding=3)

fig3.tight_layout()

### tphl

labels4 = ['Kontroll','Akustisch','Akustisch+Taktil','Taktil']

x4 = np.arange(len(labels4))  # the label locations
width4 = 0.35  # the width of the bars

fig4, ax4 = plt.subplots()
rects4_1 = ax4.bar(x4, TPHL_means, width4)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax4.set_ylabel('Fehlerdifferenz')
ax4.set_xlabel('Bedingung')
ax4.set_xticks(x4)
ax4.set_xticklabels(labels4)
ax4.legend()

ax4.bar_label(rects4_1, padding=0)

fig4.tight_layout()

### tphl2

labels5 = ["einhändig", "beidhändig"]

x5 = np.arange(len(labels5))  # the label locations
width5 = 0.35  # the width of the bars

fig5, ax5 = plt.subplots()
rects5_1 = ax5.bar(x5 - width/2, TPHL_Pre, width5, label='Vortest')
rects5_2 = ax5.bar(x5 + width/2, TPHL_Post, width5, label='Test')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax5.set_ylabel('Fehler in %')
ax5.set_xlabel('Bedingung')
ax5.set_xticks(x5)
ax5.set_xticklabels(labels5)
ax5.legend()

ax5.bar_label(rects5_1, padding=3)
ax5.bar_label(rects5_2, padding=3)
ax5.set_ylim([0, 100])

fig5.tight_layout()


### SHOW


plt.show()