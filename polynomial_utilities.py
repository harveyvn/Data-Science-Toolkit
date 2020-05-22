def simple_polynomial_regression(df, independent_name, dependent_name, degree):
	'''
	Returns the Polynomial Regression poly1d.

	Requirement: 
		import numpy as np

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_name (str): An independent variable's name.
		dependent_name (str): A dependent variable's name.
		degree (int): An order of polynomial regression.

	Returns:
		p (poly1d): The fitted Polynomial Regression model.
	
	Usage:
		p = simple_polynomial_regression(...)
		p(x)
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


def multiple_polynomia_regression(df, independent_names, dependent_name, degree):
	'''
	Returns the Polynomial Regression for more than one attribute

	Requirements: 
		from sklearn.pipeline import Pipeline
		from sklearn.linear_model import LinearRegression
		from sklearn.preprocessing import StandardScaler, PolynomialFeatures

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_names (array): An array of independent variable's name.
		dependent_name (str): A dependent variable's name.
		degree (int): An order of polynomial regression.
	
	Returns:
		pipe(Pipeline): The trainned Multiple Polynomial Regression model.

	Usage:
		pipe = multiple_polynomia_regression(...)
		pipe.predict(x)


	'''
	# We can normalize the data,  perform a transform and 
	# fit the model simultaneously. 
	Input=[('scale',StandardScaler()), 
				 ('polynomial', PolynomialFeatures(degree=degree, include_bias=False)), 
				 ('model',LinearRegression())]
	pipe = Pipeline(Input)
	Z = df[independent_names]
	Y = df[dependent_name]
	pipe.fit(Z,Y)

	return pipe
