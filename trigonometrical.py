import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np
import pandas as pd



def main():
	plt.figure(0, dpi=600, figsize=[8, 4])
	x = []
	y = []
	y2 = []
	y3 = []
	for z in range(-360, 360, 1):
		x.append(z)
		y.append(z)
		y2.append(z)
		y3.append(z)
	x = np.array(x)
	y = np.array(y) 
	y2 = np.array(y2)
	y3 = np.array(y3)
	y = y * np.pi / 180
	y2 = y2 * np.pi / 180
	y3 = y3 * np.pi / 180
	y = np.sin(y)
	y2 = np.cos(y2)
	y3 = np.tan(y3)
	df = pd.DataFrame({ "degrees": x, "sine of the degree": y, "cosine of the degree": y2, "tangent of the degree": y3})
	print(df.head())
	plt.xlim(-360, 360)
	plt.ylim(-5, 5)
	plt.title("Charles Truscott Watters")
	plt.plot(x, y, color='green', ms=12, label="sine x degrees")
	plt.plot(x, y2, color='gold', ms=12, label="cosine x degrees")
	plt.plot(x, y3, color='cornflowerblue', ms=12, label="tangent x degrees")
	plt.legend()
	plt.savefig('/sdcard/trigonometrical.pdf', papertype='a4', dpi=600)
	df.to_html('/sdcard/trigonometrical.html')
main()