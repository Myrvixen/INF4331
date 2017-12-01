from flask import Flask
from flask import render_template, request
from temperature_CO2_plotter import plot_temperature, plot_CO2, plot_CO2_country, plot_future

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("root.html")


@app.route("/plots")

def plots():

	return render_template("plots.html")


@app.route("/plots/temp_plot", methods=['GET', 'POST'])

def temp_plot():

	start_yearTemp = int(request.form["startyearTemp"])
	end_yearTemp = int(request.form["endyearTemp"]) 
	ymin = request.form["yminTemp"]
	ymax = request.form["ymaxTemp"]
	y_axis = [ymin, ymax]
	if ("Default" in y_axis) or ("" in y_axis):
		y_axis = None
	else:
		y_axis = [float(ymin), float(ymax)]

	month = request.form["month"]

	temp = plot_temperature(month, start_yearTemp, end_yearTemp, y_axis)
	return render_template("temp_plot.html", temp=temp )


@app.route("/plots/CO2_plot", methods=['GET', 'POST'])

def CO2_plot():

	start_yearCO2 = int(request.form["startyearCO2"])
	end_yearCO2 = int(request.form["endyearCO2"])
	ymin = request.form["yminCO2"]
	ymax = request.form["ymaxCO2"]
	y_axis = [ymin, ymax]
	if ("Default" in y_axis) or ("" in y_axis):
		y_axis = None
	else:
		y_axis = [float(ymin), float(ymax)]

	co2 = plot_CO2(start_yearCO2, end_yearCO2, y_axis)
	return render_template("co2_plot.html", co2=co2 )


@app.route("/CO2_by_country")
	
def country_index():

	return render_template("CO2_by_country.html")


@app.route("/CO2_by_country/bar_plot", methods=['GET', 'POST'])

def Bar_plot():

	year_country = int(request.form["yearCountry"])

	low_thresh = float(request.form["lowThresh"])
	upp_thresh = float(request.form["uppThresh"])

	co2_country = plot_CO2_country(year_country, low_thresh, upp_thresh)
	return render_template("bar_plot.html", co2_country=co2_country)


@app.route("/future")

def future_index():

	return render_template("future.html")

@app.route("/future/future_plot", methods=['GET', 'POST'])

def future_plot():

	fut_month = request.form["futMonth"]
	fut_year = int(request.form["futYear"])

	future = plot_future(fut_year, fut_month)
	return render_template("future_plot.html", future=future)

@app.route("/help")

def help():

	return"""<h1><b>Sadly I ran out of time, and wasn't able to complete
		this help page, as well as finishing writing doc-strings and comments in the codes.
		I was also unable to fit an error page into my tree of pages properly,
		but this can by checked out by going to 'http://127.0.0.1:5000/plots/error_temp'.
		I had big plans for this one, but oh well.
		</b><h1>
		"""


@app.route("/plots/error_temp")

def error_temp():
	return render_template("error_temp.html")

if __name__ == "__main__":
	app.run(debug=True)