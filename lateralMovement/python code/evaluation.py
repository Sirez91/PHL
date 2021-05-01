from scipy.stats import ranksums
from scipy import stats
import numpy as np
from scipy.stats import mannwhitneyu
from operator import sub
import matplotlib.pyplot as plt
from dataForEvaluation import *

# Wilcoxon for equal n
sample1 = diffUnAided
sample2 = score_divided_by_1000
print("Equal wilcoxon: " + str(ranksums(sample1, sample2)))
sample1 = diffAided
sample2 = score_divided_by_1000
print("Equal wilcoxon: " + str(ranksums(sample1, sample2)))
sample1 = design2
sample2 = design3
print("Equal wilcoxon prestudy: " + str(ranksums(sample1, sample2)))

# Wilcoxon for unequal n
print("Unequal wilcoxon unAidedDiff: " + str(mannwhitneyu(diffUnAided, diffUnAidedOldDesign)))
print("Unequal wilcoxon aidedDiff: " + str(mannwhitneyu(diffAided, diffAidedOldDesign)))
print("Unequal wilcoxon errorsPrePassiv: " + str(mannwhitneyu(errorsTest, errorsTestOldDesign)))
print("Unequal wilcoxon errorsUnAided: " + str(mannwhitneyu(errorsPostTestUnAided, errorsPostTestUnAidedoldDesign)))
print("Unequal wilcoxon errorsAided: " + str(mannwhitneyu(errorsPostTestAided, errorsPostTestAidedoldDesign)))
# old old 
print("Unequal wilcoxon unAidedDiff: " + str(mannwhitneyu(diffUnAided, diffUnAidedOldOldDesign)))
print("Unequal wilcoxon aidedDiff: " + str(mannwhitneyu(diffAided, diffAidedOldOldDesign)))
print("Unequal wilcoxon design: " + str(mannwhitneyu(design2, design3)))

#shapiro
print("Shapiro d2: " + str(stats.shapiro(design2)))
print("Shapiro d3: " + str(stats.shapiro(design3)))
print("Shapiro diffUnAided: " + str(stats.shapiro(diffUnAided)))
print("Shapiro diffUnAidedOldDesign: " + str(stats.shapiro(diffUnAidedOldDesign)))
print("Shapiro diffUnAidedOldOldDesign: " + str(stats.shapiro(diffUnAidedOldOldDesign)))
print("Shapiro diffAided: " + str(stats.shapiro(diffAided)))
print("Shapiro diffAidedOldDesign: " + str(stats.shapiro(diffAidedOldDesign)))
print("Shapiro diffAidedOldOldDesign: " + str(stats.shapiro(diffAidedOldOldDesign)))

print("mean diff diffUnAided: " + str(np.mean(diffUnAided)));
print("mean diff diffUnAidedOldDesign: " + str(np.mean(diffUnAidedOldDesign)));
print("mean diff diffAided: " + str(np.mean(diffAided)));
print("mean diff diffAidedOldDesign: " + str(np.mean(diffAidedOldDesign)));
print("mean diff diffUnAidedOldOldDesign: " + str(np.mean(diffUnAidedOldOldDesign)));
print("mean diff diffAidedOldOldDesign: " + str(np.mean(diffAidedOldOldDesign)));

#t-test
print("t-test : " + str(stats.ttest_ind(design3,design4,equal_var=True)));
