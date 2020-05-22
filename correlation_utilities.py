def get_corr_visualization(df, independent_name, dependent_name):
	'''
	Returns the visualization to determine the relationship between
	independent variable and dependent variable.

	Requirement: 
		import matplotlib.pyplot as plt
		import seaborn as sns
		%matplotlib inline

	Parameters:
		df (DataFrame): The pandas DataFrame.
		independent_name (str): An independent variable's name.
		dependent_name (str): A dependent variable's name.

	'''

	x = df[independent_name]
	y = df[dependent_name]
	mpl.style.use('seaborn')

	sns.regplot(x=independent_name, y=dependent_name, data=df,
							scatter_kws={'s': 20},
							line_kws={'color': 'r'})
	
	plt.title('A relationship between ' + independent_name + ' and ' 
						+ dependent_name)
	plt.xlabel(independent_name)
	plt.ylabel(dependent_name)
	plt.show()
	plt.close()

def get_corr_stats(df, independent_name, dependent_name):
	x = df[independent_name]
	y = df[dependent_name]
	coef, pvalue = stats.pearsonr(x, y)

	print('The resulting coefficient is: ', coef)
	print('The p-value is: ', pvalue)
