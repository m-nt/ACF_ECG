import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
import Peak
from scipy import io

f = io.loadmat("file.mat")

#dict_keys(['__header__', '__version__', '__globals__', 'val'])
data = f["val"][1]

Peak.detect_peaks(data,mph=0,show=True)

plot_acf(data)
plt.show()
