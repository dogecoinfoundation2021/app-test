
def dp_cal(dpi, cm):
	inch = cm/2.54
	pixel = dpi*inch
	dp = pixel * (160/dpi)

	return round(dp)

dp = dp_cal(96, 15)
print(dp)