from distutils.core import setup

setup(name='PyHighcharts',
	version='1.0',
	#py_modules=['foo'],
	description='A convenient wrapper for Highchart generation procedurally or on the command-line to browser output',
	author='Findlay Yeates',
	author_email='fidyeates@exeter.ac.uk.unconfirmed',
	url='https://github.com/fidyeates/PyHighcharts',
	packages=['highcharts','highcharts.ref'],
	#py_modules=['highcharts.chart','highcharts.ref'],
	#package_dir={'highcharts': 'highcharts'},
	)
