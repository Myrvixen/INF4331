from flask import Flask
from flask import render_template
from temperature_CO2_plotter import plot_temperature, plot_CO2

app = Flask(__name__)

@app.route("/")#, methods=['POST'])
def root():
	return render_template("root.html")

"""
def temp():
	plot_temperature('June', 1816, 2012)
	plot_CO2(1751, 2012)
	return render_template("test.html")
"""


@app.route("/plots", methods=['GET', 'POST'])

def plots():

	start_yearTemp = int(request.form["startyearTemp"])
	end_yearTemp = int(request.form["endyearTemp"])
	plot_temperature('June', start_yearTemp, end_yearTemp)

	return render_template("plots.html")

@app.route("/plots/temp_plot")

def plot():
	#plot_temperature('June', start_yearTemp, end_yearTemp)
	return render_template("test.html")

@app.route("/plots/error_temp")

def error_temp():
	return render_template("error_temp.html")

if __name__ == "__main__":
	app.run(debug=True)