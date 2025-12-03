

def smooth_func(x,y,fil,order,kind='linear'):
	import numpy as np
	from scipy.signal import savgol_filter
	from scipy.interpolate import interp1d

	xx = np.linspace(x.min(),x.max(), 1000)
	itp = interp1d(x,y, kind=kind)
	window_size, poly_order = fil, order
	yy_sg = savgol_filter(itp(xx), window_size, poly_order)

	return xx, yy_sg


