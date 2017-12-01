import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
from io import BytesIO

def plot_temperature(month, start_year, end_year, y_axis=None, show_plot=False):
	"""This function takes a month and a start year and end year as required
	arguments. It generates a Pandas dataframe of all data found in the file
	temperature.csv, and plots the data corresponding to the month and the range
	of the years given as arguments. 
	One also has the possibility to change the y-axis, but if no argument is given
	it's just set to default. 
	There is also an argument show_plot that's set to False as default to avoid 
	the plot to pop up from the terminal when the program is run on the website.
	A bytestring cointaing the bytes of the plot will be generated in this case
	instead of saving the image as a png/jpg-file.

	"""
	temp_stats = pd.read_csv('temperature.csv', sep=',')

	first_year = temp_stats['Year'][0]
	start_idx = start_year-first_year
	end_idx = end_year-first_year

	temp_stats[start_idx:end_idx].plot(x='Year', y=month, ylim=y_axis)
	plt.ylabel('Temperature (C)')
	plt.title('Average temperature in US %g-%g' %(start_year, end_year))
	if show_plot:
		plt.show()
	else:
		Tempfile = BytesIO()
		plt.savefig(Tempfile, format='png')
		Tempfile.seek(0)  # rewind to beginning of file
		import base64
		Tempdata_png = base64.b64encode(Tempfile.getvalue()).decode()
		return Tempdata_png



def plot_CO2(start_year, end_year, y_axis=None, show_plot=False):

	CO2_stats = pd.read_csv('co2.csv', sep=',')
	
	first_year = CO2_stats['Year'][0]
	start_idx = start_year-first_year
	end_idx = end_year-first_year

	CO2_stats[start_idx: end_idx].plot(x='Year', y='Carbon')
	plt.ylabel('CO2 emission (MMT)')
	plt.title('Global CO2 emmisions %g-%g' % (start_year, end_year))
	if show_plot:
		plt.show()
	else:
		CO2file = BytesIO()
		plt.savefig(CO2file, format='png')
		CO2file.seek(0)  # rewind to beginning of file
		import base64
		CO2data_png = base64.b64encode(CO2file.getvalue()).decode()
		return CO2data_png


def plot_CO2_country(year, low_thresh=0, upp_thresh=10000, show_plot=False):

	year=str(year)

	CO2_cntr_stats = pd.read_csv('CO2_by_country.csv', sep=',')

	thresholds = (upp_thresh > CO2_cntr_stats[year]) & (CO2_cntr_stats[year] > low_thresh)

	CO2_cntr_stats[thresholds].plot(x='Country Code', y=year, kind='bar')
	plt.ylabel('CO2 emission (MMT)')
	plt.title('Countries with CO2 emmisions in range %g-%g MMT (%s)' % (low_thresh, upp_thresh, year))

	if show_plot:
		plt.show()
	else:
		Countryfile = BytesIO()
		plt.savefig(Countryfile, format='png')
		Countryfile.seek(0)  # rewind to beginning of file
		import base64
		Countrydata_png = base64.b64encode(Countryfile.getvalue()).decode()
		return Countrydata_png

def plot_future(year, month, show_plot=False):

	CO2_stats = pd.read_csv('co2.csv', sep=',')

	last_CO2 = CO2_stats['Carbon'].values[-1]
	sec_last_CO2 = CO2_stats['Carbon'].values[-2]
	diff_CO2 = last_CO2 - sec_last_CO2

	last_year = CO2_stats['Year'].values[-1]
	no_years = year-last_year


	CO2_fut = np.array([last_CO2 + i*diff_CO2 for i in range(no_years + 1)])
	years_fut = np.array([last_year + i for i in range(no_years + 1)])


	temp_stats = pd.read_csv('temperature.csv', sep=',')


	#--------------------------------------
	# Temp is linear of CO2, T(x) = ax + b
	# Finding 'a' and 'b by interpolating 30 steps using linear regression
	#--------------------------------------------

	temps_past = np.array(temp_stats[month].tail(30))
	CO2 = np.array(CO2_stats['Carbon'].tail(30))
	years = np.array(CO2_stats['Year'].tail(30))


	#Linear regression (The last three values returned from the function
	# will not be used.)
	#--------------------
	a, b, r_value, p_value, std_err = stats.linregress(CO2, temps_past)


	temps = a*CO2 + b
	temps_fut = a*(CO2_fut-CO2_fut[0]) + temps_past[-1]

	Temp = pd.DataFrame({'Year': years, 'Temp': temps_past})
	Temp_future = pd.DataFrame({'Year': years_fut, 'Temp': temps_fut})


	ax = Temp.plot(x='Year', y='Temp', label="Data")
	Temp_future.plot(x='Year', y='Temp', ax=ax, label="Future")
	plt.ylabel("Temperature(C)")
	plt.title("Predicted temperature of %s up to year %g" % (month, year))

	if show_plot:
		plt.show()
	else:
		Futurefile = BytesIO()
		plt.savefig(Futurefile, format='png')
		Futurefile.seek(0)  # rewind to beginning of file
		import base64
		Futuredata_png = base64.b64encode(Futurefile.getvalue()).decode()
		return Futuredata_png
	



if __name__ == '__main__':
	#plot_temperature('June', 1816, 2012, show_plot=True)
	#plot_CO2(1751, 2012, show_plot=True)
	#plot_CO2_country(2012, low_thresh=15, upp_thresh=50, show_plot=True)
	plot_future(2030, 'June', show_plot=True)