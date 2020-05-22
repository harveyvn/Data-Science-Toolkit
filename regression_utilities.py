def simple_linear_regression(df, independent_name, dependent_name):
	'''
	Returns the Linear Regression predictor.

	Requirement: 
		from sklearn.linear_model import LinearRegression

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_name (str): An independent variable's name.
		dependent_name (str): A dependent variable's name.

	Returns:
		lm (LinearRegression): The fitted Linear Regression model.
	'''

	X = df[[independent_name]]
	Y = df[dependent_name]

	lm = LinearRegression()
	lm.fit(X, Y)

	return lm

def multiple_linear_regression(df, independent_names, dependent_name):
	'''
	Returns the Multiple Linear Regression predictor.

	Requirement: 
		from sklearn.linear_model import LinearRegression

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_names (array): An array of independent variable's name.
		dependent_name (str): A dependent variable's name.

	Returns:
		lm (LinearRegression): The fitted Linear Regression model.
	'''

	Z = df[independent_names]
	Y = df[dependent_name]

	lm = LinearRegression()
	lm.fit(Z, Y)

	return lm

def get_mlr_plot(df, target_value, lms, independent_atts):
	'''
	Returns the distribution plot to determine the effectiveness for the multiple
	linear regression between multiple independent variables and a dependent variable.

	Requirements: 
		from sklearn.linear_model import LinearRegression
		import matplotlib as mpl
		import matplotlib.pyplot as plt
		import seaborn as sns
		%matplotlib inline

	Parameters:
		df (DataFrame): The pandas DataFrame.
		target_value (str): A dependent variable's name.
		lms (array): An array of the fitted Linear Regression models [lm1, lm2].
		independent_atts (array): An array of multiple independent variable's name.
			For example:
				[
					['lm1-col1', 'lm1-col2', 'lm1-col3'],
					['lm2-col1', 'lm2-col2']
				]

	'''

	mpl.style.use('seaborn')
	ax = sns.distplot(df[target_value], hist=False, color="r", label="Actual Value")

	step = 1
	for (lm, independent_names, color) in zip(lms, independent_atts, colors):
		label = 'lm with ' + str(len(independent_names)) + ' attributes'
		Yhat = lm.predict(df[independent_names])
		sns.distplot(Yhat, hist=False, label=label, ax=ax)
		step = step + 1

	plt.title('Actual vs Fitted Values for ' + target_value)
	plt.xlabel(target_value)
	plt.ylabel('Distribution')

	plt.show()
	plt.close()

def simple_polynomial_regression(df, independent_name, dependent_name, degree):
	'''
	Returns the Polynomial Regression poly1d.

	Requirement: 
		import numpy as np

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_name (str): An independent variable's name.
		dependent_name (str): A dependent variable's name.

	Returns:
		p (poly1d): The fitted Polynomial Regression model.
			>>> p(x)
	'''

	X = df[independent_name]
	Y = df[dependent_name]
	f = np.polyfit(X, Y, degree)
	p = np.poly1d(f)

	return p

def get_spr_visualization(df, model, independent_variable, dependent_variabble):
	'''
	Returns the visualization of Simple Polynomial Regression.

	Requirement: 
		import matplotlib as mpl
		import matplotlib.pyplot as plt
		%matplotlib inline

	Parameters:
		df (DataFrame): The pandas DataFrame.
		model (poly1d): The fitted Polynomial Regression model.
		independent_name (str): An independent variable's name.
		dependent_name (str): A dependent variable's name.

	'''

	x = df[independent_variable]
	y = df[dependent_variabble]
	x_new = np.linspace(x.min(), x.max(), x.size)
	y_new = model(x_new)

	mpl.style.use('seaborn')
	plt.plot(x, y, '.')
	plt.plot(x_new, y_new, '-')
	plt.title('Polynomial Fit with Matplotlib for ' 
	          + dependent_variabble + ' ~ ' + independent_variable)
	plt.xlabel(independent_variable)
	plt.ylabel(dependent_variabble)

	plt.show()
	plt.close()
