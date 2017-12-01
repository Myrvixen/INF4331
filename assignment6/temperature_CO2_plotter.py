import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

def plot_temperature(month, start_year, end_year, y_axis=None, show_plot=False):

	temp_stats = pd.read_csv('temperature.csv', sep=',')

	first_year = temp_stats['Year'][0]
	start_idx = start_year-first_year
	end_idx = end_year-first_year

	temp_stats[start_idx:end_idx].plot(x='Year', y=month, ylim=y_axis)
	plt.ylabel('Temperature (C)')
	plt.title('Average temperature in US %g-%g' %(start_year, end_year))
	plt.savefig("static/Temp.png")
	if show_plot:
		plt.show()



def plot_CO2(start_year, end_year, y_axis=None, show_plot=False):

	CO2_stats = pd.read_csv('co2.csv', sep=',')
	
	first_year = CO2_stats['Year'][0]
	start_idx = start_year-first_year
	end_idx = end_year-first_year

	CO2_stats[start_idx: end_idx].plot(x='Year', y='Carbon')
	plt.ylabel('CO2 emission (MMT)')
	plt.title('Global CO2 emmisions %g-%g' % (start_year, end_year))
	plt.savefig('static/CO2.png')
	if show_plot:
		plt.show()


def plot_CO2_country(years, low_thresh=0, upp_thresh=10000, show_plot=False):

	if type(years) in [float, int]:
		years = str(years)
	elif type(years) in [list, tuple]:
		years = [str(year) for year in years]

	CO2_cntr_stats = pd.read_csv('CO2_by_country.csv', sep=',')


	thresholds = (upp_thresh > CO2_cntr_stats[years]) & (CO2_cntr_stats[years] > low_thresh)

	#thresholds = upp_thresh > CO2_cntr_stats['2012'] > low_thresh

	CO2_cntr_stats[thresholds].plot(x='Country Code', y=years, kind='bar')

	if show_plot:
		plt.show()

def plot_future(year, month):

	CO2_stats = pd.read_csv('co2.csv', sep=',')

	last_CO2 = CO2_stats['Carbon'].values[-1]
	sec_last_CO2 = CO2_stats['Carbon'].values[-2]
	diff_CO2 = last_CO2 - sec_last_CO2

	first_year = CO2_stats['Year'].values[0]
	last_year = CO2_stats['Year'].values[-1]

	no_years = year-last_year


	CO2_fut = np.array([last_CO2 + i*diff_CO2 for i in range(no_years + 1)])
	years_fut = np.array([last_year + i for i in range(no_years + 1)])

	CO2_future = pd.DataFrame({'Year': years_fut, 'Carbon': CO2_fut})
	print(CO2_future)
	'''
	ax = CO2_stats[-10:].plot(x='Year', y='Carbon', label='Data')
	plt.ylabel('CO2 emission (MMT)')
	CO2_future.plot(x='Year', y='Carbon', ax=ax, label='Predicted future')
	plt.show()
	'''
	temp_stats = pd.read_csv('temperature.csv', sep=',')


	#--------------------------------------
	# Temp is linear of CO2, T(x) = ax + b
	# Finding 'a' by interpolating 10 steps
	#--------------------------------------------

	T = np.array(temp_stats[month].tail(30))
	CO2 = np.array(CO2_stats['Carbon'].tail(30))
	years = np.array(CO2_stats['Year'].tail(30))

	#---------------
	# Simple method
	#a = (T[-1] - T[0])/(CO2[-1] - CO2[0])
	#---------------

	#Linear regression (The last three values returned from the function
	# will not be used.)
	#--------------------
	a, b, r_value, p_value, std_err = stats.linregress(CO2, T)


	temps = a*CO2 + b
	temps_fut = a*(CO2_fut-CO2_fut[0]) + T[-1]

	plt.plot(years, T)
	plt.plot(years_fut, temps_fut)
	plt.show()
	



if __name__ == '__main__':
	#plot_temperature('June', 1816, 2012, show_plot=True)
	#plot_CO2(1751, 2012, show_plot=True)
	#plot_CO2_country(2012, low_thresh=15, upp_thresh=50, show_plot=True)
	plot_future(2030, 'June')